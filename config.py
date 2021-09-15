import os

class Config:
    '''
    General configuration parent class
    '''
    pass
    SOURCE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


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
    'prod': ProductionConfig
}
