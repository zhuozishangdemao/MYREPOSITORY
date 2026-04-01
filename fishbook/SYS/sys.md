## sys 库
` import sys `
### sys.path  
- python在导入模块时会按照此列表顺序查找,可以动态添加路径
```py
sys.path.append('/my/module/path')
sys.path.append(os.pardir)#添加了一条当前节点父节点的路径，使得可以扫描到朋辈的文件夹
```
[os.path](/fishbook/OS/OS.md)

### sys.argv  

- 类型：列表
- 元素：[0]为脚本名称，[1:]为传入的参数
```py
# test.py
import sys
print("脚本名:", sys.argv[0])
print("参数:", sys.argv[1:])
#运行python test.py hello world
#输出脚本名: test.py
#参数: ['hello', 'world']
```

### sys.exit([arg])  

指定退出码（0）为正常，（1）为错误退出
