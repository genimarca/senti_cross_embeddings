#!/usr/bin/python3
# *-* coding: utf-8 *-*

'''
Created on 20 jul. 2018

@author: Eugenio Martínez Cámara
'''

from enum import Enum, unique

@unique
class CorpusNames(Enum):
    '''
    classdocs
    '''


    GENERAL_TASS = "sce.model.dao.corpus_general_tass.CorpusGeneralTASS"
    
    INTERTASS = "sce.model.dao.corpus_intertass.CorpusInterTASS"
    
    SEMEVAL = "sce.model.dao.corpus_semeval_twitter.CorpusSemEvalTwitter"
    
    SENTIPOLC = "sce.model.dao.corpus_sentipolc.CorpusSentipolc"
    
    ALEC_GO_STANFORD = "sce.model.dao.corpus_alec_go_stanford.CorpusAlecGoStanford"
    
    COST = "sce.model.dao.corpus_cost.CorpusCOST"
    
    GERMAN_SB10K = "sce.model.dao.corpus_german_sb10k.CorpusGermanSB10"
    
    EN_PANG_LEE_MOVIES = "sce.model.dao.corpus_english_movies_pang_lee.CorpusEnglishMoviesPangLee"
    
    ES_MUCHOCINE_MOVIES = "sce.model.dao.corpus_muchocine.CorpusMuchoCine"
    
    
    