#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from abc import ABCMeta, abstractmethod

class ABSAllowLabel(metaclass=ABCMeta):
    '''
    It defines the allow labels of the experiments
    '''

    @abstractmethod
    def __init__(self):
        '''
        Constructor
        '''
        
    @property
    @abstractmethod
    def number_of_labels(self):
        """
        """
        
        
    @abstractmethod
    def label_index(self):
        """
        """
    
    @abstractmethod
    def get_label_index(self, raw_label):
        """It returns None in case raw_label is not allowed.
        """
        
    @abstractmethod
    def  get_label_name(self, label_index):
        """
        """