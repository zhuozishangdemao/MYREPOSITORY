## 高阶函数
### 高阶函数
将实现一下三个目标  
1. 将函数作为参数传递
2. 将函数作为返回值
3. 使用python闭包和装饰器
前两个目标，只要加f作为函数参数，将函数入口地址（也就是函数的名称）传入就可以了  
**Python闭包**  
Python运行嵌套函数（内部定义的函数）访问封闭函数的作用域。此行为成为闭包:直观的理解可以看作在创建函数时的参数也可以被外包的函数决定
```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```
### Python装饰器
在不修改对象结构的条件下为之增加新的功能，调用方式：在想要装饰的函数定义之前调用
 ```py
 # 普通函数
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

# 使用装饰器实现上面的示例

'''这个装饰器函数是一个高阶函数，接收一个函数作为参数'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator#调用方式
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
#greeting会被自动执行
#greeting=uppercase_decorator(greeting)
#定义接受参数的装饰器函数
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```
### 内置高阶函数
**Map函数**
```py
map(function,iterable)
#返回一个iterable
```
**Filter函数**
```py
filter(function,iterable)
#只保留在function下为True的元素
```
**Reduce函数**
```py
from functools import reduce
reduce(function,iterable)
#从左到右一次将累计值与下一个传入的元素作function
```

