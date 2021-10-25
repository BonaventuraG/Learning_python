
from creare_obj_2 import creaobj
from classe import provaobj
from classe2 import class2 

cl_upp=creaobj()
print('instance upp= ', cl_upp.cl1.instance)
cl1=provaobj()
print('instance cl1= ', cl1.instance)
cl1.var[0]=4


print('var upp= ', cl_upp.cl1.var,' ',hex(id(cl_upp.cl1.var)))
print('var cl1= ', cl1.var,' ',hex(id(cl1.var)))

print('var3 upp= ', cl_upp.cl1.var3,' ',hex(id(cl_upp.cl1.var3)))
print('var3 cl1= ', cl1.var3,' ',hex(id(cl1.var3)))

print('var2 upp= ', cl_upp.cl1.var2,' ',hex(id(cl_upp.cl1.var2))) #questa punta ad una variabile creata fuori da instance
print('var2 cl1= ', cl1.var2,' ',hex(id(cl1.var2)))

print('upp id= ',hex(id(cl_upp.cl1)))  #gli oggetti della classe provaobj sono diversi, ma poi puntano allo stesso oggetto della classe InProva (instance è lo stesso)
print('cl1 id= ',hex(id(cl1)))

print("*****************************************")

cl1.var2=4 #questa ora punta ad una variabile creata fuori da instance
print(cl1.var2, id(cl1.var2))

obj2=class2()
cl_upp.passa_obj(obj2)

print(id(obj2.nonmut),id(obj2))
print(id(cl_upp.obj2.nonmut), id(cl_upp.obj2))
print()

obj2.nonmut=100

print(id(obj2.nonmut),obj2.nonmut, id(obj2))
print(id(cl_upp.obj22.nonmut),cl_upp.obj22.nonmut, id(cl_upp.obj22))
print(id(cl_upp.obj2.nonmut),cl_upp.obj2.nonmut, id(cl_upp.obj2))

print()










