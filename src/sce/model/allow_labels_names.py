#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from enum import Enum, unique

@unique
class AllowLabelsNames(Enum):
    '''
    classdocs
    '''


    BILABEL = "sce.model.bilabel_experiments.BiLabelExperiments"
    
    TRILABEL = "sce.model.trilabel_experiments.TriLabelExperiments"
