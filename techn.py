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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
