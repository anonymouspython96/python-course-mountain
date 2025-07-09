'''
    Scrivere un programma che chiede all'utente di inserire dei numeri da tastiera,
    e tiene il conto solamente dei numeri > 100 e alla fine 
    mi dice quanti numeri maggiori di 100 ho inserito. Per terminare il programma l'utente deve premere 0.
'''

def funzioneEsercizio():
    
    contatore_numeri_maggiori_100 = 0
    
    while True:
        try:
            n = int(input("Inserisci un numero (cliccando 0:chiudi n>100:accumula n<100:non fare niente): "))
            condizione = 0
            
            if n >= 100:
                contatore_numeri_maggiori_100 += n
                print(f"La somma attuale dei numeri maggiori di 100 è: {contatore_numeri_maggiori_100}")
        
            elif n == condizione:
                break
        
        except ValueError:
            print("Non inserire lettere, inserisci solo numeri.")
        

import math

print(math.factorial(4))

def fattoriale():
    n = int(input("Inserisci un numero a cui vuoi fare un fattoriale: "))
    fattorial = n
    while n > 1:
        n -= 1
        fattorial *= n
    print("Il fattoriale del numero inserito è: ", fattorial)
    
    