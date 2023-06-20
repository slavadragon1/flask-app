# -*- coding: utf-8 -*-

from src import app
from flask import render_template, url_for
from flask_socketio import SocketIO, emit

socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Slava'}
    return render_template('index.html', user = user )

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)