import urllib.request,json
from .models import Article,Sources,Headlines

api_key = None
base_url = None


key = None
url = None
newsapi = None

def configure_request(app):
    global key, url, newsapi
    key = app.config['API_KEY']
    url = app.config['SOURCE_URL']
    newsapi = NewsApiClient(api_key=key)


def sources():
    '''
    function that gets all english nes sources in a list
    '''
    data = newsapi.get_sources(language='en',country='ca')
    data_list = data['sources']
    source_list=[]
    for item in data_list:
        new_source = Sources(item['id'], item['name'])
        source_list.append(new_source)

    return source_list

def headlines():
    '''
    function that gets all english nes sources in a list
    '''
    res = newsapi.get_top_headlines(language='en', page_size=6, sources='cnn')
    res_list =  res['articles']
    trending = []
    for item in res_list:
        top_article = Headlines(item['title'], item['urlToImage'], item['url'])
        trending.append(top_article)

    return trending


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

def get_data(source_dict):
    '''
    function to get article list
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
