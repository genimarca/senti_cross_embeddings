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
        self.__allow_labels = None
        self.__classifier = None
        self.__random_seed = None
        
        
    def initialization(self, properties_file_path):
        PropertiesManager.load_properties(properties_file_path)
        
        
        self.__encoding = PropertiesManager.get_prop_value(PropertiesNames.ENCODING)
        
        self.__random_seed = PropertiesManager.get_prop_value(PropertiesNames.RANDOM_SEED)
        if self.__random_seed is not None:
            self.__random_seed = int(self.__random_seed)
        
        allow_labels_name = PropertiesManager.get_prop_value(PropertiesNames.ALLOW_LABELS_NAME)
        self.__allow_labels = FactoryAllowLabels.creator(allow_labels_name)
        
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
        self.__evaluation_corpus.allow_labels = self.__allow_labels
        print("Begin: Loading evaluation corpus")
        self.__evaluation_corpus.load(PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TEST_PATH))
        print("End: Loading evaluation corpus")
        
        
        #Creation of the specific classification algorithm.
        classifier_name = PropertiesManager.get_prop_value(PropertiesNames.CLASSIFICATION_NAME)
        self.__classifier = FactoryClassification.creator(classifier_name)
        
        embeddings_name = PropertiesManager.get_prop_value(PropertiesNames.EMBEDDINGS_NAME)
        if embeddings_name is not None:
            self.__embeddings_handler = FactoryEmbeddings.creator(embeddings_name)
        
    
    
    def training(self):
        self.__classifier.training_corpus = self.__training_corpus
        self.__classifier.random_seed = self.__random_seed
        self.__classifier.make_feature_space_training(external_knowledge=self.__embeddings_handler)
        self.__classifier.training()
        
            
    def classification(self):
        self.__classifier.evaluation_corpus = self.__evaluation_corpus
        self.__classifier.make_feature_space_evaluation(external_knowledge=self.__embeddings_handler)
        self.__classifier.evaluation()
    
    def results(self):
        
        real_labels = [self.__evaluation_corpus.get_document(doc_id).sparse_label for doc_id in self.__evaluation_corpus.corpus]
        predictions = self.__classifier.predictions
        confusion_matrix = ResultsMetrics.confusion_matrix(real_labels, predictions)
        confusion_matrix_string = ["Pred_{}".format(self.__allow_labels.get_label_name(label_index)) for label_index in sorted(self.__allow_labels.label_index())]
        confusion_matrix_string = "\t" + "\t".join(confusion_matrix_string)
        confusion_matrix_string = "{}\n{}".format(confusion_matrix_string, "\n".join(["R_" + self.__allow_labels.get_label_name(i) + "\t" + "\t".join([str(j) for j in confusion_matrix[i]]) for i in range(len(confusion_matrix))]))
        
        precision_x_class = ResultsMetrics.precision_x_class(real_labels, predictions, self.__allow_labels)
        precision_x_class_string = "\n".join(["Prec. {}: {}".format(self.__allow_labels.get_label_name(label_index), precision_x_class[label_index]) for label_index in precision_x_class])
        recall_x_class = ResultsMetrics.recall_x_class(real_labels, predictions, self.__allow_labels)
        recall_x_class_str = "\n".join(["Recall {}: {}".format(self.__allow_labels.get_label_name(label_index), recall_x_class[label_index]) for label_index in recall_x_class])
        f1_x_class = ResultsMetrics.f1_x_class(real_labels, predictions, self.__allow_labels)
        f1_x_class_str = "\n".join(["F1 {}: {}".format(self.__allow_labels.get_label_name(label_index), f1_x_class[label_index]) for label_index in f1_x_class])
        
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
        
