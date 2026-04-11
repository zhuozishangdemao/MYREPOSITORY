## 函数
### 使用键值对传递参数
```py
def function_name(para_1,para_2):
    codes
    codes
print(function_name(para_2='John',para_2='mike'))
```

### 带默认参数的函数
```py
def function_name(param = value):
    codess
function_name()
function_name(arg)
```

### 接受不定数量的参数
```py
def function_name(*args):
    codes 
    codes
function_name(arg1,arg2,arg3)
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # 相当于 total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```
###  函数中的默认和不定数量的参数

```py
def generate_groups(team,*args):
    print(team)
    for i in args :
        print(i)
print(generate_groups('Team1','Adesib','Nike'))
```

### 作为另一个函数参数的函数

```py
def square_number (n) :
    return n*n
def do_somethin(f,x):
    return f(x)
print(do_something(sqaure_number,3))
