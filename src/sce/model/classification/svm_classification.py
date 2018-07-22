#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from sce.model.classification.abs_classification import ABSClassification

class SVMClassification(ABSClassification):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__training_corpus = None
        self.__evaluation_corpus = None
        self.__results = None
        self.__predictions = None
        
        
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
    def results(self):
        return self.__results
    
    @property
    def predictions(self):
        return self.__predictions
    
    
    def training(self):
        