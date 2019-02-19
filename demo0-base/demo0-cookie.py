from flask import Flask, render_template, request
import time
from datetime import datetime
from flask_moment import Moment
app = Flask(__name__)
moment = Moment(app)
@app.route('/')
def index():
   return render_template('cookie_index.html')

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      # resp = make_response(render_template('readcookie.html'))
      resp = app.make_response(render_template('cookie_read.html'))
      resp.set_cookie('userID', user, expires=time.time()+10)
   return resp


if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)   