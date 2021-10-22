
from creare_obj_2 import creaobj
from classe import provaobj

cl_upp=creaobj()
print('instance upp= ', cl_upp.cl1.instance)
cl1=provaobj()
print('instance cl1= ', cl1.instance)
cl1.var[0]=4


print('var upp= ', cl_upp.cl1.var,' ',hex(id(cl_upp.cl1.var)))
print('var cl1= ', cl1.var,' ',hex(id(cl1.var)))

print('var3 upp= ', cl_upp.cl1.var3,' ',hex(id(cl_upp.cl1.var3)))
print('var3 cl1= ', cl1.var3,' ',hex(id(cl1.var3)))

print('var2 upp= ', cl_upp.cl1.var2,' ',hex(id(cl_upp.cl1.var2)))
print('var2 cl1= ', cl1.var2,' ',hex(id(cl1.var2)))

print('upp id= ',hex(id(cl_upp.cl1)))
print('cl1 id= ',hex(id(cl1)))










