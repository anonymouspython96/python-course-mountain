# # Ciclo for
# # help('for')
# # The "for" statement
# # *******************

# # The "for" statement is used to iterate over the elements of a sequence
# # (such as a string, tuple or list) or other iterable object:

# #    for_stmt ::= "for" target_list "in" starred_list ":" suite
# #                 ["else" ":" suite]

# # The "starred_list" expression is evaluated once; it should yield an
# # *iterable* object.  An *iterator* is created for that iterable. The
# # first item provided by the iterator is then assigned to the target
# # list using the standard rules for assignments (see Assignment
# # statements), and the suite is executed.  This repeats for each item
# # provided by the iterator.  When the iterator is exhausted, the suite
# # in the "else" clause, if present, is executed, and the loop
# # terminates.

# # A "break" statement executed in the first suite terminates the loop
# # without executing the "else" clause\u2019s suite.  A "continue" statement
# # executed in the first suite skips the rest of the suite and continues
# # with the next item, or with the "else" clause if there is no next
# # item.

# # The for-loop makes assignments to the variables in the target list.
# # This overwrites all previous assignments to those variables including
# # those made in the suite of the for-loop:

# #    for i in range(10):
# #        print(i)
# #        i = 5             # this will not affect the for-loop
# #                          # because i will be overwritten with the next
# #                          # index in the range

# # Names in the target list are not deleted when the loop is finished,
# # but if the sequence is empty, they will not have been assigned to at
# # all by the loop.  Hint: the built-in type "range()" represents
# # immutable arithmetic sequences of integers. For instance, iterating
# # "range(3)" successively yields 0, 1, and then 2.

# # Changed in version 3.11: Starred elements are now allowed in the
# # expression list.

# # Related help topics: break, continue, while
# '''
#     Try strings,
#     lists,
#     dictionaries, and even
#     custom iterables.
# '''

# mia_stringa = "Ciao"
# mia_stringa = "Bohhh"
# # mia_stringa[2] = "z" TypeError: 'str' object does not support item assignment

# for x in mia_stringa:
#     print(x)

# mia_lista = ["abba", "acdc", "iron mainden", "metallica"]
# for y in mia_lista:
#     print(y)

# dictio = {
#     "Reno" : "Matematica",
#     "Giuseppe" : "Geografia"  ,
#     "Lordo" : "Fisica"
# }

# for nome in dictio:
#     print(f"L'alunno {nome} studia {dictio[nome]}")

# # nome da solo nel for ci prende il valore della chiave
# # nome del dizionario con nome tra [] concatenati nel print mi stampano le chiavi

# for paperino in ["a", 125, 2.7, True]:
#     #al primo ciclo il valore del primo elemento incotrato dal for, che in questo
#     #caso è "a", verrà temporaneamente caricato nella variabile paperino, che quindi
#     # verrà temporaneamente valutata come stringa, senza necessità di essere pre-dichiarata.
#     # Al punto tale che ad ogni icclo potrebbe anche assumere valori con type diverso.
#     print(paperino) # stamperà il valore che al momento ha la variabile paperino.
#     # fine ciclo. Quindi passa all'elemento verrà caricato temporaneamente
#     # nella variabile paperino, che quindi questa volta verrà interpretata come intero.
#     #
#     #se io ho come iteratore una stringa, che è fatta solo di caratteri, o un range,
#     #che è fatto solo di numeri, allora i valori che assumerà paperino saranno omogenei.
#     #Ma se per esempio il mio iteratore ha elementi di tipo diverso, anche
#     #paperino assumerà valori non omogenei tra loro.

# if "a" in ["a", 125, 2.7, True]:
#     print("trovato!")

# for pippo in ["a", 125, 2.7]:
#     print("Ciao!")
#     '''
#     primo ciclo: pippo assume il valore "a", e viene eseguita l'istruzione,
#     che in questo caso ultraspecifico non coinvolge pippo.
#     Quindi pippo vale "a", che faccio? Lo uso? No, stampo ciao.
#     Poi pippo vale 125. Che faccio? Ristampo ciao.
#     eccettera.
#     '''

# for pluto in (1,57,0.22):
#     print("Ciao!")

# for lettera in "Abracadabra":
#     print(lettera)
#     # per 11 volte ha assunto un valore, che in questo caso essendo il mio iterabile
#     '''
#     una stringa saranno solo caratteri, e poi ha eseguito l'istruzione.
#     lettera in questo caso abbiamo detto che è una variabile.
#     Le variabili supportano l'assegnazione. Cioè posso stare alla SINISTRA dell'uguale.
#     lettera = "A"
#     lettera = "b"
#     lettera = "c"
#         i valori invece stanno a DESTRA
#     '''

# for valore in ["a", 33, "Ciao", True, None, complex(3,2), False, 3.6]:
#     if valore == bool(valore):
#         print("Salve!")

# '''
# per qualche motivo ho bisogno che mi scriva Salve solo quando, scorrendo la mia iterabile, trova un valore intero.
# '''

# for valore in ["a", 33, "Ciao", True, None, complex(3,2), False, 3.6]:
#     if type(valore) == type(bool):
#         print("Salvino!")

# print(type(int))

# '''
#     Storicamente il ciclo for è stato inventato per ripetere istruzioni sempre uguali
#     senza sforzo, quindi come il while, ma con la possibilità di avere un indice.

#     Per esempio: facciamo 2 esercizi: stampare 10 volte "1", oppure stampare i numeri da 1 a 10, col while e col for. Il for si intende questa volta utilizzato nella maniera pià elementare.
# '''

# # help(range)

# for n in range(38, 42, 2):
#     '''

#  |  start 38
#  |
#  |  step 2
#  |
#  |  stop 42

#     '''
#     print("1")

# for n in range(10):
#     print(2)

# contatore = 0
# while contatore < 10:
#     print(3)
#     contatore += 1

# for n in range(10):
#     print(n+1) #da uno a 10

# contatore = 0
# while contatore < 10:
#     contatore += 1
#     print(contatore) #da uno a 10

# # stampiamo uno per uno tutte le vocali di una stringa inserita dall'utente.

# print("Inserisci una parola: ")
# parola = input().lower()
# vocali_minuscole = "aeiou"

# for lettera in parola:
#     if lettera in vocali_minuscole:
#         print(lettera)

# Vorrei sommare tutti i numeri compresi tra 87 e 121

# somma = 0

# for n in range(87, 122):
#     somma += n
# print(somma)

"""
Scriviamo un programma che chiede all'utente di inserire dei numeri interi, e me li somma solo se sono compresi tra 87 e 121. Non appena inserisco un numero non compreso tra 87 e 121 il programma esce e restituisce la somma dei numeri eventualmente inseriti.
"""


def sum_in_range():
    contatore = 0
    while True:
        try:
            n = int(input("Inserisci i numeri della consegna consentiti (altrimenti non te li somma): "))
            condizione = range(87, 122)

            if n in condizione:
                contatore += n
                print(f"La somma attuale è: {contatore}")

            elif n != condizione:
                break

        except ValueError:
            print("Non inserire lettere, inserisci solo numeri.")

# for n in range(87, 121):
#     print(n)

#stampa la tabellina del 7

for n in range(7, 71, 7):
    print(n)
    
# tabellina dinamica
def Tabellina():
    rang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tabellina = int(input("Inserisci il numero di cui vuoi sapere la tabellina: "))
    for n in rang:
        print(n*tabellina)
    
#trovare il massimo in un insieme di numeri che inserisco da tastiera.
# Senza usare max() ma usando il ciclo 

'''
    Rifare l'esercizio con la seguente modalità di inserimento: i numeri non 
    verranno inseriti uno a uno con l'invio, ma su un unica riga di input separati l'uno dall'altro dallo spazio. 
        suggerimento: i numeri dovranno quindi essere separati con qualche metodo che molto probabilmente avrà la classe stringa.
'''
def massimo():
    Max = 0
    lista_numeri = []
    while True:
        numbers = int(input("Inserisci i numeri interi e premi invio ogni volta: "))
        if numbers == 0: break
        lista_numeri.append(numbers)
        Max = lista_numeri[0]
    for n in range(len(lista_numeri)):
        if lista_numeri[n] > Max:
            Max = lista_numeri[n]
    print(Max)
    
def massimo_diverso():
    Max = 0
    lista_numeri = []
    while True:
        numbers = int(input("Inserisci i/il numeri/o interi/o e premi invio: "))
        if numbers == 0: break
        lista_numeri.append(numbers)
    Max = lista_numeri[0]
    for n in lista_numeri:
        if n > Max: 
            Max = n
    print(Max)

def massimo_da_una_stringa():
    Max = 0
    print("Inserisci i numeri dei quali vuoi trovare il massimo, tutti in una sola riga separandoli dallo spazio: ")
    numeri = input()
    lista_numeri_stringhe = numeri.split()
    lista_numeri = [int(x) for x in lista_numeri_stringhe]
    # definire il singolo elemento come numero e ciclare la lista per ottenere in [parentesi quadre i numeri inseriti] 
    '''
    se no lo si può fare con append creando una lista vuota
    '''
    Max = lista_numeri[0]
    for n in lista_numeri:
        if n > Max: 
            Max = n
    print(Max)

def famiglia_backend():
    try:
        numero = int(input("Inserisci un numero intero: "))
        print("Hai inserito:", numero)
    except ValueError:
        print("Ops! Non hai inserito un numero valido.")
    else:
        print("Tutto è andato bene.")
    finally:
        print("Fine del programma.")
