emails= {
         'personal':'gxxxxxx@xxxxx.it',
         'work': 'bonxxxx.gxxxx@sxxx.it',
         'uni': 'bonxxx.gxxxx@unixx.it'                               
        }
print()
print(emails)
print()

#the key has to be hashable (strings, tuples, ...)
# il tempo che serve per trovare un dato in un dizionario
# non dipende dalla grandezza del dizionario O(1)

print(emails['personal'])

print(emails.get('work'))
print(emails.get('game'))
print(emails.get('game', 'not found'))

emails['pec']='boxxx_gxxx@xxxx.it' #adding a record

emails.update({ 'forum':'none',
                'highschool':'none',
                'previouswork':'none'})  #adding more records


for k in emails:    #il dizionario è iterabile, ma scorre solo le key 
    print(k)

for k,v in emails.items(): #items è un metodo che restituisce un qualcosa di iterabile sia sulle key che sui valori
    print(k,v)

print('\n',type(emails))
print('\n',type(emails.items()))
print('\n',emails.items())




