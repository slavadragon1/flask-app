# -*- coding: utf-8 -*-

from src import app
from flask import render_template, url_for, redirect, flash
from src.forms import LoginForm
from flask_login import current_user, login_user


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

