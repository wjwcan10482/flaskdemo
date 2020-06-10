from flask import request,Flask,make_response,render_template

app = Flask(__name__)
@app.route('/user/<username>')
def index(username):
    resp = make_response(render_template('index.html',username=username))
    resp.set_cookie('username', 'the username')
    return resp
app.run()