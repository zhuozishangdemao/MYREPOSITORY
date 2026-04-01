## OS

### os.dirname  
返回路径中目录部分，也就是去掉最后一级文件名或目录名的路径
```py
dataset_dir = os.path.dirname(os.path.abspath(__file__))#__file__为python内置文件的相对路径
save_file = dataset_dir + "/mnist.pkl"
#若脚本位于/home/user/code/load_data.py
#dataset_dir = /home/user/code
#save_file = /home/user/code/mnist.pkl
```

### os.environ
用于访问操作系统的环境变量
- **读取**：获取环境变量的值<br>
- **设置**：修改或新增环境变量<br>
- **删除**：删除环境变量<br>
**读取**<br>
```py
import os

# 获取 PATH 环境变量
path = os.environ.get('PATH')
print(path)

# 如果变量不存在，返回 None（推荐使用 get 避免 KeyError）(和字典的使用方式一致)
db_url = os.environ.get('DATABASE_URL', '默认值')

# 直接访问可能引发 KeyError
# api_key = os.environ['API_KEY']   # 若不存在会报错
```
**设置**
```py
os.environ['MY_VAR'] = 'hello'
print(os.environ['MY_VAR'])   # 输出 hello
```
**删除**
```py
del os.environ['MY_VAR']
```