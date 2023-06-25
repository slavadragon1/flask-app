# -*- coding: utf-8 -*-

from src import app, conn, cur
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
        cur.execute(f"INSERT INTO public.user (username, password) values ('{form.username.data}', '{form.password.data}')")
        conn.commit()
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/db', methods=['POST', 'GET'])
def test_db():
    cur.execute("SELECT * FROM public.user")
    print(cur.fetchall())
    return 'hi!'

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)