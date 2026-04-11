## 循环
### while
基本语法
```py
while conditon :
    code 
while condition:
    code
else :
    code##在false处最后执行
break#退出循环
continue
```
### for

```py
for iterator in lst :
    code
##列表，元组，字典，集合，字符串可遍历
##字典循环为访问键
for key in dict :
    print(key)
for key,value in dict.items() :
    print(key ,value)#实现键值对的输出
for iterator in range():
    code
else :
    do something#实现在循环结束执行特定的代码
for number in range(6) :
    pass#在python中当不需要任何代码执行的时候，pass可以作为填充代码避免报错
```

### range
range用于生产一个序列的数字
```py
range(start=0,end=final,step=1)#左闭右开

