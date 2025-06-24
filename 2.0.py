# OPERATORI DI APPARTENENZA
#Agisce tra un dato e una Collezione. restituiscono un Booleano.


# Agiscono tra un dato ed una collezione. Restituiscono un Booleano. 
# in - not in ( con collezzioni da definire ex: array -> vettori -> caratteri ecc...)

print("a" in "Ciao")

# in -> verifica che un dato appartiene ad una certa collezione di dati. 2 in "pari"? True
# not in -> 4 not in "dispari?" True

# Operatori di Identità 
# Agiscono tra due dati.
#is - is not
#is -> Controlla se una variabile è uguale a un altra -> a is b? True/False
#is not -> Controlla se due dati non sono uguali tra loro -> True / False

#OPERATORI SU SEQUENZE
#Agiscono su du sequenze, quindi su collezioni ordinate di tipo str, list, tuple.

#+ Concatenazione done
#* Ripetizione done
#[i] indicizzazione done
#[start:stop+1:step] slicing
#in appartenenza a una collezione



#Collezioni 
# In python una collezione è un collezione (insieme) di elementi.
# A seconda del tipo di elementi del fatto che si possono moltiplicare o no?! a seconda di come si possono modificare
# a seconda di che operazioni si possono fare tra collezioni diverse, 
# a seconda dell'eventuale organizzazione interna di queste collezioni, cambia la loro tipologia.

# Di tutte queste differenze per il momento classifichiamo le collezioni solo seconodo due criteri. 
#Il tipo di dato collezionato, ed il fatto che sono o meno ordinate.
#stringhe, str() Sono collezioni di caratteri, o meglio di stringhe monodimensionali
stringa1 = "123"
print(stringa1)
print(type(stringa1))

# range -> Sono collezioni ordinate di numeri. Int or Float sintazzi range(partenza, arrivo-1, pass(esempio di uno di due di tre))
print(type(range(28,33)))

for i in range(28, 33):
    print(i) # inizia da 20 finisce 32 ( uno prima )

tabellina_del_5 = range(5, 55, 5)

for n in tabellina_del_5: #tabellina del 5
    print(n)

print(list(tabellina_del_5)) #classe range
print(type(tabellina_del_5))
tabellina_del_5 = list(tabellina_del_5)
print(type(tabellina_del_5))

#Ci sono altre collezioni in python
#  Liste - tipi di dato accettati: caratteri. Ordinata. Immutabile. Accetta Duplicati: si.
#  Tuple - 
#  set -
#  frozenset -
#  dictionary -
#  str() - 
#  range - tipi di dato accettati: int o float. Ordinata. Immutabile. Accetta Duplicati: si.



#Cosa significa "Collezione Ordinata" che ogni elemento può essere identitificato tramite un indice.

#Vediamo ora l'indicizzazione delle sequenze. Essendo ordinato ammettono un indice che mappa gli elementidella 
# sequenza in un insieme di numeri naturali che parte da zero e arriva a n-1, con n numero totale 
# degli elementi della sequenza.

