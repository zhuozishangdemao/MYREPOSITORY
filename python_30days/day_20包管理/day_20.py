import requests # 导入请求模块

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # 来自网站的文本

# response = requests.get(url) # 打开网络并获取数据
# print(response)
# print(response.status_code) # 状态码，成功时为200
# print(response.headers)     # 获取响应的头部信息
# print(response.text) # 获取文本数据
# from pprint import pp # 导入pretty print，以美观地显示

# url = 'http://api.worldbank.org/countries/et?format=json'  # 埃塞俄比亚经济数据API
# response = requests.get(url)  # 打开网络并获取数据
# print(response) # 响应对象
# print(response.status_code)  # 状态码，成功时为200
# # 让我们改变响应的JSON格式
# ethiopia_data = response.json()
# pp(ethiopia_data) # 用pretty print打印数据
from mypackage import arithmetics
print(arithmetics.add_numbers(1, 2, 3, 5))
print(arithmetics.subtract(5, 3))
print(arithmetics.multiple(5, 3))
print(arithmetics.division(5, 3))
print(arithmetics.remainder(5, 3))
print(arithmetics.power(5, 3))

from mypackage import greet
print(greet.greet_person('张', '三'))