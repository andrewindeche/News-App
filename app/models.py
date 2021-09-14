class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,author,title):
        self.author = author
        self.headline = headline
        self.description = description
        self.images = images
        self.time = time
        self.url = url

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
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
