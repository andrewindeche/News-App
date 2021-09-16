import urllib.request,json
from .models import Article,Category,Sources,Headlines
from newsapi import NewsApiClient

api_key = None
source_url = None
newsapi = None
cat_url= None

def configure_request(app):
    global api_key,source_url, newsapi,cat_url
    api_key = app.config['API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    newsapi = NewsApiClient(api_key=api_key)
    cat_url=app.config['CAT_API_URL']

def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results
def articles(id):
    '''
    function that gets all english news sources in a list
    '''
    source_url = url.format(source_id, key)
    with urllib.request.urlopen(source_url) as url:
        result = url.read()
        response = json.loads(result)

        article_results = []

        if response['articles']:
            source_data_list = response['articles']
            article_results = get_data(source_data_list)
    return article_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results
def headlines():
    '''
    function that gets all english news sources in a list
    '''
    res = newsapi.get_top_headlines(language='en', page_size='10', sources='cnn')
    res_list =  res['articles']
    trending = []
    for item in res_list:
        top_article = Headlines(item['title'], item['urlToImage'], item['url'])
        trending.append(top_article)

    return trending

def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = cat_url.format(cat_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results
