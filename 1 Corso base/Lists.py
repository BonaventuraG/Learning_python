### Lists: a collection of things

ages =[12 , 2, 36]
people = ["io" , "tu"] 
stuff = ["aeiou", 1, 2, 58, "xyz", 1.23, ["b", 2, "c"]]

print(stuff, id(stuff))

#____________________________________
## Lists are mutable

stuff[0]="abc"
print(stuff, id(stuff))
#the string "aeiou" was destroied and replaced,
#  and the list changed

print(len(stuff))
# la lista interna conta come un solo elemento

#____________________________________________
## copy a list (shallow copy) crea un oggetto indipendente eccetto che per le sottoliste
print('\nshallow copy\n')

print(stuff[1:4])
copy_1 = stuff[:] #this way they are different objects
copy_1[0] = "areereire" 
print(stuff[0], copy_1[0])

#copy=stuff crei solo un alias per stuff, ma l'oggetto è lo stesso

copy_2 = stuff.copy() # .copy è un metodo dell'oggetto lista
#altro modo per copiare

#______________________________________________
## nested list
print('\nnested list\n')

# stuff = ["aeiou", 1, 2, 58, "xyz", 1.23, ["b", 2, "c"]]

print(stuff[6])
print(stuff[6][2])

#_______________________________________________
## deep copying
print('\ndeep copying\n')
print(stuff, copy_2)
print(id(stuff), id(copy_2))

copy_2[6][0]="k"

print(stuff, copy_2) 
#la modifica è stata effettuata ad entrambi gli oggetti!!!
print(id(stuff),id(copy_2))

#le liste interne non vengono copiate elemento 
# per elemento, ma vengoo creati degli alias. 
# se cambia un elemento della sottolista, la 
# sottolista non ha copia -->

print('indirizzi sottoliste')
print(id(stuff[6]),id(copy_2[6]),'sono uguali')

#con la deepcopy si creano oggetti completamente indipendenti
import copy

deepcopy_2= copy.deepcopy(stuff)
print('\ndeepcopy: ora gli indirizzi delle sottolista sono diversi')
print(id(stuff[6]))
print(id(deepcopy_2[6]))

#________________________________________________________
## Combining lists
print('combining list')
print(copy_1)
print(id(copy_1))
copy_1 = copy_1 + ["accio"]
print(copy_1)
print(id(copy_1))
copy_1.append("oneino")
print(copy_1)
print(id(copy_1))

