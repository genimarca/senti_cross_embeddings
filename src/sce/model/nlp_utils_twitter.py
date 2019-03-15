#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from nltk.tokenize.casual import casual_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

import re

from sce.model.abs_nlp_utils import ABSNLPUtils

class NLPUtilsTwitter(ABSNLPUtils):
    '''
    classdocs
    '''

    def __init__(self):
        self.__language = None
        self.__token_whitespace = None

    
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
        
        return casual_tokenize(text, preserve_case=a_preserve_case, reduce_len=a_reduce_len, strip_handles=a_strip_handles)
    
    def normalization_lowercase(self, text):
        return text.lower()
    
    def stopper(self, tokens, language):
        lang_stopwords = stopwords.words(language)
        return [t for t in tokens if t not in lang_stopwords]
    
    def stemmer(self, tokens, language):
        stemmer = SnowballStemmer(language)
        return [stemmer.stem(t) for t in tokens]
    
    def normalization_users(self, text, str_replace):
        #(?<! --> Negative negative look-behind. To prevent before @ a character distinct of white space
        pattern = re.compile(r"(?<![A-Za-z0-9_!@#\$%&*])@(([A-Za-z0-9_]){20}(?!@))|(?<![A-Za-z0-9_!@#\$%&*])@(([A-Za-z0-9_]){1,19})(?![A-Za-z0-9_]*@)")
        return pattern.sub(str_replace, text)