#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from sce.model.abs_allow_labels import ABSAllowLabel

import sklearn.metrics as sk_metrics

class ResultsMetrics:
    '''
    classdocs
    '''


    @staticmethod
    def confusion_matrix(real_labels, pred_labels):
        return sk_metrics.confusion_matrix(real_labels, pred_labels)
    
    
    @staticmethod
    def precision_x_class(real_labels, pred_labels, allow_labels):
        return {al: sk_metrics.precision_score(real_labels, pred_labels, labels=[al], average=None)[0] for al in allow_labels.label_index()}
    
    @staticmethod
    def macro_precision(real_labels, pred_labels):
        return sk_metrics.precision_score(real_labels, pred_labels, average="macro")
    
    @staticmethod
    def recall_x_class(real_labels, pred_labels, allow_labels):
        return {al: sk_metrics.recall_score(real_labels, pred_labels, labels=[al], average=None)[0] for al in allow_labels.label_index()}
    
    @staticmethod
    def macro_recall(real_labels, pred_labels):
        return sk_metrics.recall_score(real_labels, pred_labels, average="macro")
    
    @staticmethod
    def f1_x_class(real_labels, pred_labels, allow_labels):
        return {al: sk_metrics.f1_score(real_labels, pred_labels, labels=[al], average=None)[0] for al in allow_labels.label_index()}
    
    @staticmethod
    def macro_f1(real_labels, pred_labels):
        return sk_metrics.f1_score(real_labels, pred_labels, average="macro")
    
    @staticmethod
    def accuracy(real_labels, pred_labels):
        return sk_metrics.accuracy_score(real_labels, pred_labels)