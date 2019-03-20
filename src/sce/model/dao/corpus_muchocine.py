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
    
    
    def __init__(self, allow_labels=BilabelExperiments()):
        '''
        Constructor
        '''
        self.__allow_labels=None
        self.__encoding = "utf-8"
        self.__corpus=OrderedDict()
        self.__allow_labels = allow_labels
        self.__doc_x_labels = {i:0 for i in self.__allow_labels.label_index()}
        self.__SEP_CHAR = "\";\""
        self.__is_tokenized = False
        self.__is_lowercase = False
        
        
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
        
    
    
    
    
    def __add_document(self, id_doc, label_index, raw_text):
        """
        """
        
        doc = Document()
        doc.id = id_doc
        doc.raw_text = raw_text
        doc.sparse_label = int(label_index)
        print(id_doc)
        print(label_index)
        doc.raw_label = self.__allow_labels.get_label_name(doc.sparse_label)
        self.__doc_x_labels[doc.sparse_label] += 1
        self.__corpus[doc.id] = doc
        
        
        
    
    def load(self, path):
        """
        """
        with open(path, 'r', encoding=self.__encoding) as hand_file:
            hand_file.readline()
            own_split = str.split
            own_strip = str.strip
            for line in hand_file:
                fields = own_split(own_strip(line), self.__SEP_CHAR)
                self.__add_document(fields[0], fields[1], fields[2])
                
            
        
        
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
        