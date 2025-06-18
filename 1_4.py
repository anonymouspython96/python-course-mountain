# In python esistono molti tipi di variabili. Ciascun tipo di
# Variabile ha la sua funzione di casting.
# Interi (int) -> tutti i numeri interi
# Stringhe (str) -> tutte le sequenze di caratteri, compresi gli spazi vuoti.
# Decimali (float) -> tutti i numeri decimali 
# Booleani (bool) -> tutti i valori booleani (due) true and false

# I valori booleani sono due: True e False, scritti in pascal case!

# Esiste una funzione che prende in pasto una variabile e mi restituisce il suo type()

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))
somma = num1 + num2

print(type(somma))
nome = "Dario"
print(type(nome))

risposta = False
print(type(risposta))

if type(nome) != type(risposta): print("Bravo!")













