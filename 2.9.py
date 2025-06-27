'''
    Chiediamo all'utente di inserire una parola a caso.
    Se la parola è lunga meno di 5 caratteri, aggiungere un numero opportuno
    di "x" om ,pdp da raggoimgere il numero minimo di 5 caratteri.
'''
parola = input("Inserisci una parola: ")

if len(parola) == 4:
    print(parola+"x")
elif len(parola) == 3:
    print(parola+"xx")
elif len(parola) == 2:
    print(parola+"xxx")
elif len(parola) == 1:
    print(parola+"xxxx")
moltiplicatore = 5-len(parola)
if moltiplicatore > 0:
    print(parola + "x"*moltiplicatore)