#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:50:49 2019

@author: mariofire
"""
##############################################################################
# This script takes the input for a MOS station in the United States and grabs
# the data and puts it into a pandas dataframe.
#
# import NAMMOS or GFSMOS
#
# function call:
# df = NAMMOS(stationcode) ex: 'KLWM', 'KBOX' 
#
#
# This only is for the short term MOS. The values for Q06, P06, P12, Q12, X/N
# are not properly spaced out to match with their appropriate times at this 
# point so adjustments need to be made when using said data. This will be added
# in a future update
##############################################################################

import requests
import pandas as pd
import numpy as np
import re




def NAMMOS(station):
    #Open the data file
    response = requests.get('https://www.nws.noaa.gov/mdl/forecast/text/nammet.txt')
    #Put data into list
    data = response.text
    data = data.split("/n")
    
    #Remove all white spaces and replace with commas then split by comma
    x = re.sub("\s+", ",", data[0]).split(',')
    
    #Get the index of the place that we want
    string = station
    ind = x.index(string)
    
    #Make new list starting from our list
    newstring = x[ind:]
    
    #Get index of 'OBV' string and add 21 to get to last value
    ind2 = newstring.index('OBV')
    ind2 = ind2 + 22
    
    #Put data into new list
    datalist = newstring[0:ind2]
    
    #Get index of each of the main values to make dictionary
    indhr = datalist.index('HR')
    try:
        indxn = datalist.index('X/N')
    except:
        indxn = datalist.index('N/X')
    indtmp = datalist.index('TMP')
    inddpt = datalist.index('DPT')
    indcld = datalist.index('CLD')
    indwdr = datalist.index('WDR')
    indwsp = datalist.index('WSP')
    indp06 = datalist.index('P06')
    indp12 = datalist.index('P12')
    indq06 = datalist.index('Q06')
    indq12 = datalist.index('Q12')
    indt06 = datalist.index('T06')
    indt12 = datalist.index('T12')
    indcig = datalist.index('CIG')
    indvis = datalist.index('VIS')
    indobv = datalist.index('OBV')
    inddt = datalist.index('DT')
    
    #Get the first hour and then put the dates for each hour in. We will be putting any dates beyond day 3 under the header for day 3
    hour = int(datalist[indhr+1])
    if(hour == 18):
        days = [datalist[inddt+2],datalist[inddt+2], datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4], datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6]]
    elif(hour == 12):
        days = [datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+4]+datalist[inddt+5],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1]]
    elif(hour == 6):
        days = [datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1]]
    else:
        days = [datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+4]+datalist[inddt+5],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1]]
     
    #Put everything into a dictionary
    dictionary = {
            'HR': datalist[indhr+1:indxn],
            'X/N': datalist[indxn+1:indtmp],
            'TMP': datalist[indtmp+1:inddpt],
            'DPT': datalist[inddpt+1:indcld],
            'CLD': datalist[indcld+1:indwdr],
            'WDR': datalist[indwdr+1:indwsp],
            'WSP': datalist[indwsp+1:indp06],
            'P06': datalist[indp06+1:indp12],
            'P12': datalist[indp12+1:indq06],
            'Q06': datalist[indq06+1:indq12],
            'Q12': datalist[indq12+1:indt06],
            'T06': datalist[indt06+1:indt12],
            'T12': datalist[indt12+1:indcig],
            'CIG': datalist[indcig+1:indvis],
            'VIS': datalist[indvis+1:indobv],
            'OBV': datalist[indobv+1:],
            }
    
    #Make a pandas dataframe from the dictionary and append the 
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    df.columns = days
    
    #Swap the order of the rows to better match MOS output
    df = df.reindex(['HR','X/N','TMP','DPT','CLD','WDR','WSP','P06','P12','Q06','Q12','CIG','VIS','OBV'])
    return df

def GFSMOS(station):
    #Open the data file
    response = requests.get('https://www.nws.noaa.gov/mdl/forecast/text/avnmav.txt')
    
    #Put data into list
    data = response.text
    data = data.split("/n")
    
    #Remove all white spaces and replace with commas then split by comma
    x = re.sub("\s+", ",", data[0]).split(',')
    
    #Get the index of the place that we want
    string = station
    ind = x.index(string)
    
    #Make new list starting from our list
    newstring = x[ind:]
    
    #Get index of 'OBV' string and add 21 to get to last value
    ind2 = newstring.index('OBV')
    ind2 = ind2 + 22
    
    #Put data into new list
    datalist = newstring[0:ind2]
    
    #Get index of each of the main values to make dictionary
    indhr = datalist.index('HR')
    try:
        indxn = datalist.index('X/N')
    except:
        indxn = datalist.index('N/X')
    indtmp = datalist.index('TMP')
    inddpt = datalist.index('DPT')
    indcld = datalist.index('CLD')
    indwdr = datalist.index('WDR')
    indwsp = datalist.index('WSP')
    indp06 = datalist.index('P06')
    indp12 = datalist.index('P12')
    indq06 = datalist.index('Q06')
    indq12 = datalist.index('Q12')
    indt06 = datalist.index('T06')
    indt12 = datalist.index('T12')
    indcig = datalist.index('CIG')
    indvis = datalist.index('VIS')
    indobv = datalist.index('OBV')
    inddt = datalist.index('DT')
    
    #Get the first hour and then put the dates for each hour in. We will be putting any dates beyond day 3 under the header for day 3
    hour = int(datalist[indhr+1])
    if(hour == 18):
        days = [datalist[inddt+2],datalist[inddt+2], datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4],datalist[inddt+3]+datalist[inddt+4], datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6],datalist[inddt+5]+datalist[inddt+6]]
    elif(hour == 12):
        days = [datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+4]+datalist[inddt+5],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1]]
    elif(hour == 6):
        days = [datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1]]
    else:
        days = [datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+2] + datalist[inddt+3],datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5], datalist[inddt+4]+datalist[inddt+5],datalist[inddt+4]+datalist[inddt+5],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1],datalist[inddt+6]+datalist[inddt+1]]
     
    #Put everything into a     return dfdictionary
    dictionary = {
            'HR': datalist[indhr+1:indxn],
            'X/N': datalist[indxn+1:indtmp],
            'TMP': datalist[indtmp+1:inddpt],
            'DPT': datalist[inddpt+1:indcld],
            'CLD': datalist[indcld+1:indwdr],
            'WDR': datalist[indwdr+1:indwsp],
            'WSP': datalist[indwsp+1:indp06],
            'P06': datalist[indp06+1:indp12],
            'P12': datalist[indp12+1:indq06],
            'Q06': datalist[indq06+1:indq12],
            'Q12': datalist[indq12+1:indt06],
            'T06': datalist[indt06+1:indt12],
            'T12': datalist[indt12+1:indcig],
            'CIG': datalist[indcig+1:indvis],
            'VIS': datalist[indvis+1:indobv],
            'OBV': datalist[indobv+1:],
            }
    
    #Make a pandas dataframe from the dictionary and append the 
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    df.columns = days
    
    #Swap the order of the rows to better match MOS output
    df = df.reindex(['HR','X/N','TMP','DPT','CLD','WDR','WSP','P06','P12','Q06','Q12','CIG','VIS','OBV'])
    return df