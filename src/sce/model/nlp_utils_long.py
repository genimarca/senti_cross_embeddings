#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""



from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

import re
import nltk.data as nltk_data

from sce.model.abs_nlp_utils import ABSNLPUtils

class NLPUtilsLong(ABSNLPUtils):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.__language = None
        self.__token_whitespace = False

    
    @property
    def language(self):
        """
        """
        return self.__language    
        
    @language.setter
    def language(self, a_language):
        """
        """
        self.__language = a_language
    
    @property
    def token_whitespace(self):
        """
        """
        return self.__token_whitespace
    
    @token_whitespace.setter
    def token_whitespace(self, a_token_whitespace):
        """
        """
        
        self.__token_whitespace = a_token_whitespace

    def tokenize(self, text, a_preserve_case=True, a_reduce_len=False, a_strip_handles=False):
        
        own_tokenizer = None
        tokens = []
        own_extend = tokens.extend
        
        if self.__token_whitespace:
            tokens = text.split(" ")
        
        elif self.__language == "persian":
            own_tokenizer = ToktokTokenizer()
            for t in text:
                own_extend(own_tokenizer.tokenize(t))
        else:
            own_tokenizer = nltk_data.load("tokenizers/punkt/"+self.__language+".pickle")
            sents = own_tokenizer.tokenize(text)
            for sent in sents:
                own_extend(word_tokenize(sent, language=self.__language))
        
        return tokens
    
    def normalization_lowercase(self, text):
        return text.lower()
    
    def stopper(self, tokens, language):
        lang_stopwords = stopwords.words(language)
        return [t for t in tokens if t not in lang_stopwords]
    
    def stemmer(self, tokens, language):
        stemmer = SnowballStemmer(language)
        return [stemmer.stem(t) for t in tokens]