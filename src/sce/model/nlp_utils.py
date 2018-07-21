#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from nltk.tokenize.casual import casual_tokenize

class NLPUtils:
    '''
    classdocs
    '''

    @staticmethod
    def tokenize_tweet(text, a_preserve_case=True, a_reduce_len=False, a_strip_handles=False):
        
        return casual_tokenize(text, preserve_case=a_preserve_case, reduce_len=a_reduce_len, strip_handles=False)