import d2l
import os
import pandas as pd
os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')


data = pd.read_csv(data_file)
print(data)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)
import torch

X = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(outputs.to_numpy(dtype=float))
print(X,y)
#创建数据集
import pandas as pd
import torch

# 创建一个 5 行 6 列的原始数据，故意放入一些缺失值 NaN
data = {
    'NumRooms': [3.0, 2.0, 4.0, float('nan'), 3.0],   # 房间数量（有一处缺失）
    'NumFloors': [1.0, 1.0, float('nan'), 2.0, 1.0],   # 楼层数（有一处缺失）
    'Area': [120.0, 85.0, 150.0, 90.0, float('nan')],  # 面积（有一处缺失）
    'Price': [250.0, 180.0, 320.0, 200.0, 270.0],      # 房价（完整）
    'Year': [2005, 1998, 2010, float('nan'), 2015],     # 年份（有一处缺失）
    'Garage': [1, 0, 1, 0, float('nan')]                # 车库数量（有一处缺失）
}

df = pd.DataFrame(data)#创建dataframe的处理对象
print("原始数据集：")
print(df)
#常见函数对于dataframe对象
df.isnull()
df.drop_duplicates()
df['年龄'].mean()
df.describe()
#df.to_csv('data.csv', index=False)
#pd.read_csv('data.csv')和文件直接交互

