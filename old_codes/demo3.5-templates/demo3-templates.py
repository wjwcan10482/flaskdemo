from flask import Flask, render_template
from flask_bootstrap import Bootstrap



app = Flask(__name__)
# 3.1.1 基础用法


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/usertest/<name>')
def usertest(name):
    return render_template('user.html', name=name)


# Jinjia 可以识别 列表 字典 对象
# 条件控制语句/渲染一组数据/宏定义

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

bootstrap = Bootstrap(app)


if __name__ == "__main__":
    app.run(debug=True)
