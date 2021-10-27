'''GTK IMPORTS -------------------'''
import gi 
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
'''-------------------------------'''

'''Python IMPORTS ----------------'''
import os

'''-------------------------------'''

class ProvaGui1_5:
    
    def __init__(self):

        '''__init__Directories setup'''
                                                   #l'indirizzo in __file__ può essere assoluto o relativo a seconda di come è stato lanciato python
        nomedelfile=os.path.basename(__file__)     #la funzione basename restituisce cmq l'ultima parte del path (il nome del file.py)
        folder=os.path.abspath(__file__).strip(nomedelfile) # abspath restituisce sempre il path assoluto. L'intersezione dà la folder
        
        '''_____________________________________________________________________________________________________________________________________________'''

        '''__init__GTK setup'''

        gladefile= folder+'\ProvaGui1_5.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladefile)  #carica l'interfaccia dal file all'indirizzo
        self.builder.connect_signals(self)

        finestra = self.builder.get_object('MainW')
        finestra.show()
        finestra.connect('destroy', Gtk.main_quit)

    def printText(self, widget):
        entryInput = self.builder.get_object('toPrintEntry')
        text       = entryInput.get_text().strip()
        print(text)
        entryInput.set_text('Enter a text')



if __name__ == '__main__':
    main = ProvaGui1_5()
    Gtk.main()
