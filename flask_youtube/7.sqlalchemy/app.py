from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__) 
bootstrap=Bootstrap(app)
db=SQLAlchemy(app)

app.config.from_object(Config)

@app.route('/')
def index():
    paragraphs= [
        'Section 1',
        'Section 2',
        'Section 3',
    ]
    return render_template('index.html',title='Home',data=paragraphs)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)