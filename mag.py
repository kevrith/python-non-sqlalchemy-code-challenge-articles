class Article:
    all = []  # Class variable to track all article instances
    
    def __init__(self, author, magazine, title):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        
        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        
        # Validate and set title
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters, inclusive")
        
        self._title = title
        self._author = author
        self._magazine = magazine
        
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Prevent changing title after instantiation
        if hasattr(self, '_title'):
            raise Exception("Title cannot be changed after instantiation")
        self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        # Validate author type
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        # Validate magazine type
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._magazine = value
  
class Author:
    def __init__(self, name):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")
        
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Prevent changing name after instantiation
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed after instantiation")
        self._name = value
    
    def articles(self):
        """Returns a list of all articles the author has written"""
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        """Returns a unique list of magazines the author has contributed to"""
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        """Creates and returns a new Article instance"""
        return Article(self, magazine, title)
    
    def topic_areas(self):
        """Returns a unique list of categories of magazines the author has contributed to"""
        articles = self.articles()
        if not articles:
            return None
        return list(set([article.magazine.category for article in articles]))