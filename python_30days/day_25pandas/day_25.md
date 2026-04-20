## Pandas
提供了数据结构:dataframes 和 series
以及操作数据结构的工具  
重塑，合并，排序，切片，聚合，差补
### 安装pandas
series只是一列数据表，有index，columns和elemnents
pands是多列的series
### 创建panda series
```py
import pandas as pd
s = pd.Series(list)#此时index为默认0开头依次递增
s = pd.Series(list,index = [1,2,3,4,5])#自定义index
s = pd.Series(dct)#将字典转化为series，inde为key，elements为value
s = pd.Seires(10,index = [1,2,3])#创建所有element均为10的series
s = pa.Series(np.linspace(5,20.10))#linspace(起始点，终点，项目数)
# 0     5.000000
# 1     6.666667
# 2     8.333333
# 3    10.000000
# 4    11.666667
# 5    13.333333
# 6    15.000000
# 7    16.666667
# 8    18.333333
# 9    20.000000
# dtype: float64
```
## DataFrames
### 创建dataframes
```py
data = [[],[],[]]
df = pd.Dataframe(data,columns =[column1,colum2,colum3])#从多维列表读取
#         Name Country      City[column]
# 0   Asabeneh Finland  Helsinki[]每一行对应一个列表
# 1      David      UK    London[]
# 2       John  Sweden Stockholm[]
dct = {'key1':list 1,'key2' :list 2}
df = pd.Dataframe(dct)#从字典创建，key为column，value为一行
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)##从字典列表创建

import pandas as pd

df = pd.read_csv('./data/weight-height.csv')#读取cvs文件
print(df.head()) # 默认为前五行
df.tail()#获取后五行
df.shape#元组（len（index），len（column））
df.columns#index([],dtype='')
df['column1'].value_counts()#计算每个值有多少个
df.describe()#数据概要
```
### 修改dataframe
```py
# 导入pandas包
import pandas as pd
# 导入numpy包
import numpy as np
# 数据
data = [
    {"Name": "张三", "Country":"中国", "City":"上海"},
    {"Name": "李四", "Country":"中国", "City":"北京"},
    {"Name": "王五", "Country":"中国", "City":"广州"}]
# 创建一个数据框
df = pd.DataFrame(data)
weights =[74,78,69]
df['Weight'] = weights#新增加column
#修改列值
df['Name'] = ['赵六','钱七','孙八']#直接在列名写入新数据
df.loc[1,'Name'] = '小七'#通过loc方法定位index和column
df.iloc[1,0] = '大七'#iloc可以不必使用column具体名称而使用类似index方式
df['MBI'] = df['Weights']/((df['Heigth']*0.01)**2)#格式化处理
print(df[(df['age'] > 20) & (df['在职'] == True)])#筛选出年龄大于20且在值，df['age']>20返回一个bool列表，对df[list]直接对index进行切片选择
df.iloc[行选择器，列选择器]
行列选择器可以为一下类型
行选择器和列选择器都可以是以下类型之一：
单个整数
整数列表或数组
切片对象（start:stop:step）
布尔数组（长度必须与轴长度相同）
可调用函数（返回上述任一类型）
```