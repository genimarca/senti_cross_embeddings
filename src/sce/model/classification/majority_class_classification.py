#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from sce.model.classification.abs_classification import ABSClassification
from scipy.stats import mode as sp_mode

class MajorityClassClassification(ABSClassification):
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
        
        pass
                
    
    def __dummy_tokenizer(self, doc):
        return doc
    
    def make_feature_space_training(self, external_knowledge=None):
        
        pass
        
        
        
    def make_feature_space_evaluation(self, external_knowledge=None):
        
        pass
        
        
    def training(self):
        docs_labels = [self.__training_corpus.get_document(doc_id).sparse_label for doc_id in self.__training_corpus.corpus]
        self.__classifier = sp_mode(docs_labels, axis=None)[0][0]
        
    def evaluation(self):
        self.__predictions = [self.__classifier]*self.__evaluation_corpus.get_size()
        
        
    
        