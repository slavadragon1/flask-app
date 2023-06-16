# -*- coding: utf-8 -*-

from src import app


@app.route('/')
@app.route('/index')
def index():
    return 'hello world'