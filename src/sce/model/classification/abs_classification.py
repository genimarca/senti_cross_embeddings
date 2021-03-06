#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from abc import ABCMeta, abstractmethod

class ABSClassification(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Constructor
        '''
        
    @property
    @abstractmethod
    def random_seed(self):
        pass
    
    @random_seed.setter
    @abstractmethod
    def random_seed(self, a_random_seed):
        pass
    
    @property
    @abstractmethod
    def training_corpus(self):
        pass
    
    @training_corpus.setter
    @abstractmethod
    def training_corpus(self, a_training_corpus):
        pass
    
    @property
    @abstractmethod
    def evaluation_corpus(self):
        pass
    
    @evaluation_corpus.setter
    @abstractmethod
    def evaluation_corpus(self, a_evaluation_corpus):
        pass
    
    @property
    @abstractmethod
    def predictions(self):
        pass
    
    @property
    @abstractmethod
    def allow_labels(self):
        pass
    
    @allow_labels.setter
    @abstractmethod
    def allow_labels(self, a_allow_labels):
        pass
        
    @property
    @abstractmethod
    def nlp_utils(self):
        """
        """
        
    @nlp_utils.setter
    @abstractmethod
    def nlp_utils(self, a_nlp_utils):
        """
        """
    
    
    @abstractmethod
    def make_feature_space_training(self, external_knowledge=None):
        pass
    
    @abstractmethod
    def make_feature_space_evaluation(self, external_knowledge=None):
        pass
    
    @abstractmethod
    def training(self):
        pass
    
    @abstractmethod
    def evaluation(self):
        pass
    
    
    
    