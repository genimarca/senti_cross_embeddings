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
    
    """
    It indicates if the experiment is cross_lingual, i.e. the embeddings in training
    and test are different.
    """
    CROSS_LINGUAL_EXPERIMENT = "CROSS_LINGUAL_EXPERIMENT"
    
    LANGUAGE_TRAINING = "LANGUAGE_TRAINING"
    
    LANGUAGE_TEST = "LANGUAGE_TEST"
    
    CORPUS_TRAINING_NAME = "CORPUS_TRAINING_NAME"
    
    CORPUS_TRAINING_PATH = "CORPUS_TRAINING_PATH"
    
    CORPUS_TEST_NAME = "CORPUS_TEST_NAME"
    
    CORPUS_TEST_PATH = "CORPUS_TEST_PATH"
    
    EMBEDDINGS_NAME = "EMBEDDNGS_NAME"
    
    EMBEDDINGS_PATH = "EMBEDINGS_PATH"
    
    EMBEDDINGS_MAX_WORDS = "EMBEDDINGS_MAX_WORDS"
    
    EMBEDDINGS_EVALUATION_NAME = "EMBEDDINGS_EVALUATION_NAME"
    
    EMBEDDINGS_EVALUATION_PATH = "EMBEDDINGS_EVALUATION_PATH"
    
    EMBEDDINGS_EVALUATION_MAX_WORDS = "EMBEDDINGS_EVALUATION_MAX_WORDS"
    
    ALLOW_LABELS_NAME = "ALLOW_LABELS_NAME"
    
    ALLOW_LABELS_EVALUATION_NAME = "ALLOW_LABELS_EVALUATION_NAME"
    
    CLASSIFICATION_NAME = "CLASSIFICATION_NAME"
    
    NORM_STOPPER = "NORM_STOPPER"
    
    NORM_STEMMER = "NORM_STEMMER"
    
    NORM_USER = "NORM_USER"
    
    NN_BATCH_SIZE = "NN_BATCH_SIZE"
    
    NN_EPOCH_SIZE = "NN_EPOCH_SIZE"
    
    OUTPUT_PRED_FILE_PATH = "OUTPUT_PRED_FILE_PATH"
    
    NLP_UTILS = "NLP_UTILS"
    
    
    