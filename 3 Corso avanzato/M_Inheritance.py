#multiple inheritance

class Vehical:
    speed=0
    def drive(self, speed):
        self.speed=speed
        print('driving at ', self.speed, 'km/h')

    def stop(self):
        self.speed=0
        print('stopped')

    def display(self):
        print('Driving at', self.speed, 'speed')


class Freezer:
    temp=0
    def freeze(self,temp):
       self.temp=temp
       print('Freezing') 

    def display(self):
        print('Freezing at', self.temp, 'temperature')


class FreezerTruck(Freezer,Vehical): #method resolution order: FCFS (First Come First Serve)
    
    
    def display(self):
        print('Driving at', self.speed, 'speed while freezing at', self.temp, 'temperature')

        Freezer.display(self)  # in questo modo si risale alla classe genitore e si richiama quel metodo passando l'oggetto figlio
        Vehical.display(self)
    
    

t=FreezerTruck()
t.drive(50)
t.freeze(-20)
print('-'*10)
t.display()    #verrà richiamato il metodo del primo genitore (Freezer in questo caso). Si può fare overriding però
