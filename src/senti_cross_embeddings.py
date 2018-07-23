#!/usr/bin/python3
'''
Created on 23 jul. 2018

@author: Eugenio Martínez Cámara
'''

from sce.model.model_pipeline import ModelPipeline
import sys

if __name__ == '__main__':
    
    if(len(sys.argv)!=2):
        print("ERROR: The input must be: python3 senti_cross_embeddings.py [CONF_PATH]")
    else:
        model = ModelPipeline()
        model.initialization(sys.argv[1])
        model.training()
        model.classification()
        model.results()
        print("\nGoodBye\n")