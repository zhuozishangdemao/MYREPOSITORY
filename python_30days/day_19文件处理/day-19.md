## 文件路径
### 绝对路径
从盘符或者根目录开始的完整的地址：  
"C:/Users/YourName/data.txt"
### 相对路径
相对于当前工作目录的位置
* .:当前目录：./data.txt
* ..:上一级目录：../data.txt  
如果data.txt在当前目录下，直接使用data.txt和./data.txt效果完全一样
注意什么是当前工作目录：当我们在VSCODE运行时。打开某个文件夹的过程建立了工作的初始位置，也就是终端开始的位置。在后续的运行中，打开这个文件夹中的某个文件或者文件夹，都是在这个工作目录的基础上进行操作。终端操作的位置就是工作目录的位置。./返回的就是这个工作目录的位置，对于这个vscode项目，MYREPOSITERY就是当前的工作目录。如果想让./为day_19文件处理，必须要在目录运行cd python_30days/day_19文件处理,再运行python day_19.py才能把day_19文件处理作为工作文件夹。
### 脚本位置和运行位置
运行位置指向的就是上面说的工作目录，脚本位置可以通过  
1. __file__:得到文件的绝对路径或者相对路径（取决于你是从什么源头移动cd的，如果是直接打开，C到当前脚本就是绝对路径，如果是再在终端移动，则会以之前的终端为源头输出相对路径
2. os.path.abspath(__file__)：os方法可以直接得到绝对路径
## 文件处理
本节关注各种文件格式的处理(.txt .json .xml .csv .tsv .excel)
### 文件处理函数
#### 打开文件
```py
open('filename',mode)#mode(r,a,,w,x,t,b)，默认模式为读取
```
- "r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则返回错误
- "a" - 追加 - 打开文件进行追加，如果文件不存在则创建文件
- "w" - 写入 - 打开文件进行写入，如果文件不存在则创建文件
- "x" - 创建 - 创建指定的文件，如果文件已存在则返回错误
- "t" - 文本 - 默认值。文本模式#t和b跟在awr之后表示打开的形式
- "b" - 二进制 - 二进制模式（例如图像）
#### 读取文件
```py
f=open(file_path)
txt = f.read()#read方法，返回一str类型变量，内容是txt内的全部文本（若是以rt形式打开）
txt.read(10)#读取文本文件前十个字符
txt.readline()#只读取第一行
txt.readlines()#逐行读取所有文本，并返回一个行列表
txt.splitlines()#效果和readlines一致
f.close()#由于很容易忘记关闭
with open(file_path) as f :
    txt = f.read()
#他会自动关闭打开的文件f
```
#### 文件指针
filepointer决定了下一次读取和写入从文件哪一个字节位置开始，它的位置和
* 文件的打开方式
* seek&&tell函数相关
##### seek&tell
```py
f.tell():返回当前指针的位置
f.seek(offset,whence=0):#whence为参照点，0 为文件开头，1 为当前指针位置，2 为文件末尾，offset为移动距离。在文本模式的打开方式下只允许offset为0
```
##### write()和打开方式
模式|初始指针位置|write()后指针位置|write()写入位置|
|---|---|---|---|
|r/r+|开头|写入内容末尾|当前指针处（覆盖）|
|w/w+|开头（清空）|写入内容末尾|当前指针处|
|a/a+|末尾|文件新末尾|强制文件末尾|
#### 写入和更新文件
```py
with open(file_path,'a') as f :
    f.write('此文本附加在末尾')
with open(file_path,'w') as f :
    f.write('这段文本将被写入新创建的文件中')
#在写入之后如果还要读写就要将文件指针移动
```
#### 删除文件
```py
import os
os.remove(file_path)
#更保险的
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('文件不存在')
```
### 文件类型
#### 带有txt拓展名的文件
#### 带有json拓展名的文件
字符串化的Javascript对象或Python字典
```py
# 字典
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}
# JSON: 字典的字符串形式
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# 我们使用三个引号并使其多行以使其更具可读性
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}'''
```
##### 将json转化为字典
```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''
person_dct = json.loads(person_json)#load方法,将如上格式的字符串转化为字典，事实上更常用的应该是load方法
with open(file_name,'r',encoding="utf-8-sig")as fjson:
    json_data = json.load(fjson)
    print(json_data)
#可以直接将json文件转化成python字典，不需要额外操作
```
##### 将字典转化为json文件
将字典转化为json字符串
```py
import json
# python字典
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
# 将字典转换为JSON字符串
person_json = json.dumps(person, indent=4) # indent可以是2, 4, 8. 它漂亮地打印了。
print(type(person_json))
print(person_json)
#更一般的直接保存为json文件bump()方法
import json
# python字典
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)#
```
#### 带有csv拓展名的文件
csv代表逗号分隔值。是一种简单的文件格式，用于存储表格数据，常见于数据科学  
例如  
"name","country","city","skills"  
"Asabeneh","Finland","Helsinki","JavaScript"  
```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w+ 创建文件（如果不存在），这里返回生成器表达式，可以通过for循环或者exit进行调用，每次返回每一行的一个列表，delimiter确保分割器是逗号
    #一个cvs文件的例子
    # name,age,city
    # Asabeneh,30,Helsinki
    # Zhang San,25,Beijing
    # Li Si,22,Shanghai
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'列名为: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]}来自{row[1]}的{row[2]}。 他了解{row[3]}')
            line_count += 1
    print(f'已处理{line_count}行。')
#也可以从python写入cvs文件
import csv
with open('./files/csv_example.csv', 'w', encoding='UTF8', newline='') as f:#newline确保每两行之间不会多出空行，
    writer = csv.writer(f)#相当于打开这个文件要进行写了
    # 写入列名
    writer.writerow(['name', 'country', 'city', 'skills'])
    # 写入数据
    writer.writerow(['Asabeneh', 'Finland', 'Helsinki', 'JavaScript'])#每次写入一行
#更好的写入方式为通过dict进行读写
import csv

# 读取为字典
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])  # 直接用列名访问

# 写入字典
fieldnames = ["name", "age", "city"]
with open("output_dict.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 写入表头
    writer.writerow({"name": "Asabeneh", "age": 30, "city": "Helsinki"})
```
#### 带有xlsx拓展名的文件
读取excel文件
```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```
#### 带有xml拓展名的文件
XMl为元标记语言，目的是传递结构化的数据，比如树状结构的数据
例如：
```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScript</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```
使用py中的xml.etree.ElementTree处理
```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')#.parse方法，读取并解析指定路径的xml文件，返回一个ElemenrTree的对象，代表整课XML文档树

root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('字段: ', child.tag)
```