### try
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
    except Exception as e:
        print(f"未知错误: {e}")
    else:
        print("文件读取成功")
    finally:
        print("尝试读取文件结束")
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


### 函数的预期输入与预期返回  
语法  
```py
def get_weather(city : str) ->str:
    return f'{city}当前天气:{weather_desc}'
```
city : str表示预期的city输入值为str类型
->str表示预期的返回值是str类型

### .get()函数
用于安全的获取键对应的值，若键不存在会返回默认值none
```py
value = dict.get(key, default=None)
if(response.get('answer'))
   return response['ansswer']
formatted_results =[] 
for result in response.get('results',[])#这里使得默认值为一个空的列表
```
以上为更安全的读取字典的操作，不会抛出异常err，第二个参数（也就是第一行中的defalut）为默认值，也就是当key不存在的时候，返回结果就是默认值

