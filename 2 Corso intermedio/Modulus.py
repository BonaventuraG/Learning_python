# from 2.37.25 to

#>>>>>>>>>>>>>>MODULUS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# a module is a python file

import random

print(random)

print(type(random))

print(random.randint(0,10))


#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## From module import 

from random import randint


print(randint(0,10)) #avendo importato esplicitamente questo metodo, è possibile ora chiamarlo direttamente

'''from json import * '''
# in questo modo si importano esplicitamente tutti i metodi di json. Attenzione ai conflitti fra simboli

#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## Creating a Module 
print("CREA UN MODULO")
import my_module

'''
def my_method(list,list2,var):
    print(var,end=' ')
    var+=1
    print(var)
    list.append(var)
    list2=[0,0,0]
    print(id(list2))
    return 0
'''
list1=[0,1,2,3]
list2=[2,2,2]
var=3

print(id(list1),id(list2),id(var))

print(my_module.my_method(list1,list2,var))

print(list1,id(list1),list2,id(list2),var,id(var))
#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## Sys module

import sys

print(sys.path)

#sys.path.append('\Users\Bonaventura\my_directory)




