#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:20:05 2023

@author: samarth
"""

import pandas as pd

df = pd.read_excel("PackageWiseAdmission.xlsx")

df.columns
df.shape
df.isnull().sum()

df["Course Package"]