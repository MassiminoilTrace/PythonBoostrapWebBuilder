#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:32:45 2019

@author: rosto
"""

class Builder():
    def __init__(self,obj_html_root):
        self.ogg_html_radice = obj_html_root
        self.SCHELETRO = (
                """

                """
                
                )
    
    def __str__(self):
        return self.ogg_html_radice.to_html()