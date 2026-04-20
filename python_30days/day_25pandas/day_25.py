import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\zhuozishangdemao\Desktop\计算机\机器学习\githubdocument\30-Days-Of-Python-master\data\hacker_news.csv")
print(df.columns)
print(df.shape)
print(df.head(10))
print(df.tail(10))
print(df.iloc[[1,3],1:4])
python_rows  = df[df['title'].str.contains('Python')]
print(python_rows.head())
df_sorted_asc = df.sort_values(by = 'num_points',ascending = False)
print(df_sorted_asc.head())
non_python_sorted = df[~df['title'].str.contains('Python', case=False, na=False)].sort_values(by='num_points', ascending=False)#~为非的含义，进行排除
print("\n过滤掉Python主题后按票数降序排序（前5条）:")
print(non_python_sorted.head())