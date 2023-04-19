# -*- coding: utf-8 -*-
"""
@author: a.lyzin
"""

import pandas as pd

path = r'' #add filepath
groupper = '' #add groupping argument (column)
savepath = r'' #add directory and filename xlsx to save the result

df = pd.read_excel(path)
df_out = pd.DataFrame()
df_mid = pd.DataFrame()
groups = df[groupper].unique()



for group in groups:
    #handle the date
    df2 = df.query("Vehicle_Model==@group")
    df3 = df.query("Vehicle_Model==@group")
    df3['Maintenance_NO'] = df3['Maintenance_NO'].replace([1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20])
    df4 = df.query("Vehicle_Model==@group")
    df4 = df4.loc[df4['Maintenance_NO'] == 1]
    df4['Maintenance_NO'] = df4['Maintenance_NO'].replace([1],[21])
    
    df_mid = pd.concat([df2, df3, df4])
    
    df_mid = df_mid.sort_values(by=['Maintenance_NO'])
    df_mid['Cumulitive_Cost'] = df_mid['Total_PM_Cost_Discounted'].cumsum()
    df_out = df_out.append(df_mid)
    
df_out.to_excel(savepath)
