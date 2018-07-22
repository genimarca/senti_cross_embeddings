#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from sce.model.classification.abs_classification import ABSClassification
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import sklearn.svm.SVC as sksvm

class SVMClassification(ABSClassification):
    '''
    SVM with TF-IDF
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__training_corpus = None
        self.__evaluation_corpus = None
        self.__predictions = None
        self.__features_training = None
        self.__features_test = None
        self.__classifier = None
        self.__features_transformers = []
        
        
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
    
    
    def make_feature_space_training(self, external_knowledge=None):
        
        count_vectorizer = CountVectorizer()
        docs = [self.__training_corpus.get_document(doc_id).process_text for doc_id in self.__training_corpus.corpus]
        self.__features_training = count_vectorizer.fit_transform(docs)
        tfidf_transformer = TfidfTransformer()
        self.__features_training = tfidf_transformer.fit_transform(self.__features_training)
        self.__features_transformers.append(count_vectorizer)
        self.__features_transformers.append(tfidf_transformer)
        
        
    def make_feature_space_evaluation(self, external_knowledge=None):
        
        docs = [self.__evaluation_corpus.get_document(doc_id).process_text for doc_id in self.__evaluation_corpus.corpus]
        self.__features_test = self.__features_transformers[0].transform(docs)
        for transformer in self.__features_transformers[1:]:
            self.__features_test = transformer.transform()
        
    def training(self):
        docs_labels = [self.__training_corpus.get_document(doc_id).sparse_label for doc_id in self.__training_corpus.corpus]
        self.__classifier = sksvm()
        self.__classifier.fit(self.__features_training, docs_labels)
        
    def evaluation(self):
        self.__predictions = self.__classifier.predict(self.__features_test)
        
        
    
        