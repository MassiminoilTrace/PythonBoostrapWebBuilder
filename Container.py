#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:06:04 2019

@author: rosto
"""

import oggettoHTML

class Container(oggettoHTML.OggettoHTML):
    def __init__(self, fluid=False, ID=""):
        if fluid:
            super().__init__(classi=["container-fluid"])
        else:
            super().__init__(classi=["container"])