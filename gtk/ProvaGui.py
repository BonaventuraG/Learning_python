'''GTK IMPORTS -------------------'''
import gi 
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
'''-------------------------------'''

'''Python IMPORTS ----------------'''
import os

'''-------------------------------'''

class ProvaGui:

    def __init__(self):

        '''__init__Directories setup'''
                                                   #l'indirizzo in __file__ può essere assoluto o relativo a seconda di come è stato lanciato python
        nomedelfile=os.path.basename(__file__)     #la funzione basename restituisce cmq l'ultima parte del path (il nome del file.py)
        folder=os.path.abspath(__file__).strip(nomedelfile) # abspath restituisce sempre il path assoluto. L'intersezione dà la folder
        
        '''_____________________________________________________________________________________________________________________________________________'''

        '''__init__GTK setup'''

        gladefile= folder+'\ProvaGui.glade'
        self.builder=Gtk.Builder()
        self.builder.add_from_file(gladefile)  #carica l'interfaccia dal file all'indirizzo
                   

        button_1= self.builder.get_object('button_1')
        button_1.connect('clicked', self.printText)

        finestra= self.builder.get_object('MainW')
        finestra.show()
        finestra.connect('destroy', Gtk.main_quit)
        

    def printText(self, widget):
        print('hello world')

if __name__ == '__main__':
    main = ProvaGui()
    Gtk.main()
