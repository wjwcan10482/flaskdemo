from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('registerj2.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("resultj2.html",result = result)


if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)