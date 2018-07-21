#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from sce.model.embeddings.abs_word_embeddings import ABSWordEmbeddings

class EmbeddingsCrossCollados(ABSWordEmbeddings):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Sole constructor
        '''
        self.__word_indexes = {}
        self.__word_embeddings = []
        self.__SEP_CHAR = " "
        
    
    @property
    def word_indexes(self):
        return self.__word_indexes
    
    @property
    def word_embeddings(self):
        return self.__word_embeddings
    
    
    def get_number_of_embeddings(self):
        return len(self.__word_embeddings)
    
    def is_word(self, word):
        return word in self.__word_indexes
    
    def get_vector_embedding(self, word):
        return self.__word_embeddings[self.__word_indexes[word]] if self.is_word(word) else None 
    
    def set_vector_embedding(self, word, index, vector_embedding):
        self.__word_embeddings[index] = vector_embedding
        self.__word_indexes[word] = index
    
    def get_vector_embedding_dimension(self):
        return len(self.word_embeddings[-1])
    
    def get_word_index(self, word):
        return self.__word_indexes.get(word, None)
    
    def load(self, path, encoding, ofset=None, max_words=None, vocabulary=None):
        
        if ofset is not None:
            for i in range(ofset):
                self.__word_embeddings.append([])
                
        if max_words is None and vocabulary is None:
            self.__load_full(path, encoding)
        elif max_words is not None and vocabulary is None:
            self.__load_max_words(path, encoding, max_words)
        elif max_words is None and vocabulary is not None:
            self.__load_vocabulary(path, encoding, vocabulary)
        elif max_words is not None and vocabulary is not None:
            self.__load_max_words_vocabulary(path, encoding, max_words, vocabulary)
            
            
    def __add_vector(self, line, vocabulary=None):
        
        fields = line.partition(self.__SEP_CHAR)
        word = fields[0].strip()
        if word in vocabulary:
            emb_values = [float(x) for x in fields[-1].split(self.__SEP_CHAR)]
            self.__word_indexes[word] = len(self.__word_embeddings)
            self.__word_embeddings.append(emb_values)
    
    def __load_full(self, path, encoding):
        with open(path, "r", encoding=encoding) as emb_file:
            for line in emb_file:
                self.__add_vector(line)
                
                
    def __load_vocabulary(self, path, encoding, vocabulary):
        with open(path, "r", encoding=encoding) as emb_file:
            for line in emb_file:
                self.__add_vector(line, vocabulary)
    
    def __load_max_words(self, path, encoding, max_words):
        own_strip = str.strip
        with open(path, "r", encoding=encoding) as emb_file:
            i = 0
            line = own_strip(emb_file.readline())
            while line and i<max_words:
                self.__add_vector(line)
                i+=1
                line = own_strip(emb_file.readline())
                
            
    def __load_max_words_vocabulary(self, path, encoding, max_words, vocabulary):
        own_strip = str.strip
        with open(path, "r", encoding=encoding) as emb_file:
            i = 0
            line = own_strip(emb_file.readline())
            while line and i<max_words:
                self.__add_vector(line, vocabulary)
                i+=1
                line = own_strip(emb_file.readline())
                
    