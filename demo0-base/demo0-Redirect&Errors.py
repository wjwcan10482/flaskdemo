from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('Redirect&Errors_login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   print('request:%s' % request)
   if request.method == 'POST' and request.form['nm'] == 'admin':
     return redirect(url_for('success'))
   return redirect(url_for('index'))

@app.route('/success')
def success():
   return '<html>logged in successfully</html>'
	
if __name__ == '__main__':
       app.run(host='0.0.0.0',debug = True)