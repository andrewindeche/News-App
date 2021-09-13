import urllib.request,json
from .models import Article,Category,Sources,Headlines
from newsapi import NewsAPiClient

api_key = None
base_url = None
newsapi = None

def configure_request(app):
    global api_key,base_url,newsapi
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    newsapi = NewsApiClient(api_key=key)


def sources():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_sources_data)

        source_results = None

        if get_source_response['source']:
            source_results_list = get_sources_response['source']
            source_results = process_results(source_results_list)

    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def get_article(category):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['results']:
            article_results_list = get_article_response['results']
            article_results = process_results(article_results_list)
def headlines():
    '''
    Function that gets all english nes sources in a list
    '''
    res = newsapi.get_top_headlines(language='en', page_size=6, source='cnn')
    res_list =  res['articles']
    trending = []
    for item in res_list:
        top_article = Headline(item['title'], item['urlToImage'], item['url'])
        trending.append(top_article)

    return trending

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        author=article_item.get('author')
        headline = article_item.get('headline')
        description = article_item.get('description')
        images = article_item.get('images')
        url = article_item.get('url')


        if poster:
            article_object = article(id,author,headline,description,images,url)
            article_results.append(article_object)


    return article_results
