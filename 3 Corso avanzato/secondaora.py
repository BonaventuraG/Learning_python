'''______________________________________________________________________________________________________________________________'''
'''>>>>>>>>>>>>>>>>>THE UNDERSCORE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''

#_single
#__double
#__before
#after__
#__both__


'''_______________skipping (one before)__________________'''

for _ in range(5):   #la variabile "_" viene rilasciata immediatamente dopo l'uso
    print('hello')


#*## from now on we will use a class in the person.py file'''

from person import *

'''_____________weak private (_before)_______________'''

p= Person()
p.setName('Brian')
print('week private', p._name)
p._name='nooooo'
print('week private', p._name) #è più una convenzione che altro

'''___________strong private (__double before)________'''

#INTERNAL USE ONLY, avoid conflict in subclass
#tells python to rewrite the name (Mangling)

p= Person()
p.work()
#p.__think() #it does NOT work (__think è stata rinominata per python, quindi non si riesce ad accedervi)
c=Child()
#c.testDouble() #it does not work
c.contrasto()

'''_________________After (any number)_________________'''

class_ = Person() #used to avoid name conflicts
print(class_)

'''______Before and after (double da entrambi i lati)_____'''

#python non rinomina più (infatti __init__ può essere overrided)

p=Person()
p.__calling__()



'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
'''>>>>>>>>>>>>>>>>>>>>>DECORATORS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
print('\n'+'*'*20)
#even function (in python) are object

def test_decorator(func):
    print('before')
    func()
    print('after')

@test_decorator   #il decorator ha eseguito test_decorator inserendo doing_stuff come argomento
def do_stuff():
    print('doing stuff')

'''_____________real decorator____________________________'''
print()

def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner   #ritorna la reference all'oggetto funzione

@makeBold
def printName():
    print('Bonnie')

# se venisse lanciato così, makeBold verrebbe eseguita,
# ma nesuno farebbe eseguire inner. 

printName() 

#* Il decoratore è equivalente a scrivere prima di printName()
#? printname = makeBold(printname)
# in questo modo printname è stata modificata in makeBold che
# ritorna inner quando viene eseguita

'''_____________decorator with parameters____________________________'''
print()

def numcheck(func):
    def checkInt(o):
        if isinstance(o,int):
            if o==0:
                print('cannot divide by zero')
                return False
            return True
        print(o, 'is not a number')
        return False

    def inner(x,y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner

@numcheck
def divide(a,b):
    print(a/b)

divide(100,3)
divide(100,0)
divide(100,'cat')

'''_____________decorator chains____________________________'''
print()

def outline(func):
    def inner(*args, **kwargs):
        print('+'*20)
        func(*args,**kwargs)
        print('+'*20)
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print('args = ', args)
        print('kwargs = ', kwargs)
        for x in args:
            print('arg =', x)
        for k,v in kwargs.items():
            print('key =', k,'and value =', v)
    return inner

@outline
@list_items
def display(msg):
    print(msg)

display('hello world')


@outline
@list_items
def birthday(name='', age=0):
    print('Happy birthady', name, 'you are', age, 'years old')

birthday('Bonnie',33) #passa una tupla
birthday(name='Frank',age=30) #passa un dizionario

'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
'''>>>>>>>>>>>>>>>>>>>>>ITERATORS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
print('\n'+'*'*20)

t = (1,2,3,4)
for x in t:
    print(x, end=' ')
print('\n')

#lists, tuples, dictionaries, sets, strings

people=['Bruno', 'Are', 'Very']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) #stop iteration

'''_____________Iterable class____________________________'''
print()

import random

class Lotto:
    def __init__(self):
        self._max=5

    def __iter__(self):
        # yield statement suspend the function's execution
        # and sends a value back to the caller, but the 
        # function can be resumed where it is left off
        for _ in range(self._max):
            yield random.randrange(0,100)

    def setMax(self,value):
        self._max=value

print('-'*20)
lotto=Lotto()
lotto.setMax(10)

for x in lotto:
    print(x)

print('-'*20)