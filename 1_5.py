#num = 3.5
#print(type(num))

#num1 = input("Inserisci il primo numero")
#num2 = input("Inserisci il secondo numero")

#somma = num1 + num2
#print(somma)

# qui avviene una concatenazione di numeri quindi l'output diventa per es 71 al pari di due stringhe o di float
# Cosa vuol dire castare una variabile dentro un bool?

num3 = "47"

print(int(num3) + 3)

num4 = "Paperino"
#print(int(num4)+2) # qui semanticamente py non capisce cosa sia "Paperino"

#Cosa succede dal punto di vista booleano?

print(type(4 > 3))

#l'esito del confronto tra 4 e 3 è una variabile di tipo booleano. In particolare
#il suo valore è True
# In generale tutti i confronti
# quali sono? maggiore, minore, uguale, diverso.

#ora mi invento una variabile alla quale assegno un valore booleano.

scelta = True
esito_confronto = False
risultato = 4 < 1 #per l'interprete questi tre caratter non sono più tre caratteri
#ma sono una variabile booleana che vale False. Dire che risultato è uguale a
# 4 minore di 1 vuol dire in raltà che "risultato" è uguale all'esito booleano
# del confronto tra 4 e 1

print(risultato)
print(type(risultato))

confronto = 5 == 5 #l'interpretenon non legge nemmeno 5 ==, ma legge True.
confronto2 = 5 != 5

print(confronto, confronto2)
metaconfronto = confronto == confronto2
print(metaconfronto)

print((2<3) == (5>4)) #True ma senza le parentesi interne False

nome = "Emilian"
#se esiste la stringa nome e si casta in bool il risultato è true se non è scritto niente è false
print(type(nome))
nome_castato = bool(nome)
print(type(nome_castato))
print(nome_castato)

print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(())) #false tupla vuota
print(bool(None)) #false None

print("A" < "B") #anche le stringhe si possono confrontare con < > oltre che con == e !=. Vengono considerati
#i loro valori unicode

#Quali sono gli operatori logici?

#== # Da non confondersi con le assegnazioni
nome = "Emilian" # assegnazione alla variabile nome
nome == "Emilian" # sto controllando se per caso la variabile nome ha come valore proprio la stringa "Emilian"
#!=
#>
#>=
#<
#<=
#and #devono essere True entrambe le variabili booleane affinchè sia True
#or # deve essere True almeno una delle due variabili booleane affinchè sia True
#not # deve essere False affinchè sia True e viceversa

#xor -> definendoli come funzioni od usare le classi per creare ( unione senza intersezione )
# disgiunzione esclusiva 
#nand -> also

ciao = True and False
print(ciao)

ciao2= True or False
print(ciao)

diplomato = True
age = 18

print(f"Puoi fare l'esame di scuola guida? Risposta: {age >= 18 and diplomato}")

grandine = False
pioggia = True

print(f"Devi prendere l'ombrello? {grandine or pioggia}")

nuvole = True

print(f"Devo prendere gli occhiali da sole? {not nuvole}")



























































































