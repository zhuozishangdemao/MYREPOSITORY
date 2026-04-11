## 字典

### 操作
```py
empty_dict = {}
dict ={'key1':'value1','key2':50}#值可以为任何类型：字符串 布尔值 列表 元组 集合 字典
len(dict)
dct['key']#访问字典
dict.get('key')#可以防止因为没有对应的键抛出错误，若无会返回none
dict['new_key']='new_element'#添加新的键值对
dict['original_key']='new_element'#修改原有的键值对
'key' in dict #检查是否有
dict.pop('key1')
dct.popitem()#删除最后一项
del dct['key2']
dct.items()#把字典转化成元组组成的列表
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
dct.clear()
del dict
dict_copy = dct.copy()
dct.keys()#返回所有键的列表
dct.values()