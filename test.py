#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:08:32 2019

@author: rosto
"""

import Row
import Container

r = Row.Row()
r2 = Row.Row()
c = Container.Container()
c.add_child(r)
c.add_child(r2)

print(c.to_html())