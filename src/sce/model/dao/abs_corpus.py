#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 13 jul. 2018

@author: Eugenio Martínez Cámara
'''

from abc import ABCMeta, abstractmethod

class ABSCorpus(metaclass=ABCMeta):
    '''
    It defines the method of a corpus
    '''

    @abstractmethod
    def __init__(self):
        '''
        Sole constructor
        '''
        
        
        
    @property
    @abstractmethod
    def allow_labels(self):
        """
        """
        
    @allow_labels.setter
    @abstractmethod
    def allow_labels(self, a_allow_labels):
        """
        """
    
    @property
    @abstractmethod
    def encoding(self):
        """
        """
    
    @encoding.setter
    @abstractmethod
    def encoding(self, a_encoding):
        """
        """
        
    @property
    @abstractmethod
    def corpus(self):
        """
        """
    
    @property
    @abstractmethod
    def doc_ids(self):
        """
        """
        
    @property
    @abstractmethod
    def doc_x_labels(self):
        """
        """
    
    @abstractmethod
    def load(self, path):
        """
        """
        
    @abstractmethod
    def get_document(self, a_id):
        """
        """
        
    @abstractmethod
    def get_size(self):
        """
        """
        
        
    @abstractmethod
    def clean(self):
        """
        """