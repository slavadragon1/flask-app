# -*- coding: utf-8 -*-

from src import app
from flask import render_template, url_for
from flask_socketio import SocketIO, emit
from forms import LoginForm

socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)