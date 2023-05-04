# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:31:12 2023

把双色球开奖数据写到csv

@author: Roger
"""
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


def update_ssq(latest_count = 50, local = 'ssq2013.csv'):
    '''提取最近n期的数据，更新加入到csv文件'''
    # 请求URL
    url = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount='+str(latest_count)
    
    # 发送请求
    response = requests.get(url)
    
    # 解析JSON
    data = response.json()
    result = data['result']
    
    rows = []
    for item in result:
        rq = int(item['code'])
        red = item['red']
        blue = int(item['blue'])
        red_list = red.split(',')
        row = [rq,]+[int(i) for i in red_list]+[blue]
        rows.append(row)
    
    df = pd.DataFrame(rows)
    df.columns = ['id', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue']
    df_new = df.set_index(['id'])
     
    df_old =pd.read_csv(local,
                    encoding='ISO-8859-1',
                    index_col = 'id',
                    )
    
    df_combine = pd.concat([df_new,df_old],join = 'inner').drop_duplicates()
    # print(df_combine)
    
    df_combine.to_csv(local, index=True,)
    
    
    print('数据已导出到ssq2013.csv文件中')
    

# update_ssq()