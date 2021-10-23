#from 44.31 to 2.00.11

#>>>>>>>>>>> INSERT & REMOVE <<<<<<<<<<<

workdays=['Lunedì','martedì','mercoledì','giovedì','sabato']

workdays.insert(4,'venerdì')
print(workdays, id(workdays))

settimana=workdays[:] #shallow copy
settimana2=workdays[:] #shallow copy

workdays.remove('sabato')
print(workdays, id(workdays))

print('\n>>>>>>>>>>>  settimana', id(settimana))
del settimana[5]  #modo simile per rimuovere un oggetto dalla lista (questa volta per indice)
print(settimana, id(settimana))

print('\n>>>>>>>>>>>  settimana2', id(settimana2))
popped=settimana2.pop(5) #altro modo, ma che conserva l'elemento eliminato
print(settimana2, id(settimana2))
print(popped,'\n')

list2= ['a','b','c','d','e','f','g']
del list2[list2.index('c'):list2.index('c')+3]   #slicing
print(list2)

list2[:]=[0,0,0,3,0,0,4,0,5,0]  #list2 mantiene il suo indirizzo ma il suo contenuto è completamente sostituito
list3=list2[:]                  #shallow copy

for item in list2:
    if item == 0:
        list2.remove(item)

print(list2) # non funziona perchè nel rimuovere un oggetto si disastrano gli indici della lista

for item in list3[:]:
    if item == 0:
        list3.remove(item)

print(list3) #  funziona perchè il for scorre gli elementi su una copia della lista


#_________________________________________________________________________________________________
#*************************************************************************************************
## Reverse and change order

data=[0,1,2,3,4,[1,2,3]]
data.reverse()
print('reversed ', data)

zero=0
uno=1
zero,uno=uno,zero 
print(zero,uno)

 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Manual reverse
data=['a','b','c','d','e','f','g','h','i']
data2=data[:]

index=1
data[index], data[-index-1] = data[-index-1], data[index]  #esempio di un passo del for
print(data)

for index in range(len(data2)//2):
    data2[index], data2[-index-1] = data2[-index-1], data2[index]

print(data2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Secondo modo
data_reversed=[]

for item in reversed(data2): #reversed non cambia il posto, ma fa in modo che il for parta dalla parte opposta
    data_reversed.append(item)

print(data_reversed)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Miglior modo manuale

print(data_reversed[::2])  #slicing
print(data_reversed[::-1]) #così stampa solo al contrario

data_reversed[:]=data_reversed[::-1]
print(data_reversed) #così la lista viene effettivamente invertita

#_________________________________________________________________________________________________
#*************************************************************************************************
## Sort Lists

print(id(workdays))
workdays=['Lunedì','Martedì','Mercoledì','Giovedì','Venerdì'] #riassegnazione del simbolo ad un oggetto: cambia l'id
print(id(workdays))
print('sorted function',sorted(workdays)) #sorted crea una copia
print(id(workdays),workdays) #l'originale non è cambiato
workdays.sort()
print(id(workdays))  #nessuno dei due metodi l'id dell'oggetto lista
print(workdays)      # ma sort agisce sull'oggetto originale

data=[-1 , 32, 4, 56, 33, 3, 2]

print(sorted(data, reverse=True)) #si può anche usare .sort() e poi .reverse()

strings=['a','A','abc', 'ABC', 'aBc', 'aBC', 'Abc']
strings.sort()
print(strings)

strings=['a','A','abc', 'ABC', 'aBc', 'aBC', 'Abc']
strings.sort(key=str.lower)
print(strings)

strings[:]=['a','aaaa','aa','AAA','Hello','b','a']

strings.sort(key=len)
print(strings)

data=[1, 32, 4, 56, 31, 3, 2, 5, 11, 101]
data.sort(key=str) #ordinare numeri come se fossero stringhe
print(data)

stuff=[True,23,10,77,0,'12','5','66',3.33,'3.14',5<0,0]
stuff.sort(key=float)
print(stuff)

#_________________________________________________________________________________________________
#*************************************************************************************************
## Split strings

msg="Alta sui naufragi Dai belvedere delle torri"
words=msg.split()
print(words)
print(msg) #la stringa non viene cancellata (nè modificata)

msg="China e distante- sugli elementi del disastro"
words=msg.split('- ')
print(words)

msg='''Dalle cose che accadono al di sopra delle parole
Celebrative del nulla
Lungo un facile vento
Di sazietà di impunità'''

words=msg.split('\n')
print(words)

#_________________________________________________________________________________________________
#*************************************************************************************************
## User input (boring)

#print('insert a string')
#myin=input()

#list4=myin.split
#print(list4)

