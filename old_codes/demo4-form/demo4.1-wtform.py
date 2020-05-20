from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask import Flask, render_template
from flask import request
app = Flask(__name__)


#http://docs.jinkan.org/docs/flask/patterns/wtforms.html


# 定义表单类
class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


# 路由函数
@app.route('/register', methods=['GET', 'POST'])

# 视图函数函数中处理表单
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
        # register.html 把表单渲染成html
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)