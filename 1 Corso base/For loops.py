###For loops

##with lists

list_1 = ["a", "b", "c", "d", "e","f"]

for element in list_1:
    print(element, end=" ")

print()

#________________________________________
## without lists (range è un oggetto iterablie)

for i in range(10): #da 0 to 10 escluso
    print(i,end=" ")

print()

for j in range(10,100,10): 
    print(j,end=" ")

print()
print(sum(range(4))) 
# =3!=6 perchè range esclude 
# l'estremo sinistro (4)

list_2= list(range(10))
print(list_2)

#________________________________________
## lists and range 

for z in range(len(list_1)):
    print (str(z+1) + ")", list_1[z],end=' ')
    if z<(len(list_1)-1):
        print('-',end=' ')
    else:
         print()

#________________________________________
## Brake

for z in range(len(list_1)):
    print (str(z+1) + ")", list_1[z],end=' ')
    if z==3:
        print('...eccetera')
        break
    elif z<(len(list_1)-1):
        print('-',end=' ')
    else:
         print()

for element in list_1:
    print(element, end=" ")
    if element=="c":
        print("ecc ecc ...")
        break
print()

#________________________________________
## Continue

for element in list_1:
    print(element, end="")
    if element=="c":
        print("??? ", end='')
        continue
    print('!!! ', end='')
print()

#____________________________________________
## Pass

for element in list_1:
    print(element, end="")
    if element=="c":
        print("??? ", end='')
        continue
    elif element=="d":
        pass # ancora da implementare
    print('!!! ', end='')
print()

#____________________________________________
## else (in loops)

for element in list_1:
    print(element, end="")
    if element=="c":
        print("??? ", end='')
        break
    print('!!! ', end='')
else:  #al contrario di prima, al break l'ultimo print non viene letto
    print()