class Book():
    
    favs = [] #class property 

    def __init__(self, title, pages): #initializer or "constructor" (similar to other language constractor)
        self.title=title
        self.pages= pages

    def is_short(self):
        if self.pages<100:
            return True
        return False

    def __str__(self):  # overriding
        return f"{self.title} is {self.pages} pages long "

    def __eq__(self, other): # overriding
        if self.title == other.title and self.pages==other.pages:
            return True
        return False

    __hash__= None #the objects are not hashable. Non possono essere usati in set nè come key di dictionary (agli elementi di set e alle key di dictionaries viene applicato il metodo hash per confrontarli velocemente)
                    #se un oggetto è mutabile, è bene che sia unhashable
     
    def __repr__(self): #added to make list of items invoke str
        return self.__str__()