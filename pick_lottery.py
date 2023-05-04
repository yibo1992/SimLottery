# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:22:25 2023

中国福利彩票双色球模拟选球
主要逻辑，运行一次，选出一个号，不放回，模拟现场抽球

会检查选出的号码是否曾经中过四等奖及以上

@author: roger
"""
import pandas as pd
import random

from bll.check_result import check_lottery
from dal.histdata import update_ssq


'''更新数据库'''
update_ssq(latest_count = 10)


'''初始球组'''
redballs = list(range(1,34))
blueballs = list(range(1,17))

def pick_balls(balls,num_chosen=6):
    '''抽出一个球'''
    chosens = []
    while num_chosen>0:
        roll_ball = input('请转动轮盘') # 用户回车 摇出球
        picked = random.randint(1,len(balls))
        print(str(balls[picked-1])+'被转出')
        chosens.append(balls[picked-1])
        balls.remove(balls[picked-1])
        # print(balls)
        num_chosen+=-1
    print(chosens)
    return(chosens)
 
'''实际抽球，运行一次抽一个，时间间隔自己把控，模拟真随机'''    
reds = pick_balls(redballs)

blues = pick_balls(blueballs,num_chosen=1)

selected = [reds,blues]


df =pd.read_csv('ssq2013.csv',
                encoding='ISO-8859-1',
                )
df.columns=['rq','r1','r2','r3','r4','r5','r6','b',]
# print(df)

check_lottery(selected,df)
