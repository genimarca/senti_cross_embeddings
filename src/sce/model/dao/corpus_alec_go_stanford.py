#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''
from sce.model.dao.abs_corpus import ABSCorpus
from sce.model.document import Document
from sce.model.bilabel_experiments import BilabelExperiments
from sce.model.trilabel_experiments import TrilabelExperiments

class CorpusAlecGoStanford(ABSCorpus):
    '''
    classdocs
    '''


    def __init__(self, allow_labels=BilabelExperiments()):
        '''
        Sole constructor
        '''
        self.__corpus = {}
        self.__encoding = ""
        self.__SEP_CHAR = ","
        self.__allow_labels = allow_labels
        self.__doc_x_labels = {i:0 for i in self.__allow_labels.label_index()}
        
        
    @property
    def allow_labels(self):
        return self.__allow_labels
    
    @allow_labels.setter
    def allow_labels(self, a_allow_labels):
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
        
        raw_label = ""
        if raw_tweet[1] == "0":
            raw_label = "negative"
        elif raw_tweet[1] == "2":
            raw_label = "neutral"
        elif raw_tweet[1] == "4":
            raw_label = "postive"
            
        label_index = self.__allow_labels.get_label_index(raw_label)
        if label_index is not None:
            tweet = Document()
            tweet.id = raw_tweet[1][1:-1]
            tweet.raw_text = raw_tweet[-1][1:-1]
            tweet.raw_label = self.__allow_labels.get_label_name(label_index)
            tweet.sparse_label = label_index
            self.__doc_x_labels[label_index]+=1
            self.__corpus[tweet.id] = tweet
        
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
        return len(self.__corpus)
        
        
    def clean(self):
        """
        """
        self.__corpus.clear()
        