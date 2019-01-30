from flask import Flask, render_template
from wtforms import TextField
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fuckoff guess'
class NameForm(Form):
    name=StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST']) 
def index(): 
    name = None 
    form = NameForm() 
    if form.validate_on_submit(): 
        name = form.name.data 
        form.name.data = '' 
    return render_template('index.html', form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True)