
from . import main
from flask import render_template
from ..request import sources, headlines, articles

@main.route('/')
def homepage():
    news_sources= sources()
    trending_article = headlines()
    return render_template("index.html", news_sources=news_sources, trending_article=trending_article)

@main.route('/articles/<id>')
def all_articles(id):
    article_source = articles(id)
    return render_template("articles.html", article_source=article_source)
