#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 21 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from enum import Enum, unique

class EmbeddingsNames(Enum):



    GLOVE = "sce.model.embeddings.embeddings_glove.EmbeddingsGlove"
    
    COLLADOS = "sce.model.embeddings.embeddings_collados.EmbeddingsCollados"
    
    SPANISH = "sce.model.embeddings.embeddings_spanish.EmbeddingsSpanish"