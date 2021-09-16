import unittest
from app.models import Headlines

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.top_article = Headlines('cnn-international','https://www.google.com/img','https://www.google.com')

    def test_source(self):
        '''
        test for creation of a new instance
        '''
        self.assertTrue(isinstance(self.top_article, Headlines))

    def test_init(self):
        '''
        '''
        self.top_article.title = 'cnn-international'
        self.top_article.url_to_image='https://www.google.com/img'
        self.top_article.url='https://www.google.com'
