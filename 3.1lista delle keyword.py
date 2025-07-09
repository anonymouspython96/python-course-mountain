'''
    Andimao avanti con il ciclo while.
    while è una keyword. Le keyword sono parole riservate, cioè il cui utilizzo è proibito all'utente.
    Perchè hanno un significato sintattico. Cioè l'interprete python quando vede una keyword la interpreta come un
    qualche comando. Quindi per esempio io posso chiamare una variabile Paperino, ma non posso chiamare una variabile while,
    perchè la interpreta come un comando. L'interprete o il compilatore interpretano le keyword come comandi.
    Posso chiamarla While perchè python è case sensitive, ma è sconsigliato.
    
    Dove si trovano? Nella logica stessa del programma in esecuzione. Allora a che serve il modulo keyword?
    Come tutti i moduli, è una libreria di funzioni.
    
    NB i caratteri di escape, a volte chiamti sequenze di escape, sono dei semplici caratteri, non
    centrano con gli oggetti indicizzabili chiamati sequenze.
'''

# help("keyword")

# #attenzione, il modulo keyword NON contiene le ketword!!!
# #il modulo keyword contiene delle funzioni per compiere aioni relative alle keyword.
# import keyword
# print(dir(keyword))

# software = ["keyboard", "schermo", "mouse"]

# for item in software:
#     print("Item: " + item)
    
# #Iterazione di un range di numeri

# for num in range(10):
#     print(num)
import keyword

print(keyword.kwlist)

'''
    ['False', 
    'None', 
    'True', 
    'and', 
    'as', 
    'assert', 
    'async', 
    'await', 
    'break', 
    'class', 
    'continue', 
    'def', 
    'del', 
    'elif', 
    'else', 
    'except', 
    'finally', 
    'for', 
    'from', 
    'global', 
    'if', 
    'import', 
    'in', 
    'is', 
    'lambda', 
    'nonlocal', 
    'not', 
    'or', 
    'pass', 
    'raise', 
    'return', 
    'try', 
    'while', 
    'with', 
    'yield']
'''

help("while")
# I due punti dopo il while ma anche dopo il for, l'if... eccetera indicano da dove partono le istruzioni, 
# e richiedono 

contatore = 0
while contatore < 4:
    contatore += 1
    print(f"Siamo all'iterazione nr: {contatore}")
else: print("Il ciclo è stato eseguito correttamente")
    




















