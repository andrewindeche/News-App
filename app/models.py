class Sources:
    '''
    Article class to define source objects
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Headlines:
    '''
    Article Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,description,time,url,url_to_imageImage,image,title):
        self.author = author
        self.description = description
        self.time= time
        self.url = url
        self.url_to_image= url_to_image
        self.image = image
        self.title = title

class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,title,author,description,image,url,time):
       self.title = title
       self.author = author
       self.description = description
       self.image = image
       self.url = url
       self.time = time
class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,description,url,title):
        self.author = author
        self.description = description
        self.url = url
        self.title = title