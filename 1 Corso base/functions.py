### FUNCTIONS

def greet(nome='invitato', cognome='Esposito'): #default parameter = 'invitato'
    if nome == 'Nello':
        print('who are you?')
        return False  ##return brakes the function
    print('hello ' +  nome + ' ' + cognome)
    return True

names=['Bona','Bonnie','Nello']

for nome in names:
    greeted=greet(nome)
    if greeted:
        print('ok')

invitati=[['Bona','Boh'],['Bonnie','Clyde'],['Nello','Bruno']]

for i in range(len(invitati)):
   greeted=greet(invitati[i][0],invitati[i][1])
   if greeted:
       print('ok')

for i in range(len(invitati)):
   greeted=greet(cognome=invitati[i][1])
   if greeted:
       print('ok')

#se fosse stato
# def greet(nome='invitato', cognome='Esposito', /):
# lo slash avrebbe impedito il passaggio di parametri
# per nome. A quel punto si era costretti a passarli per 
# posizione. Tutto ciò che è PRIMA di ,/ sarà un
# parametro posizionale. Tutto ciò che è DOPO un ,*
# potrà essere passato solo per nome

#________________________________________________
## Unlimited arguments

def greet_all(*people): #questo * è diverso da ,*
    for person in people:
        print('Hi ' + person, end=' ')
    print()

greet_all('Are','Very','Frank','Bona','Giusy','Angelo','Anna','Giada')

#________________________________________________
## Unpacking lists

def print_info(name,age,email):
    print(name + ' is ' + str(age) + ' years old, reached at ' + email)

info = ['Bonnie', 33, 'garb588@yahoo.it']

print_info(*info)

#_________________________________________________
## Nested functions

def greet_all(*people): #questo * è diverso da ,*
    for person in people:
        greet(person)
    print()

greet_all('Are','Very','Frank','Bona','Giusy','Angelo','Anna','Giada')

