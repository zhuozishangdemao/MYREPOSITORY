## 正则表达式
是一种特殊的文本字符串，在数据中查找模式
```py
import re
```
- *re.match()*：只在字符串的第一行开头搜索，如果找到则返回匹配的对象，否则返回None。
- *re.search*：如果字符串中的任何地方（包括多行字符串）有匹配项，则返回匹配对象。??//相较于match包含了整个文本
- *re.findall*：返回包含所有匹配项的列表。
- *re.split*：接受一个字符串，在匹配点处分割，返回一个列表。
- *re.sub*：替换字符串中的一个或多个匹配项。

### re.match()
re.match(substring,string,re.I)  
返回带有span和match的对象  
match = re.match('I love to teach',txt,re.I)  
print(match) #<re.Match object;span=(0,15),match = 'I love to tteach'>
span = match.span()  
print(span) #(0,15)

### re.search()
re.search(substring,string,re.I)   

### re.findall()
将所有匹配项以列表的形式返回  
匹配模式可以受
- 第三个参数决定 ：
    ```py
    txt = '''Python is the most beautiful language that a human being has ever created.
    I recommend python for a first programming language'''
    # 它返回一个列表
    matches = re.findall('python', txt, re.I)
    print(matches)  # ['Python', 'python']
    ```
- 不同的模式编写方式决定
    ```py
    txt = '''Python is the most beautiful language that a human being has ever created.
    I recommend python for a first programming language'''

    matches = re.findall('Python|python', txt)
    print(matches)  # ['Python', 'python']
    matches = re.findall('[Pp]ython', txt)
    print(matches)  # ['Python', 'python']
    ```

### re.split
re.split(pattern ,string,maxsp,it=0,flags=0)  
flags:匹配标志  
string：要分割的原始字符串
pattern：正则表达式模式，指定分割符
maxsplit：最大分割次数

### 替换字符串
re.sub('original string','afterstring',txt,re.I)

### 使用RegEx拆分文本
re.split('\n',txt)#使用\n分割行尾符号

### 编写RegEx模式
类比：声明字符串变量使用双引号或者单引号，如果声明RegEx变量要使用r’‘ 
实际例子：不区分大小写的apple  
regex_pattern = r'[Aa]pple'  
使用标志re.I  
- []:一组字符
    * [a-c]:a or b or c
    * [a-z]:a or b or c..or z
    * [A-Z]:A or B or C..or Z
    * [0-9]:0 or1 or 2..or 9
    * [A-Za-z0-9]:any character
- |:表示或者
    regex_pattern = r'[Aa]pple|[Bb]anana'

-  \d:表示一个特殊字符数字
    regex_pattern = r'\d'
- \d+:+表示有一个或者多个数字
    ```py
    regex_pattern = r'\d'  # d 是一个特殊字符，表示数字
    txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
    matches = re.findall(regex_pattern, txt)
    print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']
    regex_pattern = r'\d+'  # d 是一个特殊字符，表示数字，+ 表示一个或多个
    txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
    matches = re.findall(regex_pattern, txt)
    print(matches)  # ['6', '2019', '8', '2021']
    ```
- \ \d:表示反斜杠
    ```py
    regex_pattern = r'\\d'  # 这意味着寻找 \d
    txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
    matches = re.findall(regex_pattern, txt)
    print(matches)  # []
    ```
- 句点.:.表示任何字符，除了新行也就是匹配除了换行符之外的任意单个字符#不可以匹配a\ncb
- *:表示匹配零次或者多次（针对的是它前面的那个字符：可以是a，可以是-，也可以的.
    ```py
    regex_pattern = r'[a].*'  # . 任何字符，* 任何字符零次或多次
    txt = '''Apple and banana are fruits'''
    matches = re.findall(regex_pattern, txt)
    print(matches)  # ['and banana are fruits']
    ```
- ?:表示匹配0次或者一次
    ```py
    txt = '''I am not sure if there is a convention how to write the word e-mail.
    Some people write it as email others may write it as Email or E-mail.'''
    regex_pattern = r'[Ee]-?mail'  # ? 表示零次或一次
    matches = re.findall(regex_pattern, txt)
    print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
    ```
- {digit}:表示匹配的模式长度  
r'\d{4}':正好有四位数字
r'\d{1,4}':1到4位数字

- ^:脱字符
表示以什么开始：
    ```py
    txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
    regex_pattern = r'^This'  # ^ 表示以 This 开始
    matches = re.findall(regex_pattern, txt)
    print(matches)  # ['This']   
    ```
  表示否定：
    ```py
    txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
    regex_pattern = r'[^A-Za-z ]+'  # ^ 在方括号内表示否定，不是A-Z，不是a-z，不是空格
    matches = re.findall(regex_pattern, txt)
    print(matches)  # ['6,', '2019', '8,', '2021']
    ```
- \w和\W:匹配单词字符和非单词字符  
单词字符\w:[0-9a-zA-Z_]  
非单词字符\W:[^0-9a-zA-Z_]  
- 字符串边界设置   
1. ^:匹配字符串的开头，指的是待匹配的字符串的行的开头，默认条件下只考虑第一行的开头，通过re.M可以匹配多行的开头
2. \$:匹配字符串的结尾

3. \\b:匹配单词边界
    ```py
    text = 'cat, caterpillar, catfish'

    # 匹配独立的单词 "cat"（前后不是单词字符）
    print(re.findall(r'\bcat\b', text))   # ['cat']  只匹配第一个 cat，后面的 caterpillar 和 catfish 中的 "cat" 不是独立单词

    # 匹配以 "cat" 开头的单词
    print(re.findall(r'\bcat\w*', text))  # ['cat', 'caterpillar', 'catfish']

    #匹配以 "cat" 结尾的单词
    print(re.findall(r'\w*cat\b', text))  # ['cat']  因为 caterpillar 和 catfish 中的 cat 不在末尾
    ```
4. \\B:匹配非单词边界

- \s:空白符号的元字符，匹配空格制表符换行符回车符换页符

- \Z:字符串绝对的结尾，忽略末尾的换行符

### match.group

提取怕匹配的内容  
方式：gorup(n)返回第n个捕获组的内容，group() or gourp(0)返回整个匹配的字符串  

 ```py
    import re
    m = re.search(r'(\d+)-(\d+)', '编号 123-456')
    print(m.group())     # '123-456'
    print(m.group(0))    # '123-456'
    print(m.group(1))    # '123'
    print(m.group(2))    # '456'
    print(m.groups())    # ('123', '456')
```

### (?:...)非捕获组
括号内的表达式整体分组，但是不占用捕获组group的编号

###  (?=...)正向前瞻断言
要求当前位置之后的字符串必须匹配...中的模式，但不消耗位置