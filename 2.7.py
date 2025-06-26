'''
Condizioni
    Sono collegate ai bivi logici, cioè agi if.
    Gli if, elif, else, sono keyword.
    
    ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

import keyword
print(dir(keyword))
print(keyword.kwlist)

'''
    sintassi
    
    if "condizione = True" :
        istruzioni

    Quindi l'if contiene una serie di istruzioni che vengono 
    eseguite se la condizione assume valore booleano True.

'''
#Controllo età
età = input("Inserisci la tua età: ")
età = int(età)
if età >= 18:
    print("Accesso consentito")
else:
    print("Accesso negato")

#Controllo lettera in parola
parola = input("Scegli una parola ed inseriscila: ")
lettera = input("Scegli una lettera di quella parola: ")

if lettera in parola: 
    print(f"La lettera \"{lettera}\" è inclusa nella parola (\"{parola}\")")
else:
    print("Ma ti pare?!")

#se una parola inizia per vocale ..
vocali = "aeiou"
parola = input("Inserisci la parola a cui vuoi controllare la lettera iniziale: ")


if parola[0].lower() in vocali : 
    print(f"La parola \"{parola}\" inizia con una vocale! Bravo!")
else:
    print("Puzzi di ignoranza! :P")



















