#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

import re
from nltk.tokenize.casual import casual_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
class NLPUtils:
    '''
    classdocs
    '''

    @staticmethod
    def tokenize_tweet(text, a_preserve_case=True, a_reduce_len=False, a_strip_handles=False):
        
        return casual_tokenize(text, preserve_case=a_preserve_case, reduce_len=a_reduce_len, strip_handles=a_strip_handles)
    
    
    @staticmethod
    def normalization_users(text, str_replace):
        #(?<! --> Negative negative look-behind. To prevent before @ a character distinct of white space
        pattern = re.compile(r"(?<![A-Za-z0-9_!@#\$%&*])@(([A-Za-z0-9_]){20}(?!@))|(?<![A-Za-z0-9_!@#\$%&*])@(([A-Za-z0-9_]){1,19})(?![A-Za-z0-9_]*@)")
        return pattern.sub(str_replace, text)
    
    
    @staticmethod
    def normalization_lowercas(text):
        return text.lower()
    
    @staticmethod
    def stopper(tokens, language):
        lang_stopwords = stopwords.words(language)
        return [t for t in tokens if t not in lang_stopwords]
    
    @staticmethod
    def stemmer(tokens, language):
        stemmer = SnowballStemmer(language)
        return [stemmer.stem(t) for t in tokens]