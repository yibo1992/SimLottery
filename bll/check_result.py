# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:35:54 2023

@author: DELL
"""


import pandas as pd

def same_amount(lst1, lst2):
    a = set(lst1)
    b = set(lst2)
    c = (a & b)
    return len(c)


def judge_the_reward_level(ticket1, ticket2):
    rednum = same_amount(ticket1[0], ticket2[0])
    bluenum = same_amount(ticket1[1], ticket2[1])
    if rednum == 6 and bluenum == 1:
        return 1
    elif rednum == 6 and bluenum == 0:
        return 2
    elif rednum == 5 and bluenum == 1:
        return 3
    elif rednum == 5 and bluenum == 0 or rednum == 4 and bluenum == 1:
        return 4
    elif rednum == 4 and bluenum == 0 or rednum == 3 and bluenum == 1:
        return 5
    elif rednum == 2 and bluenum == 1 or rednum == 1 and bluenum == 1 or rednum == 0 and bluenum == 1:
        return 6
    else:
        return 7



def check_lottery(selected,df):
    
    re = None
    for i in range(len(df)):
        # print(df.iloc[i])
        reds = df.iloc[i][['r1','r2','r3','r4','r5','r6',]].values
        blues = df.iloc[i][['b',]].values
        comparelist = [reds,blues]
        re =  judge_the_reward_level(selected, comparelist)
        if re<=3:
            print(df.iloc[i][['rq',]].values)
            print(re)
            break
    if re >3:
        print('该号码未曾中过大奖')
        
        
        
        
# df =pd.read_csv('ssq2013.csv',
#                 encoding='ISO-8859-1',
#                 )
# df.columns=['rq','r1','r2','r3','r4','r5','r6','b',]
# print(df)
               
# ticket1 = [[5,7,14,23,27,29],[4]]    
# check_lottery(ticket1,df)    