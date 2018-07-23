#!/usr/bin/python3
# *-* coding:utf-8 *-*
'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from sce.model.embeddings.embeddings_names import EmbeddingsNames

class FactoryEmbeddings:
    '''
    classdocs
    '''


    @classmethod
    def creator(cls, embeddings_name_key):
        cl = None
        if embeddings_name_key in EmbeddingsNames.__members__.keys():
            embeddings_class_path = EmbeddingsNames.__members__[embeddings_name_key].value
            embeddings_class_fields = embeddings_class_path.rsplit(".", 1)
            module = __import__(embeddings_class_fields[0], fromlist=embeddings_class_fields[-1])
            cl = getattr(module, embeddings_class_fields[-1])()
            
        return cl
        
        
        