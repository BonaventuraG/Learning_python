class provaobj:

    def __init__(self):
        if not provaobj.instance:
            provaobj.instance = provaobj.InProva()

    instance=None
        
    def __getattr__(self, name):
        return getattr(self.instance, name)

    class InProva: 
        

        def __init__(self):

            self.var=[5]  #bisogna usare liste o dizionari, perchè le variabili cambiano indirizzo una volta che vengono cambiate (cioè il puntatore a sinistra dell'operatore '=' dopo l'assegnazione punta all'indirizzo della variabile a destra)
            self.var2=3 #con le liste e i dizionari ciò non avviene, perchè viene modificato solo l'elemento della lista ma non l'oggetto lista.
            
            print("variabile class= ", self.var )
            print (hex(id(self.var)))

                
        var3=[0]


