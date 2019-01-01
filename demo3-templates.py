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
    return render_template('user_bootstrap.html', name=name)

# 3.1.2 变量->占位符->告诉jinjia2模板引擎，这个占位符的值从渲染模板时使用的数据中获取。
# 3.1.3 控制结构
# 3.1.4


bootstrap = Bootstrap(app)


if __name__ == "__main__":
    app.run(debug=True)
