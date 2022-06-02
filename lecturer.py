# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:37:25 2022

@author: m
"""

from person import Person

class Lecturer(Person):
    def __init__(self, first, last, course1, course2, course3):
        super().__init__(first, last)
        self._course1 = course1

        
    def get_course1(self):
        return self._course1
    
    def get_course2(self):
        return self._course2
    
    def get_course3(self):
        return self._course3
    
    
    def get_name(self):
        return super().get_lastname() + ", " + \
            super().get_firstname()
            
    # def get_course(self):
    #     return super().get_course1() + ", " + \
    #         super().get_course2() + ", " + \
    #           super().get_course3()  
    
    def set_firstname(self, firstname):
        self._firstname = firstname
        
    def set_lastname(self, lastname):
         self._lastname = lastname   
         
    def set_ID(self, ID):
        self._ID = ID
            
            