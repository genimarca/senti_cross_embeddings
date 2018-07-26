#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from sce.model.classification.abs_classification import ABSClassification
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sce.model.nlp_utils import NLPUtils
from sce.model.properties_manager import PropertiesManager
from sce.model.properties_names import PropertiesNames
from lxml.html.diff import token
from numpy.random import seed as np_seed

class SVMClassification(ABSClassification):
    '''
    SVM with TF-IDF
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.__random_seed = None
        self.__training_corpus = None
        self.__evaluation_corpus = None
        self.__predictions = None
        self.__features_training = None
        self.__features_test = None
        self.__classifier = None
        self.__features_transformers = []
        self.__allow_labels = None
        
        
    @property
    def random_seed(self):
        return self.__random_seed
    
    @random_seed.setter
    def random_seed(self, a_random_seed):
        self.__random_seed = a_random_seed
    
    @property
    def training_corpus(self):
        return self.__training_corpus
    
    @training_corpus.setter
    def training_corpus(self, a_training_corpus):
        self.__training_corpus = a_training_corpus
        
        
    @property
    def evaluation_corpus(self):
        return self.__evaluation_corpus
    
    @evaluation_corpus.setter
    def evaluation_corpus(self, a_evaluation_corpus):
        self.__evaluation_corpus = a_evaluation_corpus
        
    @property
    def predictions(self):
        return self.__predictions
    
    
    @property
    def allow_labels(self):
        return self.__allow_labels
    
    @allow_labels.setter
    def allow_labels(self, a_allow_labels):
        self.__allow_labels = a_allow_labels
    
    
    def __feature_engineering(self, corpus):
        
        for doc_index in corpus.corpus:
            doc = corpus.get_document(doc_index)
            preparing_text = NLPUtils.normalization_lowercase(doc.raw_text)
            preparing_text = NLPUtils.normalization_users(preparing_text, "@user")
            preparing_text = NLPUtils.tokenize_tweet(preparing_text, a_preserve_case=False, a_reduce_len=True, a_strip_handles=False)
            if PropertiesManager.get_prop_value(PropertiesNames.NORM_STOPPER):
                preparing_text = NLPUtils.stopper(preparing_text, PropertiesManager.get_prop_value(PropertiesNames.LANGUAGE_TRAINING))
            if PropertiesManager.get_prop_value(PropertiesNames.NORM_STEMMER):
                preparing_text = NLPUtils.stemmer(preparing_text, PropertiesManager.get_prop_value(PropertiesNames.LANGUAGE_TRAINING))
            doc.process_text = preparing_text
                
    
    def __dummy_tokenizer(self, doc):
        return doc
    
    def make_feature_space_training(self, external_knowledge=None):
        
        self.__feature_engineering(self.__training_corpus)
        
        tfidf_vectorizer = TfidfVectorizer(
            analyzer="word",
            tokenizer=self.__dummy_tokenizer,
            preprocessor=self.__dummy_tokenizer,
            token_pattern=None)
        
        
        docs = [self.__training_corpus.get_document(doc_id).process_text for doc_id in self.__training_corpus.corpus]
        
        self.__features_training = tfidf_vectorizer.fit_transform(docs)
        self.__features_transformers.append(tfidf_vectorizer)
        
        
        
    def make_feature_space_evaluation(self, external_knowledge=None):
        
        self.__feature_engineering(self.__evaluation_corpus)
        
        docs = [self.__evaluation_corpus.get_document(doc_id).process_text for doc_id in self.__evaluation_corpus.corpus]
        
        self.__features_test = self.__features_transformers[0].transform(docs)
        for transformer in self.__features_transformers[1:]:
            self.__features_test = transformer.transform(self.__feature_test)
        
        
    def training(self):
        docs_labels = [self.__training_corpus.get_document(doc_id).sparse_label for doc_id in self.__training_corpus.corpus]
        np_seed(self.__random_seed)
        self.__classifier = SVC(kernel="linear")
        self.__classifier.fit(self.__features_training, docs_labels)
        
    def evaluation(self):
        self.__predictions = self.__classifier.predict(self.__features_test)
        
        
    
        