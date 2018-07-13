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

class CorpusGeneralTASS(ABSCorpus):
    '''
    General TASS corpus class
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.__corpus = {}
        self.__encoding = ""
        self.__doc_ids = []
        self.__labels = []
        self.__doc_x_labels = {}
        
        
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
    def labels(self):
        """
        """
        return self.__labels
        
    @property
    def doc_x_labels(self):
        """
        """
        return self.__doc_x_labels
    
    def __add_document(self, raw_tweet):
        
        tweet = Document()
        tweet.id = raw_tweet["id"]
        tweet.raw_text = raw_tweet["content"]
        tweet.raw_label = raw_tweet["label"]
        
        if raw_tweet["label"] not in self.labels:
            self.labels.append(raw_tweet["label"])
        tweet.sparse_label = self.labelsindex(raw_tweet["label"])
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
        