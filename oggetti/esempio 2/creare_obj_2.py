from classe import provaobj
from classe2 import class2

class creaobj:

    def __init__(self):
        
        self.cl1=provaobj()
        self.cl1.var[0]=12
        self.cl1.var3[0]=1
        self.obj22=class2()

        print('****************************************')
        print("lista creobj= ",self.cl1.var, end=' ')
        print (hex(id(self.cl1.var)))
        print('elemento creobj= ', id(self.cl1.var[0]))

        self.cl1.var[0]=13
        print("lista creobj= ",self.cl1.var ,end=' ')
        print (hex(id(self.cl1.var)))
        print('elemento creobj= ', id(self.cl1.var[0]))

        print('id oggetto = ', hex(id(self.cl1)) )
        print('id var2 = ', hex(id(self.cl1.var2)))
        self.cl1.var2=99   # var2 non è modificabile. Quindi la self.cl1.var2=99 viene creata fuori dall'istanza InProva ma dentro l'oggetto provaobj. Quella interna non muore ma viene schermata da questa 
        print('id var2 = ', hex(id(self.cl1.var2)))
        print('id oggetto = ', hex(id(self.cl1)) )
        print('****************************************')

    def passa_obj(self, obj):
        self.obj2=obj

