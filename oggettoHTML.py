#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:00:29 2019

@author: rosto
"""

class OggettoHTML():
    def __init__(self, nome_tag="div", ID="", classi=[]):
        self.proprieta=(
            {
            "nome_tag":nome_tag,
            "id":ID,
            "classi":classi
            }
            )
        
        self.struttura_tag='<{nome_tag} id="{id}" class="{classi}" >%s</{nome_tag}>'
        self.ogg_figli=[]#Devono ereditare da OggettoHTML
    
    def to_html(self):
        risposta=""
        ogg_conversione = self.proprieta.copy()
        ogg_conversione["classi"] = " ".join(self.proprieta["classi"])
        
        risposta= self.struttura_tag.format(**ogg_conversione)
        risposta= risposta.replace('class="" ',"")
        risposta= risposta.replace('id="" ',"")
        
        ris_figli = ""
        for figlio in self.ogg_figli:
            ris_figli += figlio.to_html()
        
        return risposta % (ris_figli,)
    
    def add_child(self, child_obj):
        self.ogg_figli.append(child_obj)
    
    def add_class(self, classe):
        self.proprieta["classi"].append(str(classe))