## 异常处理
Python使用 try 和 except 优雅地处理错误。优雅的退出（或优雅的错误处理）是一种简单的编程习惯 - 程序检测到严重的错误条件并"优雅地退出"，即以受控的方式处理结果。通常，程序会在优雅退出时向终端或日志打印描述性错误消息，这使我们的应用程序更加健壮
### try & exception
```py
try:
    import urllib.request#仅有python3.0有的module
except ImportError:
    raise ImportError('You should use Python 3.x')#若有异常后续不再执行
import os.path
import gzip
import pickle
import os
import numpy as np
```
- try块：放置可能导致异常的代码  
- except块：捕获并且处理异常，可以指定异常的类型（此处的Import Error或者ZeroDivisionError）  
- else块：无任何异常时执行
- finally块：无论如何均执行  

合理的try-except-else-finally结构
 ```py
 def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
    except PermissionError:
        print(f"错误：没有权限读取 '{filename}'")
    except Exception as e:#一种简化方式，Exception此时根据实际错误类型决定
        print(f"未知错误: {e}")
    else:
        print("文件读取成功")
    finally:
        print("尝试读取文件结束")#always run this code始终执行，可以描述为这个任务操作结束
    return None
```

可以在某个分支使用requests.exceptions中的某个异常或者全部异常来捕获，并且可以捕获并输出
```py
try:
    response = requests.get('https://api.example.com', timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("请求超时，请稍后重试")
except requests.exceptions.ConnectionError:
    print("网络连接失败，请检查网络")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 错误: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"其他请求异常: {e}")
#except requests.exceptions.RequestException as e:
    # 网络异常、超时、HTTP错误等都会进入这里
 #   raise Exception(f"网络请求异常: {e}")
```

### 打包和解包参数
#### 解包
解包：将可迭代对象的元素拆开，分别赋值给多个变量，或展开为函数参数
使用两个操作符
* *用于元组或者列表
* **用于字典（解包映射对象）
* *字典得到的是关于键的拆分

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```
#### 打包
有时候我们不知道需要向Python函数传递多少个参数。我们可以使用打包方法让我们的函数接受无限数量或任意数量的参数。也就是将参数先打包成一个列表或者字典，再在函数里进行操作，此时的输入任然是具体的参数。  
将多个分散的值收集到一个容器变量中
```py
#打包列表
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
#打包字典
def packing_person_info(**kwargs):
    # 检查kwargs的类型，它是一个字典类型
    # print(type(kwargs))
    # 打印字典项
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```
### Python中的展开
不一定要在函数中操作，作为基本语句也可以展开
#字符串
print([*"ABC"])      # ['A', 'B', 'C']
#字典（迭代的是键）
print([*{"a":1, "b":2}])  # ['a', 'b']
#文件对象（迭代行）
#with open("file.txt") as f:
#lines = [*f]
#生成器表达式
gen = (i**2 for i in range(3))
print([*gen])         # [0, 1, 4]

### 枚举
enumerate函数  
enumerate(iterable,start=0)每次迭代返回一个（index，item）元组
### Zip
zip(*iterable,strict =False)#第一个参数要求多个可迭代对象，第二个参数默认为False，若为True则在可迭代对象长度不同时抛出ValueError  
每次迭代产生一个由各个可迭代对象元素产生的元组