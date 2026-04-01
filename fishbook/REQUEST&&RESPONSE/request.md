## request  
### request.get()
作用：向指定的url发送httpget请求，返回一个response对象<br>
语法
```py
import request
request.get(url,params=None,**kwargs)
```
常见参数  
- params:作为查询参数

### response.raise_for_status()

作用：检查响应状态码，若为4xx或者5xx，抛出HTTPError异常；否则什么都不做（2xx为正常取值）
可以快速判断请求是否成功

### response.json()
作用：将响应的内容（json格式字符串）解析为PYthon对象，通常为字典或者列表
