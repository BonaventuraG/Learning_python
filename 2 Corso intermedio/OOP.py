#from 3.58.15 to 4.48.50

class Book():

    favorites = []

    def __init__(self, title, pages): #initializer or "constructor" (similar to other language constractor)
        self.title=title
        self.pages= pages

    def is_long(self):
        if self.pages>200:
            return True
        return False

    def __str__(self):  # overriding
        return f"{self.title} is {self.pages} long "

    def __eq__(self, other): # overriding
        if self.title == other.title and self.pages==other.pages:
            return True
        return False

    __hash__= None #the objects are not hashable. Non possono essere usati in set nè come key di dictionary (agli elementi di set e alle key di dictionaries viene applicato il metodo hash per confrontarli velocemente)
                    #se un oggetto è mutabile, è bene che sia unhashable

    
    #def __hash__(self):     # override di hash
        #return hash(self.title) ^ hash(self.pages)
    

book=Book("LOTR", 950) #book object
book2=Book("L'isola del tesoro",250) #book object

print(book.title, book.is_long())
print(book2.title, book.is_long())
print(book) # stampa l'indirizzo dell'oggetto: favorites è una lista di oggetti.
#a meno che non si sia fatto l'overriding (line 14)

Book.favorites.append(book) 

print(Book.favorites)  #stampa l'indirizzo dell'oggetto

for b in Book.favorites:
    print(b.title, b.pages)

print (book==book2) #verifica che siano lo stesso oggetto (lo stesso indirizzo di memoria) a meno che non si faccia overriding


'''#________________________________________________________________________________________________________
#********************************************************************************************************
## Objects id''' #vedi anche cartella oggetti


book3=Book("L'isola del tesoro",250) #book3 è uguale (secondo l'overriding di __eq__) a book2, ma non sono lo stesso oggetto

book4=book3 #book3 e book4 sono lo stesso oggetto

print((book2 == book3), (id(book2)==id(book3)), (book2 is book3)) #gli ultimi due comandi sono equivalenti (legge l'id), mentre il primo dipende da __eq__
print(book4 == book3, (id(book4)==id(book3)),(book4 is book3))

def do_something(book, book2): #essendo gli oggetti mutabili, ed essendo passati gli indirizzi, le funzioni modificano gli oggetti originali
    book.title= "something else"
    book2= Book("new book",55) #viene creato un nuovo oggetto che non ha nulla a che fare con l'oggetto passato
    print(id(book),id(book2))

book5 = book3
print(id(book3),id(book4),id(book5))

do_something(book3, book5)

print(id(book3),id(book4),id(book5))
print(book3,book4,book5)
#l'id di book3 e book 4 e 5 (che sono solo alias) non cambiano


'''#________________________________________________________________________________________________________
#********************************************************************************************************
## FILE I/O and exceptions'''

'''file = open("input.txt",'w')
file.write('I racconti ritrovati\t123\n')
file.write('i racconti incompiuti\t133\n')
file.close'''

try:
    file=open('input.txt','r')
except FileNotFoundError as e:
    print('cannot find file')
except Exception as e:
    print(e)
    print('somthing went wrong')
finally:
    print('resources relased')
    

data=file.read().split('\n')
file.close

print(data)

book_data=data[2].split('\t')
print(book_data)
book6=Book(book_data[0],book_data[1])

print(book6)


with open('input.txt') as file: #un modo per gestire le risorse in modo compatto ed automatizzare la chiusura delle risorse
    if not file.closed:
        print('open')

if file.closed:
    print('closed')

try: #un modo per usare il with mantenendo il catch dell'errore sull'open
    file=open('input.txt')
except OSError:
    print('cannot open')
else:
    with file:
        #code to parse
        print('parsed')

