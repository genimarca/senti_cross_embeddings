#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from enum import Enum, unique

@unique
class NLPUtilsNames(Enum):
    '''
    classdocs
    '''


    NLPUTILS_LONG = "sce.model.nlp_utils_long.NLPUtilsLong"
    
    NLPUTILS_TWITTER = "sce.model.nlp_utils_twitter.NLPUtilsTwitter"
