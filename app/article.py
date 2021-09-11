class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://images.cointelegraph.com/images/1200_aHR0cHM6Ly9zMy5jb2ludGVsZWdyYXBoLmNvbS91cGxvYWRzLzIwMjEtMDkvMzczZjNkMjMtMTExMS00NTEwLWEwNDgtZWQyNmMwN2JhMjhmLmpwZw==.jpg'+ poster
        self.views_Total = views_total
        self.shares_Total = shares_Total
