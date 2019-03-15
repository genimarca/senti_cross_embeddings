#!/usr/bin/python3
# *-* coding:utf-8 *-*
'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from sce.model.nlp_utils_names import NLPUtilsNames

class FactoryNLPUtils:
    '''
    classdocs
    '''


    @classmethod
    def creator(cls, nlp_utils_name_key):
        cl = None
        if nlp_utils_name_key in NLPUtilsNames.__members__.keys():
            nlp_utils_class_path = NLPUtilsNames.__members__[nlp_utils_name_key].value
            nlp_utils_class_fields = nlp_utils_class_path.rsplit(".", 1)
            module = __import__(nlp_utils_class_fields[0], fromlist=nlp_utils_class_fields[-1])
            cl = getattr(module, nlp_utils_class_fields[-1])()
            
        return cl
        
        
        