#abbiamo 3 possibilità di utilizzare il comando print.
# 1) separare variabili diverse con la virgola.
#print("Ciao ", nome, " la tua età è: ", anni, ".")
# 2) usare la formattazione del messaggio di output. Si indica
# a python che vogliamo formattare il messaggio aggiungendo una f prima
# delle virgolette. A quel punto possiamo inserire le variabili direttamente
# nel messaggio utilizzando le parentesi graffe.

# print(f"Ciao la somma di 4 e 7 è: {4+7}") #utilizzo di f per vare operazioni o richiamo di variabili e costanti

# anni = input("Inserisci la tua età: ") #esempio di casting int.
# print(f"I tuoi anni: {anni}")
# print(f"Ciao ora faccio un calcolo: {int(anni) + 33}") 
# qui si può fare casting degli anni assegnando int(anni)

# '''
# Nota Bene: Quando uso il comando input(), di default l'input viene
# interpretato come una stringa.
# Come faccio a inserire un numero che venga interpretato come numero?
# Con il casting delle variabili!!!!!!!!!!

# Ci sono delle funzioni che trasformano un tipo di variabile in un altro tipo.
# le funzioni sono int(), str() e/o bool()

# Casting -> la variabile resta sempre la stessa come anche il suo valore 
#           cambia l'interpretazione...
#                       Che python dà a quel valore. E' come se fosse un nesting in orizzontale.

# Il simbolo + è un operatore cioè è un simbolo che svolge un'operazione a seconda
# del tipo di oggetti che vengono sommati
# il simbolo + avrà un simbolo differente
# Cioè in python esiste l'overloading degli operatori, cioè lo stesso simbolo può avere più significati a
# seconda del contesto. 3 + 5 vuol dire sommare due interi.

# "Abra" + "Cadabra" vuol dire invece concatenazione = AbraCadabra

# Il terzo modo di usare il print è concatenando tra loro STRINGHE.
# '''

num_gatti = int(input("Numero di gatti: "))
num_cani = int(input("Ora inserisci il numero di cani: "))
num_animali = num_gatti + num_cani
print("Io ho: " + str(num_animali) + " animale/i")

# se voglio concatenare numeri e stringhe devo castare i valori ad uno solo.

#revisionato 08/07/2025























