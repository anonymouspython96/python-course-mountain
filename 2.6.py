'''
    Le collezioni ed i contenitori!

    Che tipo di criterio di ragruppamento è? E' un ragruppamento che segue il 
    dominio di applicabilità degli operatori for e in, cioè sono ragruppati gli elenchi sui
    quali si possono far agire gli operatori for e in.
    E quindi una classificazione operativa.

    Gli elenchi iterabili sono quegli elenchi che supportano l'splorazione elemento per elemento con il ciclo for.
    
    I contenitori sono quegli elenchi sui quali può agire l'operatore di appartenenza in.

        # Una stringa come anche un file è iterabile.

    Gli oggetti che sono SIA iterabili che contenitori sono     COLLEZIONI.

'''
mia_lista = ["Dario"]
print(mia_lista[0][0]) #iniziale => D
#statico

def iniziale(nome):
    print (nome[0][0])
#dinamico

iniziale("Emilian")

'''
    Milestone
    Condizioni -> if -> boom
    Cicli -> for -> boom
    Funzioni -> def -> boom
    Moduli -> ecc
    Classi -> ecc
'''

mia_tupla = ("Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica")

print(dir(tuple))

mio_set = set({}) #set elimina duplicati
mio_set.add(3) #set assieme ad add mette in ordine i dati
mio_set.add(4)
mio_set.add(5)
mio_set.add(1)
print(mio_set)












