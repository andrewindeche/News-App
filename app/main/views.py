from . import main
from flask import render_template,url_for,request,redirect
from ..request import article_source,get_category,get_headlines

@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    headlines = get_headlines()
    return render_template("index.html",headlines = headlines)

@main.route('/articles/<id>')
def articles(id):
    article_source = articles(id)
    return render_template("articles.html",article=article,id=id)

@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)
