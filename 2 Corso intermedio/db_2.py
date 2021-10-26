from book import Book
import booksSDK

booksSDK.delete_duplicates() # funziona!!!
#booksSDK.delete_book_by_title("Il vecchio e il mare")
book=Book("Il vecchio e il mare", 88)
#print(booksSDK.add_book(book))
print()
print(booksSDK.get_books())
print()
print(booksSDK.get_bookobj_list())  
# essendo oggetti book ritornano stringhe secondo il 
# metodo __str__ perchè è stato fatto overriding sul 
# metodo __repr__ 
print()

print(booksSDK.get_book_by_title('La Gabbianella e il Gatto'))
print(booksSDK.get_bookobj_by_title('La Gabbianella e il Gatto'))

