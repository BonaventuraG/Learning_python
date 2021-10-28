from cats import Cat
from cats import Tiger
from cats import Lion


def test():
    b = Cat('Milù',2,'gray')
    c = Cat('Nerone',2,'black')
    b.description()
    c.description()
    b.sleep()
    
    l=Lion('leo')
    print(l.name)

    #t=Tiger(Tigro)     ##gives error. Spiegazione nel file della classe (cats.py)
    #print(t.name)

    t=Tiger()
    print(t)
    print(t.name)
    t.rename('Tigro')
    print(t.name)      #in qualche modo funziona grazie a super, ma di certo funziona male (c'è bisogno di riassegnare il nome). 
    #Si può fare meglio, passando in super un argomento che viene da fuori.
    # Meglio non sovrascrivere gli init, e se proprio si deve, meglio fare attenzione

if __name__ == "__main__":
    test()