from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__) 
app.config.from_object(Config)

bootstrap=Bootstrap(app)
db=SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)


# from models import User
# User.query.all()