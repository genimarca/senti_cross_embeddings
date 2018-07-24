#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 13 jul. 2018

@author: Eugenio Martínez Cámara
'''

from sce.model.dao.abs_corpus import ABSCorpus
from sce.model.dao.corpus_general_tass_xml_parser import CorpusGeneralTASSXML
from xml.etree.ElementTree import XMLParser
from sce.model.document import Document
from sce.model.abs_allow_labels import ABSAllowLabel
from sce.model.bilabel_experiments import BilabelExperiments
from sce.model.trilabel_experiments import TrilabelExperiments

from collections import OrderedDict

class CorpusGeneralTASS(ABSCorpus):
    '''
    General TASS corpus class
    '''


    def __init__(self, allow_labels=None):
        '''
        Constructor
        '''
        self.__corpus = OrderedDict()
        self.__encoding = ""
        self.__doc_ids = []
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
        
        label_index = self.__allow_labels.get_label_index(raw_tweet["label"])
        if label_index is not None:
            tweet = Document()
            tweet.id = raw_tweet["id"]
            tweet.raw_text = raw_tweet["content"]
            tweet.raw_label = self.__allow_labels.get_label_name(label_index)
            tweet.sparse_label = label_index
            self.__doc_x_labels[label_index]+=1
            self.__corpus[raw_tweet["id"]] = tweet
    
    def load(self, path):
        """
        """
        own_xml_parser = CorpusGeneralTASSXML()
        xml_parser = XMLParser(target=own_xml_parser) 
        with open(path, encoding=self.__encoding) as corpus_file:
            for line in corpus_file:
                xml_parser.feed(line)
                if own_xml_parser.full_doc:
                    raw_tweet = own_xml_parser.doc
                    self.__add_document(raw_tweet)
                    
                
        
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
        