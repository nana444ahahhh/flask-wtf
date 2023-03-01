import flask
from flask import render_template
from flask import Flask
import json
import os

app = Flask(__name__)
from http.server import HTTPServer, CGIHTTPRequestHandler


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
