#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:04:45 2019

@author: rosto
"""

import oggettoHTML
class Row(oggettoHTML.OggettoHTML):
    def __init__(self,ID=""):
        super().__init__(nome_tag="div", ID=ID, classi=["row"])
if __name__=="__main__":
    r = Row()
    print(r.to_html())