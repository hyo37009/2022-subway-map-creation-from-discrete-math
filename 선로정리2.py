import pandas as pd
import subway
import os

allData = pd.read_excel('운영기관_역사_코드정보.xlsx')

print(allData.head())

newData = allData[['LN_NM', 'STIN_NM']]

print(newData.head())

