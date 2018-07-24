#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from enum import Enum, unique

class PropertiesNames(object):
    '''
    classdocs
    '''
    
    RANDOM_SEED = "RANDOM_SEED"
    
    ENCODING = "ENCODING"
    
    LANGUAGE_TRAINING = "LANGUAGE_TRAINING"
    
    LANGUAGE_TEST = "LANGUAGE_TEST"
    
    CORPUS_TRAINING_NAME = "CORPUS_TRAINING_NAME"
    
    CORPUS_TRAINING_PATH = "CORPUS_TRAINING_PATH"
    
    CORPUS_TEST_NAME = "CORPUS_TEST_NAME"
    
    CORPUS_TEST_PATH = "CORPUS_TEST_PATH"
    
    EMBEDDINGS_NAME = "EMBEDDNGS_NAME"
    
    EMBEDDINGS_PATH = "EMBEDINGS_PATH"
    
    ALLOW_LABELS_NAME = "ALLOW_LABELS_NAME"
    
    CLASSIFICATION_NAME = "CLASSIFICATION_NAME"
    
    NORM_STOPPER = "NORM_STOPPER"
    
    NORM_STEMMER = "NORM_STEMMER"
    
    OUTPUT_FILE_PATH = "OUTPUT_FILE_PATH"
    
    