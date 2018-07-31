#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from sce.model.properties_manager import PropertiesManager
from sce.model.properties_names import PropertiesNames  
from sce.model.dao.factory_corpus import FactoryCorpus
from sce.model.factory_allow_labels import FactoryAllowLabels
from sce.model.classification.factory_classification import FactoryClassification
from sce.model.embeddings.factory_embeddings import FactoryEmbeddings
from sce.model.classification.results_metrics import ResultsMetrics

class ModelPipeline:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Sole constructor
        '''
        self.__encoding = None
        self.__training_corpus = None
        self.__evaluation_corpus = None
        self.__embeddings_handler = None
        self.__embeddings_evaluation_handler = None
        self.__allow_labels = None
        self.__allow_labels_evaluation = None
        self.__classifier = None
        self.__random_seed = None
        self.__external_knowledge = {}
        
        
    def initialization(self, properties_file_path):
        PropertiesManager.load_properties(properties_file_path)
        
        
        self.__encoding = PropertiesManager.get_prop_value(PropertiesNames.ENCODING)
        
        self.__random_seed = PropertiesManager.get_prop_value(PropertiesNames.RANDOM_SEED)
        if self.__random_seed is not None:
            self.__random_seed = int(self.__random_seed)
        
        allow_labels_name = PropertiesManager.get_prop_value(PropertiesNames.ALLOW_LABELS_NAME)
        self.__allow_labels = FactoryAllowLabels.creator(allow_labels_name)
        allow_labels_evaluation_name = PropertiesManager.get_prop_value(PropertiesNames.ALLOW_LABELS_EVALUATION_NAME)
        if allow_labels_evaluation_name is None:
            self.__allow_labels_evaluation = self.__allow_labels
        else:
            self.__allow_labels_evaluation = FactoryAllowLabels.creator(allow_labels_evaluation_name)
        
        corpus_training_name = PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TRAINING_NAME)
        self.__training_corpus = FactoryCorpus.creator(corpus_training_name)
        self.__training_corpus.encoding = self.__encoding
        self.__training_corpus.allow_labels = self.__allow_labels
        
        print("Begin: Loading training corpus")
        self.__training_corpus.load(PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TRAINING_PATH))
        print("End: Loading training corpus")
        
        corpus_test_name = PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TEST_NAME)
        self.__evaluation_corpus = FactoryCorpus.creator(corpus_test_name)
        
        self.__evaluation_corpus.encoding = self.__encoding
        self.__evaluation_corpus.allow_labels = self.__allow_labels_evaluation
        print("Begin: Loading evaluation corpus")
        self.__evaluation_corpus.load(PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TEST_PATH))
        print("End: Loading evaluation corpus")
        
        
        #Creation of the specific classification algorithm.
        classifier_name = PropertiesManager.get_prop_value(PropertiesNames.CLASSIFICATION_NAME)
        self.__classifier = FactoryClassification.creator(classifier_name)
        
        embeddings_name = PropertiesManager.get_prop_value(PropertiesNames.EMBEDDINGS_NAME)
        if embeddings_name is not None:
            self.__embeddings_handler = FactoryEmbeddings.creator(embeddings_name)
            self.__external_knowledge["embeddings"] = self.__embeddings_handler
            
        
        cross_lingual_experiment = PropertiesManager.get_prop_value(PropertiesNames.CROSS_LINGUAL_EXPERIMENT)
        if cross_lingual_experiment:
            embeddnigs_evaluation_name = PropertiesManager.get_prop_value(PropertiesNames.EMBEDDINGS_EVALUATION_NAME)
            if embeddings_name is not None:
                self.__embeddings_evaluation_handler = FactoryEmbeddings.creator(embeddnigs_evaluation_name)
                self.__external_knowledge["embeddings_evaluation"] = self.__embeddings_evaluation_handler
        
    
    
    def training(self):
        self.__classifier.training_corpus = self.__training_corpus
        self.__classifier.random_seed = self.__random_seed
        self.__classifier.allow_labels = self.__allow_labels
        self.__classifier.make_feature_space_training(external_knowledge=self.__external_knowledge)
        print("Begin: Training")
        self.__classifier.training()
        print("End: Training")
        
            
    def classification(self):
        self.__classifier.evaluation_corpus = self.__evaluation_corpus
        self.__classifier.make_feature_space_evaluation(external_knowledge=self.__external_knowledge)
        print("Begin: Evaluation")
        self.__classifier.evaluation()
        print("End: Test")
    
    def results(self):
        
        corpus_training_size_str = "Train_size:\t {}".format(self.__training_corpus.get_size())
        training_doc_x_class_str = "\n".join(["Train_size {}:\t{}".format(self.__allow_labels.get_label_name(label_index),self.__training_corpus.doc_x_labels[label_index]) for label_index in sorted(self.__allow_labels.label_index())])
        corpus_training_size_str = "{}\n{}".format(corpus_training_size_str,training_doc_x_class_str)
        print(corpus_training_size_str)
        
        corpus_evaluation_size_str = "Eva_size:\t {}".format(self.__evaluation_corpus.get_size())
        evaluation_doc_x_class_str = "\n".join(["Eva_size {}:\t{}".format(self.__allow_labels_evaluation.get_label_name(label_index),self.__evaluation_corpus.doc_x_labels[label_index]) for label_index in sorted(self.__allow_labels_evaluation.label_index())])
        corpus_evaluation_size_str = "\n\n{}\n{}".format(corpus_evaluation_size_str,evaluation_doc_x_class_str)
        print(corpus_evaluation_size_str)
        
        real_labels = [self.__evaluation_corpus.get_document(doc_id).sparse_label for doc_id in self.__evaluation_corpus.corpus]
        predictions = self.__classifier.predictions
        confusion_matrix = ResultsMetrics.confusion_matrix(real_labels, predictions)
        confusion_matrix_string = ["Pred_{}".format(self.__allow_labels_evaluation.get_label_name(label_index)) for label_index in sorted(self.__allow_labels.label_index())]
        confusion_matrix_string = "\t" + "\t".join(confusion_matrix_string)
        confusion_matrix_string = "{}\n{}".format(confusion_matrix_string, "\n".join(["R_" + self.__allow_labels.get_label_name(i) + "\t" + "\t".join([str(j) if j is not None else str(0) for j in confusion_matrix[i]]) for i in range(len(confusion_matrix))]))
        
        precision_x_class = ResultsMetrics.precision_x_class(real_labels, predictions, self.__allow_labels_evaluation)
        precision_x_class_string = "\n".join(["Prec. {}: {}".format(self.__allow_labels_evaluation.get_label_name(label_index), precision_x_class[label_index]) for label_index in precision_x_class])
        recall_x_class = ResultsMetrics.recall_x_class(real_labels, predictions, self.__allow_labels_evaluation)
        recall_x_class_str = "\n".join(["Recall {}: {}".format(self.__allow_labels_evaluation.get_label_name(label_index), recall_x_class[label_index]) for label_index in recall_x_class])
        f1_x_class = ResultsMetrics.f1_x_class(real_labels, predictions, self.__allow_labels_evaluation)
        f1_x_class_str = "\n".join(["F1 {}: {}".format(self.__allow_labels_evaluation.get_label_name(label_index), f1_x_class[label_index]) for label_index in f1_x_class])
        
        macro_precision_str = "Macro-Precision: {}".format(ResultsMetrics.macro_precision(real_labels, predictions))
        macro_recall_str = "Macro-Recall: {}".format(ResultsMetrics.macro_recall(real_labels,predictions))
        macro_f1_str = "Macro-F1: {}".format(ResultsMetrics.macro_f1(real_labels, predictions))
        accuracy_str = "Accuracy: {}".format(ResultsMetrics.accuracy(real_labels, predictions))
        
        
        print("\n"+confusion_matrix_string+"\n")
        print(precision_x_class_string)
        print(recall_x_class_str)
        print(f1_x_class_str)
        print(macro_precision_str)
        print(macro_recall_str)
        print(macro_f1_str)
        print(accuracy_str)
        
