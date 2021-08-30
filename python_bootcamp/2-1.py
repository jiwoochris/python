from typing import Coroutine
import pandas as pd

info1 = pd.read_csv('C:\\Users\\정지우\\Downloads\\Materials\\stock_info_1Q.csv', encoding = 'cp949', low_memory=False, index_col = 0)
print(info1)

info2 = pd.read_csv('C:\\Users\\정지우\\Downloads\\Materials\\stock_info_2Q.csv', encoding = 'cp949', low_memory=False, index_col = 0)
print(info2)

stock_info = pd.concat( [info1, info2] )
print(stock_info)

print(stock_info.describe())

samsung_info = stock_info[['삼성전자', '삼성바이오로직스', '삼성전자우', '삼성SDI']]
print(samsung_info)

print(stock_info.shape)

print(stock_info.isnull().sum())

stock_info = stock_info.fillna(method = 'pad')

print(stock_info.isnull().sum())

return_df = (stock_info / stock_info.shift(1) * 100 - 100).dropna()

print(return_df)

corr_df = return_df.corr()

corr_df = corr_df.style.background_gradient()

display(corr_df)
