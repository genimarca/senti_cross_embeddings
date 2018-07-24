#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''
from sce.model.dao.abs_corpus import ABSCorpus
from sce.model.document import Document
from sce.model.abs_allow_labels import ABSAllowLabel
from sce.model.bilabel_experiments import BilabelExperiments
from sce.model.trilabel_experiments import TrilabelExperiments

from collections import OrderedDict
import numpy as np

class CorpusSemEvalTwitter(ABSCorpus):
    '''
    classdocs
    '''


    def __init__(self, allow_labels=None):
        '''
        Sole constructor
        '''
        self.__corpus = OrderedDict()
        self.__encoding = ""
        self.__doc_ids = []
        self.__SEP_CHAR = "\t"
        self.__allow_labels = allow_labels
        self.__doc_x_labels = None
        
        
        
    @property
    def allow_labels(self):
        return self.__allow_labels
    
    @allow_labels.setter
    def allow_labels(self, a_allow_labels):
        self.__allow_labels = a_allow_labels
        self.__doc_x_labels = {i:0 for i in self.__allow_labels.label_index()}
    
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
    def doc_ids(self):
        """
        """
        return self.__doc_ids
        
    @property
    def doc_x_labels(self):
        """
        """
        return self.__doc_x_labels
    
    def __add_document(self, raw_tweet):
        own_strip = str.strip
        label_index = self.__allow_labels.get_label_index(raw_tweet[1])
        if label_index is not None:
            tweet = Document()
            tweet.id = own_strip(raw_tweet[0])
            tweet.raw_text = own_strip(raw_tweet[-1])
            tweet.raw_label = self.__allow_labels.get_label_name(label_index)
            tweet.sparse_label = label_index
            if own_strip(raw_tweet[0]) in self.__corpus:
                raw_tweet[0] = own_strip(raw_tweet[0]) + "_2"
            elif own_strip(raw_tweet[0]) + "_2" in self.__corpus:
                raw_tweet[0] = own_strip(raw_tweet[0]) + "_3"
            self.__doc_x_labels[label_index] += 1
            self.__corpus[raw_tweet[0]] = tweet
            self.__doc_ids.append(own_strip(raw_tweet[0]))
    
    
    def load(self, path):
        """
        """
        own_split = str.split
        own_strip = str.strip
        with open(path, encoding=self.__encoding) as corpus_file:
            for line in corpus_file:
                fields = own_split(own_strip(line), self.__SEP_CHAR)
                self.__add_document(fields)
                
        
    def get_document(self, a_id):
        """
        """
        return self.__corpus.get(a_id, None)
        
    def get_size(self):
        """
        """
        return len(list(self.__corpus.keys()))
        
        
    def clean(self):
        """
        """
        self.__corpus.clear()
        
        
        