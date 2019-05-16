#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:54:45 2018

@author: muveexu
"""
#%%
import pandas as pd

file = r'Energy+Indicators.xls'
df = pd.read_excel(file)
print(df)