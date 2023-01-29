# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:22:25 2023

中国福利彩票双色球模拟选球
主要逻辑，运行一次，选出一个号，不放回，模拟现场抽球

@author: roger
"""

import random

'''初始球组'''
redballs = list(range(1,34))
blueballs = list(range(1,17))
chosen_reds = []
chosen_blues = []

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
pick_balls(redballs)







