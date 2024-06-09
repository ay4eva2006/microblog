from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form vvalidate_on_submit():

        return redirect(url_for('index'))
