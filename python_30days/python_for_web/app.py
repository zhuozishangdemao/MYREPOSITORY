# 导入flask
from flask import Flask, render_template, request, redirect, url_for
import os # 导入操作系统模块

app = Flask(__name__)

@app.route('/') # 这个装饰器创建主页路由
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30天Python编程挑战'
    return render_template('home.html', techs=techs, name=name, title='主页')

@app.route('/about')
def about():
    name = '30天Python编程挑战'
    return render_template('about.html', name=name, title='关于我们')

@app.route('/post')
def post():
    name = '编程语言文章'
    path = request.path
    return render_template('post.html', name=name, path=path, title='文章')

if __name__ == '__main__':
    # 部署时我们使用环境变量
    # 使其同时适用于生产和开发环境
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)