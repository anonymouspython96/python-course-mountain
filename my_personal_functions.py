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
    
