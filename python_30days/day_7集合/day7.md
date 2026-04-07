## 集合
### 创建集合
```py
    st = set()
    st ={ 'item1','item2','item3'}
```
### 集合操作
```py
len(st)
'item1' in st
st.add('item')
st.update(['item1','item2','item3'])#update接受列表为参数
st.remove('item')#若无此元素抛出错误
st.discard()#不会抛出错误
st.pop()#随机抛出元素
st.clear()
del st
lst = ['item1','item2']
st = set(lst)#列表转集合
st3 = st1.union(st2)#合并集合
st1.update(st2)#添加集合
st1.intersection(st2)#返回交集
st2.issubset(st1)#返回True or False
st1.issuperset(st2)#检查是否为超集
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
#差集
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
#集合的对称差异：共有项的补集
st1.symmetric_difference(st2)
#检查两个集合是否相交
st2.isdisjoint(st1)
