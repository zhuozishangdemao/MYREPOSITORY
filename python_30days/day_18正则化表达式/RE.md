## RE
用于正则表达式操作的模块：描述字符串模式的工具  
常见任务  
- 匹配：判断字符串是否符合某种模式
- 搜索：在字符串中查找第一个符合模式的子串
- 查找所有：找出所有符合模式的子串

### re.research(pattern,string,flags)  
在字符串搜索第一个匹配的位置，返回match对象  
match对象是返回的结果
```py
match = re.research(r'(Thought:.*?Action:.*?)',llm_output,re.DOTALL)
if match:
    execute#判断是否正常进行
```

### r'
原始字符串，将\不要当作转义字符串使用

### \D\S\W
\D(dihgit):匹配数字  
\W匹配非单词字符
\s匹配非空白字符

### re.DOTALL
