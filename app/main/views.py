from . import main
from flask import render_template,url_for
from .request import get_source,get_category,headlines,articles

@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    global source
    source = get_source()
    headlines = headlines()
    trending_article = trending_article()
    return render_template("index.html",sources=source,headlines=headlines,trending_article=trending_article)

@main.route('/articles/<id>')
def articles(id):
    article_source = articles(id)
    return render_template("articles.html",article_source=article_source,id=id)

@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)
