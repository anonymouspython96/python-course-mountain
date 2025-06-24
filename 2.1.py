#Approfondiamo le collezioni Range e Stringhe.

#approfondire vuol dire imparare i comandi per lavorare su quesre collezioni.
#Essendo collezioni ordinate si possono definire sequenze.

myrange = range(120, 190, 9)

for n in myrange:
    print(n)

print(list(myrange)) #crea una lista simil array di js :)

#In python ogni tipologia di variabile ha la sua funzione di casting.
#Quindi int ha int(), str ha str() (con le parentesi.) o bool che ha bool() o infine float() ;)
# Ma anche le collezioni hanno il loro type.
# Le liste, che ancora dobbiamo vedere, hanno la loro funzione di casting: list().

#in quanto sequenze ammettono operazioni (su sequenze )
rangeone = range(1,11)
print(list(rangeone))
rangetwo = range(11, 21)
print(list(rangetwo))
rangeone = list(rangeone) + list(rangetwo)
print(list(rangeone))

#Come concatenare due liste 

risata = "ah"*18
print(risata)
