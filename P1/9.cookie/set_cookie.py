from flask import request,Flask

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    return "Cookie is %s" % username

app.run()