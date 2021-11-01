#Test class

class Person:
    #week private (it is for internal scopes but it can be accessed from outside)

    _name='No name'

    def setName(self, name):
       self._name=name 
       print('Name set to', self._name)

    #strong private

    def __think(self):
        print('thinking about myself')

    def work(self):
        self.__think()

    #before and after
    def __init__(self):
        print('constructor')

    def __calling__(self):
        print('call someone')

class Child(Person):

    def testDouble(self):
        self.__think()

    def contrasto(self):
        print('ok')
