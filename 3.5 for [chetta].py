# # Richiede all'utente di inserire una sequenza di caratteri
# lista_numeri = input("Lista: ")  

# # Inizializza una nuova lista vuota
# nuova_lista = []

# # Cicla attraverso la stringa, fermandosi al penultimo carattere
# for i in range(len(lista_numeri) - 1):
#     # Controlla se il carattere corrente è una cifra
#     if lista_numeri[i].isdigit():
#         # Controlla se il carattere successivo è anch'esso una cifra
#         if lista_numeri[i + 1].isdigit():
#             # Se sì, aggiunge la concatenazione delle due cifre alla nuova lista
#             nuova_lista.append(lista_numeri[i] + lista_numeri[i + 1])
#         else:
#             # Altrimenti, aggiunge solo la cifra corrente
#             nuova_lista.append(lista_numeri[i])

# # Dopo il ciclo, controlla gli ultimi due caratteri per gestire eventuali casi speciali
# if len(lista_numeri) >= 2:
#     if not lista_numeri[-2].isdigit() and lista_numeri[-1].isdigit():
#         nuova_lista.append(lista_numeri[-1])

# # Mostra il risultato finale
# print("Nuova lista:", nuova_lista)

'''
🟢 Semplici
Questi algoritmi sono basilari, ma estremamente utili:
- Ricerca Lineare: per trovare un elemento in una lista controllando uno alla volta.
- Bubble Sort / Selection Sort: per ordinare piccole quantità di dati.
- Conteggio: per contare elementi che soddisfano una condizione (es. quante email ricevute oggi).
- Calcolo della media, somma, minimo, massimo: utili nell’analisi dei dati.
- Modulo e divisione intera: per calcolare ratei o cicli (es. turnazioni).

🟡 Medi
Questi richiedono più attenzione, ma sono comuni in contesti professionali:
- Ricerca Binaria: efficace su strutture ordinate, velocissima.
- Quick Sort / Merge Sort: algoritmi di ordinamento efficienti, usati in produzione.
- Hashing: per la gestione veloce di dati associativi (es. codici cliente → informazioni).
- Gestione di file e buffer: algoritmi per caricare e scrivere dati in memoria.
- *Dijkstra / A (pathfinding)**: usati in logistica, giochi o sistemi di navigazione.
- Backtracking: per risolvere problemi con molte combinazioni (es. puzzle, ottimizzazioni).

🔴 Complessi
Qui entrano in gioco algoritmi usati in ambiti avanzati:
- Algoritmi di Machine Learning (Random Forest, SVM, Gradient Boosting): per estrarre insight dai dati.
- Neural Networks: alla base dell’intelligenza artificiale moderna.
- Algoritmi crittografici (RSA, AES): per protezione dei dati.
- Algoritmi genetici / evolutivi: usati nell’ottimizzazione e simulazione.
- Algoritmi di compressione (Huffman, LZW): per ridurre dimensioni di file o trasmissioni.
- Distributed algorithms: per gestire risorse e calcoli su sistemi in rete.

''' #Vira Team theme

# nuovo esercizio = 
#utilizzando il ciclo for far stampare al programma un rettangolo fatto con gli astrichi la base e l'altezza del rettangolo dovranno essere inserite dall'utente.
print("Inserisci la misura delle righe e delle colonne del rettangolo...")
righe = int(input("righe: "))
colonne = int(input("colonne: "))

for x in range(righe):
    riga = ""
    for y in range(colonne):
        riga += " * "
    print(riga)

print("__________________________________________________________________ \n")

for x in range(righe):
    for y in range(colonne):
        print(" * ",end="")
    print("")
    
print("__________________________________________________________________ \n")

riga = " * "*colonne
for i in range(righe):
    print(riga)
    
print("__________________________________________________________________ \n")