import os

class Config:
    '''
    General configuration of parent class
    '''
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'


class ProductionConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevelopmentConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig
}
