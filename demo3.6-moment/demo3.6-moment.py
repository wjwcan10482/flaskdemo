from flask_moment import Moment
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
moment = Moment(app)

@app.route('/')
#https://github.com/miguelgrinberg/Flask-Moment
def index():
    return render_template('index.html', current_time=datetime.utcnow())
    #datetime(1989,11,11))
    #current_time=datetime.utcnow())

if __name__ == "__main__":
    app.run(debug=True)