# -*- coding: utf-8 -*-
"""
Created on Thu May 26 07:59:15 2022

@author: rwmacharia1
"""

class Person:
    
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
        
    def get_firstname(self):
        return self._firstname
    
    def get_lastname(self):
        return self._lasstname
    
    def get_ID(self):
        return self._ID
    
    """ Create a string representation of the object"""
    