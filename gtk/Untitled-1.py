'''Python IMPORTS ----------------'''
import os

'''-------------------------------'''

print('indirizzo:  '+ os.getcwd())
print('indirizzo2: ' + __file__)
print('indirizzo3: ' +os.path.abspath(__file__))
print('indirizzo3: ' +os.path.basename(__file__))
print('indirizzo4: ' + __file__.strip(os.path.basename(__file__)))
