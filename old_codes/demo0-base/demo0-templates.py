from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return '<html><body><h1>' + 'Hello World' + '</h1></body></html>'
    return render_template('hello.html')

@app.route('/user/<name>')
def user(name):
    # return '<html><body><h1>' + 'Hello World' + '</h1></body></html>'
    return render_template('user.html', name=name)


@app.route('/result/')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)