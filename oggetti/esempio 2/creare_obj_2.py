from classe import provaobj

class creaobj:

    def __init__(self):
        
        self.cl1=provaobj()
        self.cl1.var[0]=12
        self.cl1.var3[0]=1

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
        self.cl1.var2=99
        print('id var2 = ', hex(id(self.cl1.var2)))
        print('id oggetto = ', hex(id(self.cl1)) )
        print('****************************************')
