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
    def creator(cls, allow_labels_name_key):
        cl = None
        if allow_labels_name_key in AllowLabelsNames.__members__.keys():
            allow_labels_class_path = AllowLabelsNames.__members__[allow_labels_name_key].value
            allow_labels_class_fields = allow_labels_class_path.rsplit(".", 1)
            module = __import__(allow_labels_class_fields[0], fromlist=allow_labels_class_fields[-1])
            cl = getattr(module, allow_labels_class_fields[-1])()
            
        return cl
        
        
        