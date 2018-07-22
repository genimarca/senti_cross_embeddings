#!/usr/bin/python3
# *-* coding:utf-8 *-*
'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from sce.model.allow_labels_names import AllowLabelsNames

class FactoryAllowLabels:
    '''
    classdocs
    '''


    @classmethod
    def creator(cls, corpus_name_key):
        cl = None
        if corpus_name_key in AllowLabelsNames.__members__.keys():
            corpus_class_path = AllowLabelsNames.__members__[corpus_name_key].value
            corpus_class_fields = corpus_class_path.rsplit(".", 1)
            module = __import__(corpus_class_fields[0], corpus_class_fields[-1])
            cl = getattr(module, corpus_class_fields[-1])()
            
        return cl
        
        
        