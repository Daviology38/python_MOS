#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:41:00 2019

@author: mariofire
"""

from getmos import NAMMOS, GFSMOS
import pandas as pd
import matplotlib.pyplot as plt

df = GFSMOS('KBOS')
df = df.T
df = df.reset_index()
df['HR'] = pd.to_numeric(df['HR']) -4

df.TMP = pd.to_numeric(df.TMP)

i = 0 
index = len(df.HR)
while i < index:
    if(df.HR[i] < 0 and df.HR[i] != -4):
        df.HR[i] = str(df.HR[i] + 12) + ' AM'
    elif(df.HR[i] > 12):
        df.HR[i] = str(df.HR[i] - 12) + ' PM'
    elif(df.HR[i]  < 0 and df.HR[i] == -4):
        df.HR[i] = str(df.HR[i] + 12) + ' PM'
    else:
        df.HR[i] = str(df.HR[i]) + ' AM'
    i = i + 1
df['dateandtime'] = df['index'].map(str) + ' '+  df['HR'].map(str)
#df.HR = pd.to_numeric(df.HR)
ax = df.plot(x='dateandtime',y='TMP',legend=False,grid=True)
ax.set_xticks(range(len(df.HR)));
ax.set_xticklabels(["%s" % item for item in df.dateandtime.tolist()], rotation=90);
ax.set_title('3 Day Temperature Outlook')
plt.savefig('temp.png', bbox_inches='tight')
