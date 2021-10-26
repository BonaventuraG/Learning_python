'''#________________________________________________________________________________________________________
#********************************************************************************************************
## DATABASE'''

import sqlite3

conn=sqlite3.connect('example.db') #pass the name of a database or keep it in memory for testing
#conn=sqlite3.connect(':memory:') #pass the name of a database or keep it in memory for testing

print('connect done')

c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS 
            books (title TEXT, pages INTEGER)''')

c.execute(''' INSERT INTO books VALUES('LOTR',950)''')
conn.commit()


#c.execute(''' INSERT INTO books (title) 
#                VALUES('Il segno dei quattro')''')
#conn.commit() 

c.execute('''SELECT * FROM books''')
data=c.fetchall() #mi ritorna una lista di tuple
print(data)
print()

SHbooks= [('Uno studio in rosso',87),
        ('Il mastino dei baskerville', 103),
        ('Le avventure di Sherlock Holmes', 150)
        ]

#c.executemany('INSERT INTO books VALUES (?,?)',SHbooks)
#conn.commit()

#c.execute('''SELECT * FROM books''')
#data=c.fetchall() #mi ritorna una lista di tuple
#print(data)

c.execute('''SELECT * FROM books WHERE title="Uno studio in rosso"''')

#c.execute('''SELECT * FROM books''')
data=c.fetchall() #mi ritorna una lista di tuple
print(data)
print()

#c.execute('''DELETE FROM books WHERE title='Il segno dei quattro' ''')
#conn.commit()

c.execute('''SELECT * FROM books''') #select all
data=c.fetchall() #mi ritorna una lista di tuple
print(data)
print()

c.execute('''SELECT ROWID, title FROM books''')
data=c.fetchall() #mi ritorna una lista di tuple
print(data)
print()

c.execute('''SELECT ROWID FROM books WHERE title='LOTR' ''')
data=c.fetchone() #mi ritorna una tupla (n°,) con il numero di riga del primo record che trova
print(data)
print()

c.execute('''UPDATE books 
            SET title="Le pietre di Shannara" 
            WHERE rowid=13''')

conn.commit()

c.execute('''SELECT * FROM books''') #select all
data=c.fetchall() #mi ritorna una lista di tuple
print(data)
print()