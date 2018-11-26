#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from sce.model.abs_allow_labels import ABSAllowLabel 

class BilabelExperiments(ABSAllowLabel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Sole constructor
        '''
        
        self.__labels = {0:("NEGATIVE",["N","negative"]), 1:("POSITIVE",["P","positive"]), 2:("Not_available", ["Not Available"])}
        self.__number_of_labels = 2
        
        
    @property
    def number_of_labels(self):
        return self.__number_of_labels
    
    def label_index(self):
        """
        """
        return list(self.__labels.keys())
    
    def get_label_index(self, raw_label):
        """It returns NONE in case the @raw_label is not allowed.
        
        """
        
        i=0
        stop=False
        label_index = None
        while(i < self.__number_of_labels and not stop):
            if raw_label in self.__labels[i][1]:
                stop = True
                label_index = i
            else:
                i+=1
        
        return label_index
    
    def get_label_name(self, label_index):
        
        label_name = None
        if label_index in self.__labels:
            label_name = self.__labels[label_index][0] 
        
        return label_name
        