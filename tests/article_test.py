import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Jinia Shawdagor','Cointelegraph','El Salvador’s Bitcoin detractors: Opposition mounts despite crypto rollout - Cointelegraph','2021-09-11T05:07:00Z','https://images.cointelegraph.com/images/1200_aHR0cHM6Ly9zMy5jb2ludGVsZWdyYXBoLmNvbS91cGxvYWRzLzIwMjEtMDkvMzczZjNkMjMtMTExMS00NTEwLWEwNDgtZWQyNmMwN2JhMjhmLmpwZw==.jpg','https://cointelegraph.com/news/el-salvador-s-bitcoin-detractors-opposition-mounts-despite-crypto-rollout')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

        return app


if __name__ == '__main__':
    unittest.main()
