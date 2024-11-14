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

controllo = True
while controllo == True:
    print("1) Aggiungi un elemento alla lista")
    print("2) Visualizza la lista")
    print("3) Elimina un elemento della lista")
    x = input ("Inserisci il numero di ciò che vuoi fare ")
    if x == 1:
        aggiunta()
    elif x == 2:
        stampaLista()
    elif x == 3:
        eliminaElemento()
    else:
        uscita = input("Vuoi uscire dal programma? (y/n)")
        uscita.lower()
        if uscita == "y":
            controllo = False
