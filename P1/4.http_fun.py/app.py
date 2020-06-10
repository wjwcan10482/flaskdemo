from flask import request,Flask
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'log in'
    else:
        return 'log in info'

app.run()