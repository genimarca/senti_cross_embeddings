#!/usr/bin/python3
# *-* coding: utf-8 *-*
'''
Created on 13 jul. 2018

@author: Eugenio Martínez Cámara
'''
import sys
class CorpusGeneralTASSXML:
    '''
    '''


    def __init__(self):
        '''
        sole constructor
        '''
        self.__target_tags = {"tweetid":"__get_tweetid", "content":"__get_content", "value":"__get_polarity"}
        self.__tag = None
        self.__tag_end = None
        self.__doc = {"id":"", "content":"", "label":""}
        self.__full_doc = False
    
    
    @property
    def doc(self):
        return self.__doc
    
    @property
    def full_doc(self):
        return(self.__full_doc)
    
    def start(self, tag, attrib):
        """
        """
        if tag == "tweet":
            self.__full_doc = False
            self.__doc = {"id":"", "content":"", "label":""}
        
        if tag in self.__target_tags:
            self.__tag = tag
        
        
    def end(self, tag):
        self.__tag_end = tag
        if self.__tag is not None and tag in self.__target_tags:
            self.__tag = None
        elif tag == "tweet":
            self.__full_doc = True
            
        
    
    def __get_tweetid(self, data):
        
        self.__doc["id"] = data
        
    def __get_content(self, data):
        
        self.__doc["content"] = data
        
    def __get_polarity(self, data):
        
        if self.__tag == "value" and self.__tag_end != "entity":
            self.__doc["label"] = data
            
        
        
    
    def data(self, data):
        if self.__tag is not None:
            method_to_call = getattr(self,"_"+__class__.__name__+self.__target_tags[self.__tag], None)
            if method_to_call is not None:
                method_to_call(data)
            
        return data
        
    def close(self):
        return
    
