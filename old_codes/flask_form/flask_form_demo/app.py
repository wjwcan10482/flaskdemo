from form import LoginForm
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_bootstrap import Bootstrap
app=Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    if form.validate_on_submit():       
        username = form.username.data        
        flash('Welcome home %s' % username)
        return redirect(url_for('index'))
    return render_template('bootstrap.html',form=form)
app.secret_key='123456'
app.run()