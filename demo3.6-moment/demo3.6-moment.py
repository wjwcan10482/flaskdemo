from flask_moment import Moment
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


if __name__ == "__main__":
    app.run(debug=True)