from . import main
from flask import render_template
from ..request import sources, headlines, articles

@main.route('/')
def index():
    news_sources= sources()
    trending_article = headlines()
    return render_template("index.html", news_sources=news_sources,headlines=headlines,trending_article=trending_article)

@main.route('/articles/<id>')
def articles(id):
    article_source = articles(id)
    return render_template("articles.html", article_source=article_source,id=id)
