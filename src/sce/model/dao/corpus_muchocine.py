#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2 oct. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from sce.model.dao.abs_corpus import ABSCorpus
from sce.model.bilabel_experiments import BilabelExperiments
from sce.model.document import Document
from collections import OrderedDict


class CorpusMuchoCine(ABSCorpus):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__allow_labels=None
        self.__encoding = "utf-8"
        self.__corpus=OrderedDict()
        self.__doc_x_labels = None
        self.__SEP_CHAR = "\";\""
        
        
    @property
    def allow_labels(self):
        """
        """
        return self.__allow_labels
        
        
    @allow_labels.setter
    def allow_labels(self, a_allow_labels):
        """
        """
        self.__allow_labels = a_allow_labels
        
    @property
    def encoding(self):
        """
        """
        return self.__encoding
        
    @encoding.setter
    def encoding(self, a_encoding):
        """
        """
        self.__encoding = a_encoding
        
    @property
    def corpus(self):
        """
        """
        return self.__corpus
        
    def doc_ids(self):
        """
        """
        
        return list(self.__corpus.keys())
        
    @property
    def doc_x_labels(self):
        """
        """
        if self.__doc_x_labels is None:
            self.__doc_x_labels = {self.__corpus[doc_id].raw_label:0 
                                   if self.__corpus[doc_id].raw_label not in self.__doc_x_labels else self.__doc_x_labels[self.__corpus[doc_id].raw_label]+1 
                                   for doc_id in self.__corpus.keys()}
            
        return self.__doc_x_labels
        
    
    @property        
    def is_tokenized(self):
        """
        """
        return self.__is_tokenized
        
    @is_tokenized.setter        
    def is_tokenized(self, a_is_tokenized):
        """
        """
        
        self.__is_tokenized = a_is_tokenized
        
    @property
    def is_lowercase(self):
        """
        """
        return self.__is_lowercase
        
    @is_lowercase.setter
    def is_lowercase(self, a_is_lowercase):
        """
        """
        self.__is_lowercase = a_is_lowercase
    
    
    def __add_document(self, line):
        """
        """
        label = int(line[1])
        if label == 1:
            label = 5 
        allow_label = self.__allow_labels.get_label_index(label)
        if allow_label is not None:
            doc = Document()
            doc.id = int(line[0])
            doc.raw_title = line[2]
            doc.raw_body = line[-1]
            label = int(line[1])
            if label == 1:
                label = 5 
            doc.raw_label = label
            doc.allow_label = allow_label
            self.__corpus[doc.id] = doc
            print("INFO: READ doc: {}".format(doc.id))
        else:
            print("INFO: The doc: {} has a non allowed label {}".format(line[0], label))
    
    def load(self, path):
        """
        """
        with open(path, 'r', encoding=self.__encoding) as hand_file:
            hand_file.readline()
            own_split = str.split
            own_strip = str.strip
            for line in hand_file:
                line = own_split(own_strip(line), self.__SEP_CHAR)
                self.__add_document(line)
                hand_file.readline()
            
        
        
    def get_document(self, doc_id):
        """
        """
        return self.__corpus.get(doc_id, None)
        
    def get_size(self):
        """
        """
        return len(self.__corpus)
        
    def clean(self):
        """
        """
        self.__corpus.clear()
        