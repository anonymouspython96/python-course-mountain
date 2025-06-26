# parola1 = input("Prima parola: ")
# parola2 = input("Seconda parola: ")
# parola3 = input("Terza parola: ")

# if len(parola1) > len(parola2):
#     print("La prima è più lunga della seconda")
# elif len(parola2) > len(parola3):
#     print("La seconda parola è più grande della terza")
# elif len(parola3) > len(parola1):
#     print("La terza parola è più grande della prima")

#Manualmente è una coa inutile qua serve un loop

# lista_parole=set()

# parola4 = input("Prima parola: ")
# lista_parole.add(parola4)
# parola5 = input("Seconda parola: ")
# lista_parole.add(parola5)
# parola6 = input("Terza parola: ")
# lista_parole.add(parola6)

# print(lista_parole)

'''
    I dictionari sono dei set, quindi sono degli iterabili contenitori (quindi collezioni)
    non ordinabili e modificabili. Come i set si dichiarano con le graffe. La differenza 
    è che gli elementi son delle coppie ordinate. Il primo elemento della coppia si chiama chiave
    ed è il "pilota della coppia. E' la chiave primaria di questa specie di database con record a 
    due campi. Il secondo elemento è il valore della coppia. I valori possono essere non univoci.
    Per esempio {key1: val1, ...2: ...2, ecc...}
    Le coppie sono elementi non ordiabili, ma all'interno della coppia gli elementi sono ordinati e immutabili,
    poichè il ruole di chiave e valore è ben definito.
    E' come se il dictionary fosse un set i cui elementi son tutte tuple di 2 elementi.
'''

primi_due_mesi = {
    "Gennaio": "A",
    "Febbraio": "B",
    "Marzo": ["C", "c", "ç"]
}

print(primi_due_mesi["Marzo"][-1]) # così se è nestato
due_comuni = {
    "Torino": "T219",
    "Moncalieri": "F335"
}

'''
    è come se l'indice che mi permette di esplorare il mio archivio di valori non fosse più 
    vincolato ad una sequenza di numeri naturali zero compreso, ma potesse essere preso da un insieme qualsiasi di elementi
    chiamati chiavi della coppia- La differenza è che le key sono univoche, mentre i valori possono essere uguali. Che vantaggio da? Nessuno se non ho bisogno di fare un piccolo database a due valori. Mi serve invece per creare con un comando solo un intero, anche se semplice, database a due valori.
'''

print(due_comuni["Moncalieri"])

'''
    Il dictionary è quel set i cui elementi sono tuple a due valori il cui primo elemento è univoco e lo chiamo chiave.
    Potrei inventarmi un set i cui elementi sono tuple a due valori senza restrizioni sul primo elemento.
'''

#Quale parola ha la lunghezza maggiore
# miao

'''
Prima parola: cacca
Seconda parola: verdure
Terza parola: elefante

'''

# dict_lista = []
# parola1_1 = input("Prima parola: ")
# parola2_1 = input("Seconda parola: ")
# parola3_1 = input("Terza parola: ")
# dict_lista= [parola1_1,parola2_1,parola3_1] 
# print(max(dict_lista))

'''
Chiedi tre parole, e stampa la parola con la prima lettera più alta
la parola con l'ultima lettera più alta 
inseriamo un controllo, se le due parole coincidono 
dire che la parola è la stessa.
'''

parola1_2 = input("Prima parola: ")
parola2_2 = input("Seconda parola: ")
parola3_2 = input("Terza parola: ")

ALFABETO = "abcdefghijklmnopqrstuvwxyz"

mio_dictionary = {
    parola1_2: parola1_2[0],
    parola2_2: parola2_2[0],
    parola3_2: parola3_2[0],
}

mio_dictionary2 = {
    parola1_2: parola1_2[-1],
    parola2_2: parola2_2[-1],
    parola3_2: parola3_2[-1],
}

max1 = max(mio_dictionary, key=mio_dictionary.get)
max2 = max(mio_dictionary2, key=mio_dictionary2.get)

# migliorare il controllo errore in python after professional or nel frattempo

if max1 == max2: 
    print(f"La parola {max1} è sia quella con la prima che con l'ultima lettera più alta.") 

