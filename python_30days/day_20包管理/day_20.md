## PIP包管理
### Python PIP-Python包管理器
pip uninstill package
pip list
pip showpackage
### PIPFreeze
生成已安装的Python包及其版本，输出合适在requirements文件中使用
### 从URL读取数据
要从网站上读取数据，需要使用url从网站或者APi读取数据。API表示应用程序编程接口，是一种服务器之间叫交换结构化数据的方式，主要为json数据  
打开网络连接，我们需要一个名为_requests_的包——它允许打开网络连接并实现CRUD（创建、读取、更新和删除）操作
#### Requests
1. _get_：打开网络从url获取数据，返回响应对象
response = requests.get(url)#url为string类型
2. status_code：
response.status_code:状态码，成功时为200
3. headers：一个字典，包含了有关响应的元数据
例如{'Content-Type': 'text/plain; charset=iso-8859-1', 'Content-Length': '1935', 'Connection': 'keep-alive', ...}
4. _text_：将服务器返回的响应体内容解码为字符串返回
5. _json_：
### 创建包
可以创建自己的包，上传到python包管理器仓库，并且下载
