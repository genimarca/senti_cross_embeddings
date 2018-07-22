#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 22 jul. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

import re

class PropertiesManager:
    '''
    classdocs
    '''

    properties = {}
    FIELDS_SEPARATOR = "="
    re_multi_value_properties = re.compile(",|;")
    
    @classmethod
    def load_properties(cls, properties_path):
        
        with(open(properties_path, encoding="utf-8")) as properties_file:
            own_split = str.split
            own_strip = str.strip
            for prop in properties_file:
                fields = own_split(prop, cls.FIELDS_SEPARATOR)
                #Multi-value property
                if(cls.re_multi_value_properties.search(fields[1]) != None):
                    cls.properties[own_strip(fields[0])] = [own_strip(value) for value in cls.re_multi_value_properties.split(fields[1])]
                elif(fields[1] == "YES"):
                    cls.properties[own_strip(fields[0])] = True
                elif(fields[1] == "NO"):
                    cls.properties[own_strip(fields[0])] = False
                else:
                    cls.properties[own_strip(fields[0])] = own_strip(fields[1])
                    if (len(cls.properties[own_strip(fields[0])]) == 0):
                        cls.properties[own_strip(fields[0])] = None
                        
                        
    @classmethod
    def get_prop_value(cls, prop_name):
        return(cls.properties.get(prop_name, None))