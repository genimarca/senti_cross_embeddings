#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from enum import Enum, unique

@unique
class ClassificationNames(Enum):
    '''
    classdocs
    '''


    SVM = "sce.model.classification.svm_classification.SVMClassification"
    
    