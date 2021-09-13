from flask import render_template,request,url_for
from . import main
from ..request import sources,article_source,get_article,headlines

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    source= sources()
    trending_article=headlines()
    return render_template('index.html',sources = sources,headlines = headlines)


@main.route('/article')
def article(id):
     '''
     View article page function that returns the news details page and its data
     '''
     article_source = article(id)
     return render_template('article.html',article_source=article_source)

@main.route("/favicon.ico")
def favicon():
    return "", 200
