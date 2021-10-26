import sqlite3
from book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()


c=cursor()
c.execute('''CREATE TABLE IF NOT EXISTS 
            books (title TEXT, pages INTEGER)''')
c.connection.close()


def add_book(book:Book):
    c=cursor()

    with c.connection:
        c.execute('INSERT INTO books VALUES (?,?)',(book.title, book.pages))
        rowid=c.lastrowid
    c.connection.close()
    return rowid


def get_books():
    c=cursor()
    with c.connection:
        c.execute('SELECT * FROM books')
        books=c.fetchall()
    c.connection.close()
    return books


def add_new_book(book:Book):
    books=get_books()
    for b_tuple in books:
        if b_tuple[0]==book.title:
            return -1
    
    return add_book(book)


def get_bookobj_list(): #crea una lista di oggetti libro
    c=cursor()
    booklist = []
    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            booklist.append(Book(book[0],book[1]))
    c.connection.close()
    return booklist

def delete_book_by_title(title):
    c=cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=?',(title,))
    c.connection.close()    
    return


def delete_duplicates(): 
    books=get_books()
    c=cursor()
    with c.connection:
        for i in range(len(books)-1):
            for j in range(i+1,len(books)):
                if books[i]==books[j] and i!=j:
                    btitle=str(books[j][0])
                    c.execute('''SELECT ROWID FROM books WHERE title=?''',(btitle,))
                    data=c.fetchone() #mi ritorna una tupla (n°,) con il numero di riga del primo record che trova
                    rowid=data[0]
                    #c.execute('DELETE FROM books WHERE title=?',(btitle,)) #cancella tutti i record con quel titolo
                    c.execute('DELETE FROM books WHERE rowid=?',(rowid,)) 
                    
                    break
    c.connection.close()    
    return


def get_book_by_title(title:str):
    c=cursor()
    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?',(title,))
        book=c.fetchone()
    c.connection.close()
    return book


def get_bookobj_by_title(title:str):
    c=cursor()
    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?',(title,))
        data = c.fetchone()
    c.connection.close()
    
    if not data:
       return None

    return Book(data[0],data[1]) 
