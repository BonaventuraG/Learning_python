# Cat class

class Cat:
    name = ''
    age = 0
    color = ''

    def __init__(self,name,age=0,color='white'):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')

    def meow(self):
        print(f'{self.name} meow')

    def sleep(self):
        print(f'{self.name} zzzzzz')

    def hungry(self):
        for i in range(5):
            self.meow()

    def description(self):
        print(f'{self.name} is a {self.color} cat, who is {self.age} years old')

