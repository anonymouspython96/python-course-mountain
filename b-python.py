alunni = ['Giovanni', 'Giuseppe', 'Maria', 'Luca', 'Maddalena', 'Emmanuele', 'Gregorio']
print(alunni)

#estrapolare Gregorio
print(alunni[-1])

#estrapolare la lunghezza della lista
alunni[-1] = "Emilian"

print(alunni)

if ("a" not in "aeiou"):
    print("False")
else: 
    print("True") # è strano ma è come dire non c'è (controllalo) 

for x in alunni: #iterazione ( ci stampa tutti gli elementi di una lista )
    print(x)

unità_di_misura = ("metri", "litri", "grammi")

for y in unità_di_misura: #iterazione di una tupla
    print(y)

#Gli elenchi che supportano gli operatori di appartenenza si chiamano container.

list1 = ["apple", "banana", "cherry"] #strighe 
list2 = [1, 5, 7, 9, 3] #numeri (int)
list3 = [True, False, False] #booleani 
list4 = ["abc", 34, True, 40, "male"]

print(list1, list2, list3)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:2]) # è come dire dall'inizio al 3° elemento escluso
print(thislist[1:4]) # dal secondo al terzo quindi "banana" "cherry" e "orange"
print(thislist[4:]) #dal 5 elemento in poi

#pensa + se si trova a sinistra pensa meno se si trova a destra

if "apple" in thislist: 
    print("\"apple\" it's in the list")

# OGGETTO: ragruppamento di attributi e metodi
    thislist2 = ["apple", "banana", "cherry"]
    thislist2[1:2] = ["blackcurrant", "watermelon"]
    print(thislist2) #li aggiunge alla lista levando "banana"

    thislist3 = ["apple", "banana", "cherry"]
    thislist3[1:3] = ["watermelon"]
    print(thislist3) # sostituisce anche altri elementi se con lo slice si supera il len degli elementi

argomenti_scolastici = ["matematica", "fisica"]
argomenti_scolastici.insert(2, "geografia")
print(argomenti_scolastici) # output: ['matematica', 'fisica', 'geografia'] 

oggetti_di_casa = ["panno", "padella", "appendino (se capisce)"]

oggetti_di_casa.append("scopa") #aggiunge scopa alla lista

print(oggetti_di_casa) 

oggetti_di_casa.insert(2, "sedia")

print(oggetti_di_casa) #entra dopo l'indice 1

# ora userò extend

thislist1_2 = ["apple", "banana", "cherry"]
tropical1_2 = ["mango", "pineapple", "papaya"]

thislist1_2.extend(tropical1_2)

print(thislist1_2)

#output -> ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#usando extend posso unire una lista con una tupla

listamia = ["ciao"]
tuplamia = ("ciao")
listamia.extend(tuplamia)
print(type(listamia)) # <class 'list'>

thislistthatremove = ["apple", "banana", "cherry"]
thislistthatremove.remove("banana") # banana verrà eliminato
print(thislistthatremove)

listadellaspesa=["cibo del gatto", "cacca finta", "farina", "birra"]
listadellaspesa.pop(1)
print(listadellaspesa) 
#If you do not specify the index, the pop() method removes the last item.

#The del keyword also removes the specified index:

del listadellaspesa[0]
print(listadellaspesa)

#del può eliminare la lista completamente
#The clear() method empties the list.

#The list still remains, but it has no content.