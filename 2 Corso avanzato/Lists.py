# LISTE 
# da min 3.40 to 30.06
# 
# le liste sono oggetti. Ci sono metodi

healthy =['pineapple','tomatoes','vegetables','fruit']

healthy.append('water')

print(healthy)
print('fruit is in healty?'+'fruit' in healthy)

backpack =['pizza', 'nutella', 'pineapple', 'beer','cocacola']
print(id(backpack),' ',backpack)
backpack.remove('pizza')
print("->backpack.remove('pizza')<-")
print(id(backpack),' ',backpack)

#________________________________________
## List comprehension
print('\nlist comprehension\n')

print(id(backpack))
backpack =[item for item in backpack if item in healthy]
#in questo modo la lista è stata distrutta e ricreata
print(backpack)
print(id(backpack))

backpack.append(['cake','candies','fruit'])
print(backpack)
backpack[:] =[item.upper() for item in backpack if item in healthy]
#con i : la lista è stata modificata senza essere distrutta
print(id(backpack))
print(backpack)

addings=['water','broccoli','water']
for item in addings:
    backpack.append(item)
#anche in questo modo la lista è stata solo aggiornata ma non distrutta
print(id(backpack))
print(backpack)

squares = [i**2 for i in range(10) if i%2==0]
print(squares)

#_____________________________________________
## len() and count

print('\nlen and count\n')

print(len(backpack), ' ', backpack[len(backpack)-1])

print(backpack.count('water')) #how many water in backpack

