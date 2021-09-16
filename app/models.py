class Sources:
    '''
    Article class to define source objects
    '''
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Headlines:
    '''
    Article Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,description,url,image,url_to_image,title):
        self.author = author
        self.description = description
        self.url = url
        self.image = image
        self.url_to_image = url_to_image
        self.title = title

class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,title,author,description,image,url,published_at):
       self.title = title
       self.author = author
       self.description = description
       self.image = image
       self.url = url
       self.published_at = published_at
class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,description,url,title):
        self.author = author
        self.description = description
        self.url = url
        self.title = title
