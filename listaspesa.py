lista = []


def aggiunta():
    item = input("Inserisci un elemento alla lista")
    lista.append(item)

def stampaLista():
    print(lista)

def eliminaElemento():
    print(lista)
    risp = input ("inserisci il nome dell'elemento che vuoi eliminare")
    risp.lower()
    lista.remove(risp)

