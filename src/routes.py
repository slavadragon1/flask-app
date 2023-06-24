# -*- coding: utf-8 -*-

from src import app
from flask import render_template, url_for, redirect, flash
from flask_socketio import SocketIO, emit
from src.forms import LoginForm

socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)



@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)