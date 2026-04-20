### 网页抓取
需要requests和beatifulsoup4
前者可以获得网站响应的html源代码文件，后者进行解析  
### html文件结构
html的逻辑：树状嵌套结构
文档 (document)
 └── <html> （根元素）
      ├── <head> （头部：元信息、标题等，不显示在页面正文）
      └── <body> （身体：所有你看得见的内容都在这里）
           ├── <header> （页眉区域）
           ├── <main>   （主要内容区域）
           │    ├── <h1> 主标题 </h1>
           │    ├── <div class="post"> 
           │    │    ├── <h2> 文章标题 </h2>
           │    │    ├── <p> 第一段 </p>
           │    │    └── <p> 第二段 </p>
           │    └── </div>
           └── <footer> （页脚区域）
三大组成要素
1. Tag：<p><div><a>定义内容是什么类型
2. Attribute：属性，在**标签内**的额外信息，提供元素的ID，类名，链接地址，如class="title"、href="..."
3. Text文本内容：**标签之间**的纯文字，是用户实际阅读到的文字
<a href="https://example.com" class="link">点击访问</a>
ID和类是HTML文件的身份标签。ID用于唯一的确定一个元素，class可以重复使用，给一组元素贴上相同的标签

### 实际操作
```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # 我们从网站获取所有内容，逸二进制的方法保存
soup = BeautifulSoup(content, 'html.parser') # beautiful soup将给我们一个解析的机会,s
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>返回HTML第一个<title>标签的tag对象
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets，返回标签的纯文本等同于soup.title.text
print(soup.body) # 给出网站上的整个页面,返回<bdoy>标签的对象
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# 我们定位cellpadding属性值为3的表格
# 我们可以使用id、class或HTML标签进行选择，有关更多信息，请查看beautifulsoup文档
table = tables[0] # 结果是一个列表，我们从中提取数据
for td in table.find('tr').find_all('td'):
    print(td.text)
```