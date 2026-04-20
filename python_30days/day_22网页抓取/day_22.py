import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# 让我们使用requests的get方法从url获取数据
response = requests.get(url)
# 检查状态
status = response.status_code
print(status) # 200表示获取成功
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # 我们从网站获取所有内容
soup = BeautifulSoup(content, 'html.parser') # beautiful soup将给我们一个解析的机会
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # 给出网站上的整个页面
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# 我们定位cellpadding属性值为3的表格
# 我们可以使用id、class或HTML标签进行选择，有关更多信息，请查看beautifulsoup文档
table = tables[0] # 结果是一个列表，我们从中提取数据
for td in table.find('tr').find_all('td'):
    print(td.text)