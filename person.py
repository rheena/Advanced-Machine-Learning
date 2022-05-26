# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:30:23 2022

@author: m
"""

class Person (object):
    
    count = 0
    
    def __init__(self, firstname, lastname, ID=123456):
        self._firstname = firstname
        self._lastname = lastname
        self._ID = ID
        self.__class__.count += 1
        
    def get_count(self):
        return self.__class__.count
    
    def get_name(self):
        return self._firstname + " " + self._lastname
    
    def set_firstname(self, firstname):
        self._firstname = firstname
        
    def set_lastname(self, lastname):
         self._lastname = lastname   
         
    def set_ID(self, ID):
        self._ID = ID
        
    """Create a string representation of the object"""
    def __str__(self):
        return self._firstname + " " + \
            self._lastname + " " + \
                str(self._ID)
    
    