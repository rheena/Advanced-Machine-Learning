# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:30:18 2022

@author: m
"""

from person import Person

class Student(Person):
    
    def __init__(self, first, last, ID, school, major):
        super().__init__(first, last, ID)
        self._school = school
        self._major = major
        
    def get_school(self):
        return self._school
    
    def get_major(self):
        return self._major
    
    def get_name(self):
        return super().get_lastname() + "," + \
            super().get_firstname()
            
    def __str__(self):
        return super().__str__() + "\n" + \
            self._school + "\n" + self._major