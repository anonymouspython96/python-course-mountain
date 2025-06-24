lamiastringa = "CiaoCiao"
print(lamiastringa[3:7]) #oCia è l'output
myrange4 = range(1,11)
print(list(myrange4[4:7])) #5, 6, 7
print(list(myrange4[:7])) # se non metto niente è sottinteso dall'inizio o dalla fine.
print(list(myrange4[4:]))

#problema: senza sapere la lunghezza del mio range da 1 a 10, voglio estrarre gli ultimi 3 elementi, utilizzando
#solamente lo slicing, il comando len, e l'operatore di indicizzazione.

print(list(myrange4[len(myrange4)- 3:])) #[8, 9, 10]
print(list(myrange4[-3:]))#[8, 9, 10]

# lunghezza_range = int(input("Inserisci il numero che vuoi usare per far iniziare il range: 2"))

# print(list(myrange4[lunghezza_range: 11])) # si può fare dinamismo anche con il range!!

#OGGETTI
#   ATTRIBUTI 
#   METODI

mystring1 = "Ciao Bella"
mystring2 = "CIAO BELLO"
print(mystring1.upper()) #CIAO BELLA uppercase
print(mystring2.lower()) #ciao bello lowercase
print(mystring2.count("O")) #conta quante O ci sono
print('''snifghgihagihaaaaaaaaaaaaaaaa
aaaaadsafjkbmfnsabfjdbfdasfihfiaf''') #per andare a capo mettere '''

# metodi relativi a un certo tipo di oggetti!!!

print("ciao, come stai?".upper()) #OOP everywhere
print("ciao come stai?".capitalize()) #maiuscola ad inizio stringa
print("Ciao, come stai?".title()) #capitalizza come titolo in Copilot c'era WOOW
print("Ciao, come stai?".split(" ")) #split separa in una lista di 3 sottostringhe
print("Ciao, come stai?".split(" ")[0]) 
# Appena trova lo spazio tronca il resto a destra e lascia il contenuto di sinistra

print(sorted("Ciao come stai?"))

#Split separa una stringa secondo un separatore che metto a destra come argomento del metodo 
# e serve le sottostringhe in una lista
# join è l'esatto opposto: unisce gli elementi di una lista in un unica 
# stringa separando i vari elementi con un separatore a scelta
bellebuono = "ciao come stai?"
print(bellebuono.split())
print(" ".join(["Ciao,", "come", "stai?"])) # join è vero che agisce su una lista ma in realtà è un metodo della
#classe stringa in particolare dell'oggetto stringa usato come separatore.

print(" ".join(["Ciao,", "Emi"]))
prova2 = list("Bene grazie, e tu?")
print(prova2)

print(" Ciao".strip())

#le stringhe sono immutabili: non supportano l'assegnazione
#ma non vuol dire che non esistono metodi specifici per fare modifiche
#replace

print(" ".join(prova2).replace(" ",""))
print("Ciao".replace("C","Z"))
elemento = "09"
print(elemento.find("9")) #find trova l'index dell'elemento







