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

import my_module

'''
def my_method():
    return 0
'''

print(my_module.my_method())

#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## Sys module

import sys

print(sys.path)

#sys.path.append('\Users\Bonaventura\my_directory)




