import urllib.request,json
from .models import Article,Sources,Headlines
from newsapi import NewsApiClient

api_key = None
source_url = None
newsapi = None

def configure_request(app):
    global api_key,source_url
    api_key = app.config['API_KEY']
    source_url = app.config['NEWS_API_BASE_URL']
    api = NewsApiClient(api_key=api_key)

def sources():
    '''
    function that gets all news sources in a list
    '''
    data = newsapi.get_source(language='en',country='ca')
    data_list = data['sources']
    source_list=[]
    for item in data_list:
        new_source = get_source(item['id'], item['author'])
        source_list.append(new_source)

    return source_list

def articles(source_id):
    '''
    function that gets all english news sources in a list
    '''
    source_url = url.format(source_id, key)
    with urllib.request.urlopen(source_url) as uri:
        result = uri.read()
        response = json.loads(result)

        article_results = []

        if response['articles']:
            source_data_list = response['articles']
            article_results = get_data(source_data_list)
    return article_results

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
    res = newsapi.get_top_headlines(language='en', page_size=6, sources='cnn')
    res_list =  res['articles']
    trending = []
    for item in res_list:
        top_article = Headline(item['title'], item['urlToImage'], item['url'])
        trending.append(top_article)

    return trending

def get_data(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    '''

    article_list = []
    for item in source_dict:
        title = item.get('title')
        author = item.get('author')
        description = item.get('description')
        url = item.get('url')
        url_to_image = item.get('urlToImage')
        published_at = item.get('publishedAt')

        if url_to_image and url:
            new_article = Articles(title, author, description, url, url_to_image, published_at)
            article_list.append(new_article)
    return article_list
