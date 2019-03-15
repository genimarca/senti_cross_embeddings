'''
Created on 15 mar. 2019

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''

from collections import OrderedDict
import os

from sce.model.dao.abs_corpus import ABSCorpus
from sce.model.bilabel_experiments import BilabelExperiments
from sce.model.document import Document

class CorpusEnglishMoviesPangLee(ABSCorpus):
    '''
    classdocs
    '''


    def __init__(self, allow_labels=BilabelExperiments()):
        '''
        Sole constructor
        '''
        self.__corpus = OrderedDict()
        self.__encoding = ""
        self.__doc_ids = []
        self.__SEP_CHAR = ";;;"
        self.__allow_labels = allow_labels
        self.__doc_x_labels = {i:0 for i in self.__allow_labels.label_index()}
        self.__is_tokenized = True
        self.__is_lowercase = True
        
        
        
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
    def doc_ids(self):
        """
        """
        return self.__doc_ids
        
    @property
    def doc_x_labels(self):
        """
        """
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
    
    def __add_document(self, id_doc, label, raw_text):
        
        doc = Document()
        doc.id = id_doc
        doc.raw_text = raw_text
        doc.sparse_label = self.__allow_labels.get_label_index(label)
        doc.raw_label = self.__allow_labels.get_label_name(doc.sparse_label)
        self.__doc_x_labels[doc.sparse_label] += 1
        self.__corpus[doc.id] = doc
        
    
    def load(self, path):
        """
        
        """
        with open(path, encoding=self.__encoding) as file_handler:
            own_split = str.split
            own_strip = str.strip
            for line in file_handler:
                fields = own_split(own_strip(line),self.__SEP_CHAR)
                raw_text = fields[-1]+"\n"
                line_doc = file_handler.readline()
                while(line_doc != "" and line_doc != "++--------\n"):
                    raw_text = "".join([raw_text, line_doc])
                    line_doc = file_handler.readline()
                self.__add_document(fields[0], fields[1], raw_text)
                
        
        
        
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
        