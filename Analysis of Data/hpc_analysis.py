#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:40:53 2017

@author: parth
"""
import csv
import sys
# For doing cool regular expressions
import re
import time
import matplotlib
import matplotlib.pyplot as plt

# For sorting dictionaries
import operator
import pandas as pd
import numpy as np
from textblob import TextBlob
test1_df=pd.read_csv('iphone7.csv',encoding = "ISO-8859-1")
test2_df=pd.read_csv('iphone7_3.csv',encoding = "ISO-8859-1")
test3_df=pd.read_csv('iphone7_4.csv',encoding = "ISO-8859-1")
test4_df=pd.read_csv('iphone7_5.csv',encoding = "ISO-8859-1")
test5_df=pd.read_csv('iphone7_6.csv',encoding = "ISO-8859-1")
test6_df=pd.read_csv('iphone7_7.csv',encoding = "ISO-8859-1")
test7_df=pd.read_csv('iphone7_8.csv',encoding = "ISO-8859-1")
test8_df=pd.read_csv('iphone7_9.csv',encoding = "ISO-8859-1")
test9_df=pd.read_csv('iphone7_10.csv',encoding = "ISO-8859-1")
combine1=[test1_df,test2_df,test3_df,test4_df,test5_df,test6_df,test7_df,test8_df,test9_df]
combine1=pd.concat(combine1)
#print(combine1)
test01_df=pd.read_csv('oneplus3T_1.csv',encoding = "ISO-8859-1")
test02_df=pd.read_csv('oneplus3T_2.csv',encoding = "ISO-8859-1")
test03_df=pd.read_csv('oneplus3T_3.csv',encoding = "ISO-8859-1")
test04_df=pd.read_csv('oneplus3T_4.csv',encoding = "ISO-8859-1")
test05_df=pd.read_csv('oneplus3T_5.csv',encoding = "ISO-8859-1")
test06_df=pd.read_csv('oneplus3T_6.csv',encoding = "ISO-8859-1")
test07_df=pd.read_csv('oneplus3T_7.csv',encoding = "ISO-8859-1")
test08_df=pd.read_csv('oneplus3T_8.csv',encoding = "ISO-8859-1")
test09_df=pd.read_csv('oneplus3T_9.csv',encoding = "ISO-8859-1")
test010_df=pd.read_csv('oneplus3T_10.csv',encoding = "ISO-8859-1")
combine2=[test01_df,test02_df,test03_df,test04_df,test05_df,test06_df,test07_df,test08_df,test09_df,test010_df]
combine2=pd.concat(combine2)
#print(combine2) 
use1=combine1["month"]
combine1=combine1["text"]
use2=combine2["month"]
combine2=combine2["text"]
#print(combine2)
##print(test_df)
polarity=[]
def tweets():
    for row in combine1:

            tweet=row
        
        

#        # Fix classic tweet lingo
            tweet = re.sub(r'\bthats\b', 'that is', tweet)
            tweet = re.sub(r'\bive\b', 'i have', tweet)
            tweet = re.sub(r'\bim\b', 'i am', tweet)
            tweet = re.sub(r'\bya\b', 'yeah', tweet)
            tweet = re.sub(r'\bcant\b', 'can not', tweet)
            tweet = re.sub(r'\bwont\b', 'will not', tweet)
            tweet = re.sub(r'\bid\b', 'i would', tweet)
            tweet = re.sub(r'wtf', 'what the fuck', tweet)
            tweet = re.sub(r'\bwth\b', 'what the hell', tweet)
            tweet = re.sub(r'\br\b', 'are', tweet)
            tweet = re.sub(r'\bu\b', 'you', tweet)
            tweet = re.sub(r'\bk\b', 'OK', tweet)
            tweet = re.sub(r'\bsux\b', 'sucks', tweet)
            tweet = re.sub(r'\bno+\b', 'no', tweet)
            tweet = re.sub(r'\bcoo+\b', 'cool', tweet)
            tweet = re.sub(r'\\n', ' ', tweet)
            tweet = re.sub(r'\\r', ' ', tweet)
            tweet = re.sub(r'&gt;', '', tweet)
            tweet = re.sub(r'&amp;', 'and', tweet)
            tweet = re.sub(r'\$ *hit', 'shit', tweet)
            tweet = re.sub(r' w\/', 'with', tweet)
            tweet = re.sub(r'\ddelay', '\d delay', tweet)
            tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)

#         Create textblob object
            tweet = TextBlob(tweet)
            polr=float(tweet.sentiment.polarity)
            polr=polr*1
            polr=polr+1
#            if(polr<=-0.1):
#                polr=-1
#            elif(polr>=0.1):
#                polr=1
#            elif(polr>-0.1 and polr<0.1):
#                polr=0
            polarity.append(polr)
    return polarity    
list=tweets()

#print(df)
#df.plot(kind='line')
#submission1 = pd.DataFrame({
#        "month": use1,
#        "polarity": list
#    })
#print(submission1)
print("****************************************************")
polarity1=[]
def tweets():
    for row in combine2:

            tweet=row

#        # Fix classic tweet lingo
            tweet = re.sub(r'\bthats\b', 'that is', tweet)
            tweet = re.sub(r'\bive\b', 'i have', tweet)
            tweet = re.sub(r'\bim\b', 'i am', tweet)
            tweet = re.sub(r'\bya\b', 'yeah', tweet)
            tweet = re.sub(r'\bcant\b', 'can not', tweet)
            tweet = re.sub(r'\bwont\b', 'will not', tweet)
            tweet = re.sub(r'\bid\b', 'i would', tweet)
            tweet = re.sub(r'wtf', 'what the fuck', tweet)
            tweet = re.sub(r'\bwth\b', 'what the hell', tweet)
            tweet = re.sub(r'\br\b', 'are', tweet)
            tweet = re.sub(r'\bu\b', 'you', tweet)
            tweet = re.sub(r'\bk\b', 'OK', tweet)
            tweet = re.sub(r'\bsux\b', 'sucks', tweet)
            tweet = re.sub(r'\bno+\b', 'no', tweet)
            tweet = re.sub(r'\bcoo+\b', 'cool', tweet)
            tweet = re.sub(r'\\n', ' ', tweet)
            tweet = re.sub(r'\\r', ' ', tweet)
            tweet = re.sub(r'&gt;', '', tweet)
            tweet = re.sub(r'&amp;', 'and', tweet)
            tweet = re.sub(r'\$ *hit', 'shit', tweet)
            tweet = re.sub(r' w\/', 'with', tweet)
            tweet = re.sub(r'\ddelay', '\d delay', tweet)
            tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)

#         Create textblob object
            tweet = TextBlob(tweet)
            polr=float(tweet.sentiment.polarity)
            polr=polr*1
            polr=polr+1
#            if(polr<=-0.1):
#                polr=-1
#            elif(polr>=0.1):
#                polr=1
#            elif(polr>-0.1 and polr<0.1):
#                polr=0
            polarity1.append(polr)
    return polarity1    
list1=tweets()

submission1= pd.DataFrame({
        "month": use1,
        "polarity_iphone7": list,
#        "polarity_oneplus": list1
    })
submission1=submission1.groupby("month")['polarity_iphone7'].sum()
print(submission1)
submission2= pd.DataFrame({
        "month": use2,
#        "polarity_iphone": list,
        "polarity_oneplus3T": list1
    })
submission2=submission2.groupby("month")['polarity_oneplus3T'].sum()
print(submission2)

#result=submission1.join(submission2,on='month',how='outer')
#print(result)
submission1.plot(legend='iphone7')
submission2.plot(legend='oneplus3T')

plt.show()
#
#        # Correct spelling (WARNING: SLOW)
#        #tweet['TextBlob'] = tweet['TextBlob'].correct()
