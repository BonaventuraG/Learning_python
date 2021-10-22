
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
        gladefile= folder+'\ProvaGui2.glade'
        self.builder=Gtk.Builder()
        self.builder.add_from_file(gladefile)  #carica l'interfaccia dal file all'indirizzo
        self.builder.connect_signals(self)     #connette tutti i segnali (glade) ai simboli dell'applicazione (nomi delle funzioni(?) )
        
        '''_____________________________________________________________________________________________________________________________________________'''
                
        '''__init__GTK_Tree_View'''
        self.pathTreeView = self.builder.get_object('pathTreeView')  # carica l'oggetto GtkTreeView con id pathTreeView 
        self.pathListStore = Gtk.ListStore(str)                      # carica il metodo Gtk.ListStore (dando l'alisas pathListStore) che implementa GtkTreeView e i suoi metodi
                                                                     # più informazioni su Gtk.ListStore su https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListStore.html
        '''____________________________________________________________________________________________________________________________________________'''

        '''__init__Caricamenti e setups'''
        self.loadPaths()      #il programma carica i paths secondo la funzione definita in basso
        self.setupTreeView()  #il programma prepara il TreeView 

        #self.bashrcPath   = os.path.expanduser('~') + "/" + ".bashrc"  #path del file bashrc NON LO USEREMO, viene usato nel videotutorial
        self.selected  = None                                          #variabile globale (a livello di file??) per gestire la cancellazione di una riga selezionata
        self.txtFile = folder+'\ProvaGui2.txt'

        '''___________________________________________________________________________________________________________________________________________'''

        '''__init__Chiamata a finestra principale'''
        finestra= self.builder.get_object('MainWindow') # carica la finestra e i suoi metodi
        finestra.show()                                 # mostra la finestra col metodo .show
        finestra.connect('destroy', Gtk.main_quit)      # ?? dovrebbe connettere il metodo per chiudere tutto all'uscita dal programma
        '''___________________________________________________________________________________________________________________________________________'''
        
    '''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Fine __init__ <<<<<<<<<<<<<<<<<<<<<<<<<<<<'''       

    '''Funzioni associate a signals'''

    def addEntry(self, widget):
        
        toAddPathTxt= self.builder.get_object('toAddPathEntry').get_text().strip() # carica l'oggetto e i suoi metodi e usa get_text per ottenere il testo (poi strip per eliminare spazi)
        
        if os.path.isdir(toAddPathTxt):
            self.pathListStore.append([toAddPathTxt])   # Gtk.ListStore.append accetta come argomento delle liste. Si aggiunge [] per avere una lista

    
    def deleteEntry(self, widget):
        
        self.pathListStore.remove(self.selected)  #viene passato l'indirizzo e rimosso l'elemento selezionato


    def setSelected(self, user_data):
        
        selected=user_data.get_selected()[1] #user_data punta all'oggetto (tree). get_selected restituisce l'indirizzo della selezione. Insieme formano una lista di due indirizzi di cui prendiamo il secondo [1] (quello della selezione)
        
        if selected:                 #controllo necessario dovuto al segnale changed della gtk (alias setSelected) che potrebbe essere emesso anche quando non accade nulla 
            self.selected=selected   #la variabile locale viene riversata nella globale


    def saveToTxt(self, widget):
        
        file=open(self.txtFile, mode='w')
        iter= self.pathListStore.get_iter_first() # in questo modo si prende la prima riga. pathListStore è una lista di righe, NON di stringhe 
        while iter != None: 
            stringa= self.pathListStore.get_value(iter,0) + '\n' # con get_value(iter,0) si prende la stringa associata alla riga iter e colonna 0
            file.write(stringa) 
            iter= self.pathListStore.iter_next(iter)             # si passa alla riga successiva finchè non è inesistente

        print('file sovrascritto')

                            


    '''_________________________________________________________________________________________________________________________________________________'''

    ''' Funzioni di servizio''' 

    def loadPaths(self):
        pathsStr = os.getenv('PATH')            # carica in una stringa i path dalla variabile UNIX 'PATH' (directories in cui UNIX cerca gli eseguibili) 
        paths= pathsStr.split(';')              # split a sting into a list

        for path in paths:
            self.pathListStore.append([path])   # Gtk.ListStore.append accetta come argomento delle liste. Ma path è un elemento della lista, quindi va messo fra [] per renderlo una lista 


    def setupTreeView(self):

        renderer = Gtk.CellRendererText()
        pathColumn = Gtk.TreeViewColumn(title='Paths', cell_renderer=renderer, text=0)  # crea una colonna con titolo "Paths"
        self.pathTreeView.append_column(pathColumn)                            # appende la colonna all'oggetto pathTreeView
        self.pathTreeView.set_model(self.pathListStore)                        # definisce il modello di TreeView integrando la colonna e la list store

    '''_________________________________________________________________________________________________________________________________________________'''

if __name__ == '__main__':
    main = ProvaGui()
    Gtk.main()
