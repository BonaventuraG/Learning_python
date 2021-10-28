class Feline:

    def __init__(self,name):
        self.name = name
        print('creating a feline')

    def sleep(self):
        print(f'{self.name}: zzzzzz')

    def setName(self, name):
        self.name = name

#Lion class

class Lion(Feline):

    def roar(self):
        print('roar')

#Tiger class

class Tiger(Feline):
    def __init__(self): #abbiamo sovrascritto la funzione __init__ ed ora la classe Tiger non ha l'attributo name definito nell'init di Feline
        super().__init__('no name')
        print('creating a tiger')

    def rename(self,name):
        super().setName(name)


# Cat class

class Cat(Feline):
    name = ''
    age = 0
    color = ''

    def __init__(self,name,age=0,color='white'):
        self.name = name
        self.age = age
        self.color = color
        print('Constructor for', self.name)

    def meow(self):
        print(f'{self.name} meow')

    def hungry(self):
        for i in range(5):
            self.meow()

    def description(self):
        print(self.name,' is a ',self.color,' cat, who is ',self.age,' years old')

