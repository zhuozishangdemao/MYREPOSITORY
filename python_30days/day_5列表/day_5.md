## 列表
python中有四种数据集合类型
- List：有序且可变的集合。允许重复元素
- Tuple：有序且不可变的集合。允许重复元素
- Set：无序且不可变的集合，但可以增加元素，无重复元素
- Dictionary：无序，可变，可索引的集合。不允许重复元素

### 创建列表

```py
lst = list()#默认长度为0
lst=[]
lst =[ 'asmbia',250,True,{'duck':'play'}]#可以包含不同种类元素
```

### 操作函数
```py
len(lst)
lst[index]#索引访问正索引0，1，2....
#负索引-1，-2，-3...
first_item,second_iem,&rest = lst#拆解列表
lst[para1:para2:para3]#para1起始索引，默认为开始，para2结束索引，默认为尾部，para3步长大小，默认为1
lst[index]=new_element#修改列表
in #检查元素是否在列表，返回boolen
lst.append(item)#末尾添加元素
lst.insert(index,item)#其他项会向右移动
lst.remove(item)#删除第一次出现的item
lst.pop(index)#按照索引删除列表元素
del lst[index]
del lst[start_index:end_index]#左闭右开
del lst#删除一项或者删除全部
lst.clear()#清空列表项
lst.copy()#不通过引用而是通过复制的方式创建新的列表变量
lst1=;st2+lst3#列表连接
lst1.exetend(lst2)#附加列表
.count(item)#统计元素出现次数
.index(item)#查找项
.reverse()#反转列表
.sort()#ascending 
.sort(reverse=True)#descending
sorted_list=sorted(lst,reverse=True)

```