#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from sce.model.properties_manager import PropertiesManager
from sce.model.properties_names import PropertiesNames  
from sce.model.dao.factory_corpus import FactoryCorpus
from sce.model.factory_allow_labels import FactoryAllowLabels

class ModelPipeline:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Sole constructor
        '''
        self.__encoding = None
        self.__training_corpus = None
        self.__evaluation_corpus = None
        self.__external_knowledge = []
        self.__allow_labels = None
        
        
    def initialization(self, properties_file_path):
        PropertiesManager.load_properties(properties_file_path)
        
        
        self.__encoding = PropertiesManager.get_prop_value(PropertiesNames.ENCODING.value)
        
        allow_labels_name = PropertiesManager.get_prop_value(PropertiesNames.ALLOW_LABELS_NAME.value)
        self.__allow_labels = FactoryAllowLabels.creator(allow_labels_name)
        
        corpus_training_name = PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TRAINING_NAME.value)
        self.__training_corpus = FactoryCorpus.creator(corpus_training_name)
        self.__training_corpus.encoding = self.__encoding
        self.__training_corpus.allow_labels = self.__allow_labels
        
        print("Begin: Loading training corpus")
        self.__training_corpus.load(PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TRAINING_PATH.value))
        print("End: Loading training corpus")
        
        corpus_test_name = PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TEST_NAME.value)
        self.__evaluation_corpus = FactoryCorpus.creator(corpus_test_name)
        
        self.__evaluation_corpus.encoding = self.__encoding
        self.__evaluation_corpus.allow_labels = self.__allow_labels
        print("Begin: Loading training corpus")
        self.__evaluation_corpus.load(PropertiesManager.get_prop_value(PropertiesNames.CORPUS_TEST_PATH.value))
        
    
    
    def training(self):
        pass
    
    def classification(self):
        pass
    
    def results(self):
        pass