from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Ayobami"}
    posts = [
        {
            'author': {"username": "John"},
            'body': 'Beautiful day in Nigeria'
        },
        {
            'author': {'username': 'Esther'},
            'body': 'The Funmilayo Ransome kuti movie is so great!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
