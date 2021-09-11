from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message='This is your favorite News Application'
    return render_template('index.html',message = message)

@app.route('/article/<article_id>')
def article(article_id)
     '''
    View arrticle page function that returns the movie details page and its data
    '''
    return render_template('article.html',id = article_id)
