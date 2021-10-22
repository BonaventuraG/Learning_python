import gi 
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class ProvaGui:

    def __init__(self):
        gladefile= 'D:\Documents\Bonaventura\MASCOT\MieProve\ProvaGui.glade'
        self.builder=Gtk.Builder()
        self.builder.add_from_file(gladefile)

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
