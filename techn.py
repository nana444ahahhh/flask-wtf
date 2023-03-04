import flask
from flask import render_template
from flask import Flask
import json
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect

app = Flask(__name__)
from http.server import HTTPServer, CGIHTTPRequestHandler
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username1 = StringField('id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/news')
def news():
    return render_template('line.html', title="ewf")


@app.route('/base')
def base():
    return render_template('base.html', title="ewf", number=6)


@app.route('/work/<workk>')
def work(workk):
    print(os.getcwd())
    if 'инженер' in workk:
        return render_template('works.html', wurk="инжтех", image='/static/p2.jpg')
    else:
        return render_template('works.html', wurk="научные", image='/static/p1.jpg')


@app.route('/list_prof/<dependant>')
def list_prof(dependant):
    param = {}
    param["list"] = ['дворник', 'уборщик', 'сантехник', 'специалист по атомной физике', 'врач', 'инженер',
                     'программист', 'исследователь организмов', 'боксер', 'строитель', 'тестировщик']
    if "ol" == dependant:
        factor = 1
    elif "ul" == dependant:
        factor = 2
    else:
        factor = 3
    param["list_type"] = factor
    print(factor)
    return render_template('list.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {"title": "ответ", "surname": "Ридналов", "name": "Иван", "education": "среднее",
             "profession": "специалист по починке техники", "sex": "мужчина",
             "motivation": "зарабатывает на жизнь своим детям и жене", "готовы остаться на марсе? ": True}
    return render_template('answerer.html', **param)
@app.route('/distribution')
def distribution():
    return render_template('rooms_sort.html',
                           people=["Майкл Джордан", "Майкл Джексон", "Александр Пушкин", "Лев Толстой",
                                   "Эрнест Хэмингуэй", "Леонардо Дикаприо"])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
