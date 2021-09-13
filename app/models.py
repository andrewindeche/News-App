from . import db
class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,author,title,description,images,time,shares_Total,url):
        self.author = author
        self.headline = headline
        self.description = description
        self.images = images
        self.time = time
        self.url = url
class Category:
    '''
    Article class to define Category Objects
    '''
    def __init__(self,author,title,description,images,time):
        self.author = author
        self.headline = headline
        self.description = description
        self.images = images
        self.time = time

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
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
        
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
