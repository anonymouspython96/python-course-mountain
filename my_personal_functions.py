def break_loops(len_loop):
    contatore = 0
    while contatore < len_loop:
        contatore += 1
        print(f"We are now in the iteration number: {contatore}")
        risposta = input("Push \"s\" to stop the iteration, other key to continue!")
        if risposta == "s":
            break
    else: print("The end of the iteration.") 
    # così ho anche un controllo ed un metodo più intuitivo e "supportivo"
    # per programmare
    
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