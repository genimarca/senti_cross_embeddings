'''
Created on 15 mar. 2019

@author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
'''


from abc import ABCMeta, abstractmethod

class ABSNLPUtils(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self):
        '''
        Sole constructor
        '''
        
    @property
    @abstractmethod
    def language(self):
        """
        """    
        
    @language.setter
    @abstractmethod
    def language(self, a_language):
        """
        """
    @property
    @abstractmethod
    def token_whitespace(self):
        """
        """
    
    @token_whitespace.setter
    @abstractmethod
    def token_whitespace(self, a_token_whitespace):
        """
        """
    
    
    
    @abstractmethod
    def tokenize(self, text, a_preserve_case=True, a_reduce_len=False, a_strip_handles=False):
        """
        """
        
    @abstractmethod
    def normalization_lowercase(self, text):
        """
        """
        
    @abstractmethod
    def stopper(self, tokens, language):
        """
        """
    
    @abstractmethod
    def stemmer(self, tokens, language):
        """
        """
