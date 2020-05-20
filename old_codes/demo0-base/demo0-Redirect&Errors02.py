from flask import Flask, redirect, url_for, render_template, request, abort
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('Redirect&Errors_login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   print('request:%s' % request)
   if request.method == 'POST': 
      if request.form['nm'] == 'admin':
         return redirect(url_for('success'))
      else:
         abort(401)
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return '<html>logged in successfully</html>'
	
if __name__ == '__main__':
       app.run(host='0.0.0.0',debug = True)