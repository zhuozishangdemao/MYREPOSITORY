## 列表表达式
### 生成器对象
```py
(表达式for 变量in可迭代对象if)
#区别与列表表达式，生成器表达式不会显示的创建列表，旨在节省内存开销
### 列表推导式
```py
[f(i) for i in ierable if 表达式]#语法
#if可以是空的，f(i)可以和i无关
# 扁平化三维数组
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]#表达式可以进行嵌套，for row in list_of_lists每次都会都会返回一个iterable给for number in row 执行
print(flattened_list)
```
### Lambda函数
```py
x = lambda para1,para2,para3:返回值
x(arg1,arg2,arg3)#调用方式
