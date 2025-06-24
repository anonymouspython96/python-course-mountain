# domanda = input("Qual è la capitale d'Italia? ")

# corretta = "Roma"

# if (domanda == corretta) :
#     print("Risposta corretta")
# else : 
#     print("Risposta errata")


#Operatori in Python 

#Abbiamo accennato a molte tipologie diverse di operatori.
#Ok, ma quanti ne esistono e come si posson classificare?

#Operatori ARITMETICI

# Agiscono su variabili int e float. Esito: risultato int o float. 

# + - * ** / // %

#Operatore di assegnazione.

#Assegnano o modificano (cioè aggiornato) il valore di una variabile. Esito è una variabile inizializzata o modificata.
#NB Dichiarare una variabile vuol dire dire al programma che quella variabile esiste, deve ritagliarsi uno spazio 
#per lei nella memoria, e deve organizzare questo spazio per riconoscere questa variabile come appartenente a un certo 
# tipo (int str ecc). IN PYTHON NON è NECESSARIO.
# INIZIALIZZARE una variabile precedentemente dichiarata vuol dire darle un valore iniziale. Python è abbastanza
# intelligente da fare una dichiarazione nel momento stesso dell'inizializzazione.

# = Assegnazione vera e propria.
# += Esempio: num1 += num2 vuol dire che mi sta agiornando il valore di num1 SOMMANDOGLI num2. Cioè è un modo
    #compatto di scrivere num1 = num1 + num2.
# -=
# *=
# /=
# //=
# **=
# %=

#Ho in mano un contapersone. Ogni volta che clicco si aggiorna di uno il totale.Roma
numero_persone = 0
numero_persone =+ 1 #incremento
numero_persone =- 1 #decremento e così via...

a = 5
b = 3
a += b
print(a) #Output: 8!

#a-=b -> a = a - b
#a*=b -> a = a * b 
#ecc

#N:B: Così come l'operatore di assegnazione regge non solo i numeri ma anche altri tipi di variabili, 
# anche le shortcuts reggono altri tipo di variabili.

# operazione = int(input("Quanto fa 10 / 2? "))

# corretta = 5

# if (operazione == 5 ):
#     print("Esatto")
# else:
#     print("Sbagliato")

stringa1 = "Bau"
stringa2 = "Miao"
print(stringa1 + stringa2)
stringa1+=stringa2
print(stringa1)

#Operatori di confronto True or False
# == esempio -> 5==6 False legge python 
# > 
# <
# >=
# <=
# !=

# Operatori logici.
# Agiscono tra variabili booleane. Restituiscoo una variabile booleana.
# Essendo operatori binari, possono essere visualizzati come una matrice caratteristica
# per ogni operatore. Not invece non avrà una matrice caratteristica ma avrà un vettore.
# Sono l'analogo delle Tabelle di moltiplicazione.

# and
# or
# not

# Operatori di confronto = Confronto di dati che restituiscono un booleano
# Operatori Logici = Bool x Bool -> Bool
# Sono operatori che agiscon su due variabili booleane, cioè tra due condizioni.













