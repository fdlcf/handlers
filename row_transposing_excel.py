# -*- coding: utf-8 -*-
"""
@author: a.lyzin
"""
import pandas as pd

path = r'' # set excel file path

df = pd.read_excel(path)
total = pd.DataFrame()

for index, row in df.iterrows():
    df2=pd.DataFrame(row)
    row_to_y_1 = df2.loc['row1'].values[0]
    row_to_y_2 = df2.loc['row2'].values[0]
    row_to_y_3 = df2.loc['row3'].values[0]
    df2 = df2.drop(['row1', 'row2', 'row3'])
    df2.columns = ['cost']
    df2['row1'] = row_to_y_1
    df2['row2']= row_to_y_2
    df2['row3'] = row_to_y_3
    total = total.append(df2)

total.to_excel(r'') # set savedir path and filename
