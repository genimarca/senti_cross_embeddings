#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from abc import ABCMeta, abstractmethod

class ABSWordEmbeddings(metaclass=ABCMeta):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params):
        '''
        Sole constructor
        '''
        
        
    @property
    @abstractmethod
    def word_embeddings(self):
        pass
    
    @property
    @abstractmethod
    def word_indexes(self):
        pass
    
    @abstractmethod
    def is_word(self, word):
        pass
    
    @abstractmethod
    def get_vector_embedding(self, word):
        pass
    
    @abstractmethod
    def get_word_index(self, word):
        pass
    
    @abstractmethod
    def load(self, path, encoding, ofset=None, max_words=None, vocabulary=None):
        pass
    
    @abstractmethod
    def get_number_of_embeddings(self):
        pass
    
    @abstractmethod
    def get_vector_embedding_dimension(self):
        pass
    
    @abstractmethod
    def set_vector_embedding(self, word, index, vector_embedding):
        pass