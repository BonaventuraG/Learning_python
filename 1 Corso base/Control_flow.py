###Control flow

##Booleans

vero= True
falso= False

age=15
can_drink= age>20

print(can_drink)

#_________________________________________
## If statement
print("->",end=" ")

age=int(input())

if age>20:
    print("welcome to the alchool party")
    if age==21:
        print("Is it your first drink?")
#l'indentazione in python è funzionale
    if age>65:
        print("Hi, old pal")
else:
    print("go away")

print("see you next time")

#_________________________________________
## IF with boolean
bool_1=True
if bool_1:
    print("vero")
else:
    print("falso")

#__________________________________________
## OR, NOT operator

name="Bonaventura"

if name=="Bonaventura" or name=="Brunello":
    print("welcome to your PC")
else:
    print("you're not allowed")

bool_2=False
if bool_2 or print("It is false"): #non dà errore. 
    #Se la prima condizione è falsa, passa oltre e invoca la funzione posta dopo or 
    # (se la funzione non restituisce un booleano lascia il valore a falso)
    print("It is true")






