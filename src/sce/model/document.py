'''
Created on 13 jul. 2018

@author: geniugr
'''

class Document:
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.id = ""
        self.__raw_text = ""
        self.__process_text = []
        self.__raw_label = ""
        self.__sparse_label = ""
        self.__prob_label = []
        
        
    @property
    def id(self):
        return self.id
    
    @id.value
    def id(self, a_id):
        self.id = a_id
    
    @property
    def raw_text(self):
        return self.__raw_text
    
    @raw_text.setter
    def raw_text(self, a_raw_text):
        self.__raw_text = a_raw_text
    
    @property
    def process_text(self):
        return self.__process_text
    
    @process_text.setter
    def process_text(self, a_process_text):
        self.__process_text = a_process_text
    
    @property
    def raw_label(self):
        return self.__raw_label
    
    @raw_label.setter
    def raw_label(self, a_raw_label):
        self.__raw_label = a_raw_label
        
    @property
    def sparse_label(self):
        return self.__sparse_label
    
    @sparse_label.setter
    def sparse_label(self, a_sparse_label):
        self.__sparse_label = a_sparse_label
        
    @property
    def prob_label(self):
        return self.__prob_label
    
    @prob_label.setter
    def prob_label(self, a_prob_label):
        self.__prob_label = a_prob_label
        