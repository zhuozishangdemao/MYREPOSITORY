## 统计模块
### 统计模块
python的statustucs模块提供了计算数值数据的数学统计模块。
### Numpy
提供了高性能的多维数组对象和用于处理这些数据的工具
#### 创建整型numpy数组
```py
list 
numpy_array_from_list = np.array(list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])
```
#### 创建浮点数numpy数组
```py
# Python列表
python_list = [1,2,3,4,5]

numpy_array_from_list2 = np.array(python_list, dtype=float)#设置默认格式
print(numpy_array_from_list2) # array([1., 2., 3., 4., 5.])
```
#### 创建布尔型numpy数组
```py

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])#非0为True
```
#### 创建多维numpy数组ndarrray
```py
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))#<class 'numpy.ndarray'>

print(numpy_two_dimensional_list)
#[[0 1 2]
#  [3 4 5]
#  [6 7 8]]
```
#### 将numpy数组转换列表.tolist()
#### 从元组创建numpy数组nparray(tuple)
#### Numpy数组的形状.shape方法，返回元组
#### Numpy数组数据类型：str,iny,float,complex,bool,list,None。通过.dtype访问
#### Numoy数组的大小：.size方法，返回元素总数
#### 加法
np.add(numoyarray,added number)或者  
nparray+num_number
#### 减法
nparray-number or np.subtract(nparray,number)
#### 乘法
nparray*number or np.multiply(nparray.number)
#### 除法
nparray/number or np.divide(nparray,number)
#### 模数
nparray%number pr np.mod(nparray,number)
#### 整除
nparray//number or np.floor_divide(nparray,number)
#### 指数
nparray**number or np.power(nparray,number)
#### 转换类型
nparray.astype('type')
#### 多维数组访问
nparray[x][y]...系数x若为:表示取所有项
#### numpy数组切片
nparray[para1:para2:para3]#起始位置，停止位置，步长  
二维数组切片  
nparray[para1:para2:para3,para4:para5:para6]先切出第0维（行），再切出第1维（列）
#### numpy连接数组
##### 水平连接
np.hstack(nparray1,nparray2,nparray3)
##### 垂直连接
np.vstack(nparray1,nparry2,nparry3)
#### numpy数值操作函数
nparry.max()  
nparray.min()
nparray.mean()
