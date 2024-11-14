lista = []


def aggiunta():
    item = input("inserisci un elemento alla lista:")
    item.lower()
    lista.append(item)

def stampaLista():
    print(lista)

def eliminaElemento():
    print(lista)
    risp = input("inserisci il nome dell'elemento che vuoi eliminare")
    risp.lower()
    lista.remove(risp)

def conteggio():
    cont =0 
    for i in range(len(lista)):
        cont += 1
    print(f"la lista contiene {cont} elementi")

def svuotaLista():
    for i in range(len(lista)):
        lista.remove(lista[i-1])

controllo = True
while controllo == True:
    print("1) Aggiungi un elemento alla lista")
    print("2) Visualizza la lista")
    print("3) Elimina un elemento della lista")
    print("4) Stampa il numero di elementi presenti nella lista")
    print("5) Svuota la lista")
    print("(Qualsiasi altro tasto per uscire dal programma)")
    x = input ("Inserisci il numero di ciò che vuoi fare ")
    if x == "1":
        aggiunta()
    elif x == "2":
        stampaLista()
    elif x == "3":
        eliminaElemento()
    elif x == "4":
        conteggio()
    elif x == "5":
        svuotaLista()
    else:
        uscita = input("Vuoi uscire dal programma? (y/n)")
        uscita.lower()
        if uscita == "y":
            controllo = False
