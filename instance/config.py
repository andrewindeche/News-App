import os

class Config:
API_KEY = '6923221c2b374f8bbb9e30c6e2cbcfd1'
NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

class ProductionConfig(Config):
    '''
    '''
    pass


class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

config_options = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
