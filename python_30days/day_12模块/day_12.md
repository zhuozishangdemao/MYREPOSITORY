## 模块
模块：包含一组代码或者一组函数的文件，可以包含在一个应用程序中。模块可以是包含单个变量，函数或者大规模代码库的文件

### 模块操作
```py
import mymodule
mymodule.function(para)
from mymodule import function
from mymodule import function as new_function_name
```

### 内置模块
#### OS模块
```py
import os
os.mkdir('directory_name')#创建目录
os.chdir('path')#更改目录
os.getcwd()#获取工作目录
os.rmdir()#删除目录
```
#### Sys模块
返回运行时不同部分的变量和函数，0处时脚本的名称，1处是传入的参数
```py
import sys
print(sys.argv[0],argv[1],argv[2])#文件名 augument1 argument2
sys.exit()#一某些值退出，0为正常，非0为不成材
sys.maxsize()#环境最大整形变量
sys.path()#知道环境路径，环境路径指的是进行import操作时，python会在这个环境路径的列表中查找
#[
'c:\\Users\\zhuozishangdemao\\Desktop\\MYREPOSITORY\\python_30days\\day_12模块',  # ① 脚本所在目录
'C:\\Users\\zhuozishangdemao\\anaconda3\\envs\\torch_env\\python39.zip',         # ② 标准库压缩包
'C:\\Users\\zhuozishangdemao\\anaconda3\\envs\\torch_env\\DLLs',                 # ③ 动态链接库目录
'C:\\Users\\zhuozishangdemao\\anaconda3\\envs\\torch_env\\lib',                  # ④ 标准库路径
'C:\\Users\\zhuozishangdemao\\anaconda3\\envs\\torch_env',                       # ⑤ Python 环境根目录
'C:\\Users\\zhuozishangdemao\\anaconda3\\envs\\torch_env\\lib\\site-packages',   # ⑥ 第三方包安装位置
...  # 其他第三方相关目录
#]
sys.version()#使用的python的版本
```
#### 统计模块
```py
from statistics import *#导入全部模块
ages = list
mean(ages)
median(ages)#中位数
mode(ages)#众数
stdev(ages)#标准差
```
#### 数学模块
```py
import math
math.pi 
math.sqrt(num)
math.pow(num,exp)
math.floor(num)#向下取整
math,ceil(num)
math.log10*()
```
#### 字符串模块
```py
import string 
print(string.ascii_letters)#所有的ascii字母[a-zA-Z]
string.digits#[0-9]
string.punction#[`0-9a-zA-Z]
```
#### 随机模块
```py
from randowm import random ,randint
random()#0到0.9999
randint(5,20)#随机整数含边界
random.choice(seq)#从序列中随机选择一个元素
random.choices(seq,k=N)#有放回的随机选择N个元素，可以设置权重
random.sample(seq,k=N)#不放回的随机取N个元素
random.shuffle(seq)#就地打乱序列中的元素
```
