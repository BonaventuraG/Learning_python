import booksSDK
from book import Book

#print a menu

def print_menu():
    print('''
    Choose an option

    1. print all books
    2. add a book
    3. update a book

    9. quit

    ''')
    return

while True:
    print_menu()
    response=int(input())
    if response == 1:
        print('print all books\n')
        print(booksSDK.get_books())
    elif response==2:
        print('add a book\n')
        print('input the book title')
        title=input()
        print('input the book number of pages')
        pages=int(input())

        newbook=Book(title, pages)
        booksSDK.add_new_book(newbook)
    elif response==3:
        print('update a book\n')
    
    elif response==9:
        break
    


