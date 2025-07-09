# def unicodeforeveryletter_long_version():    
#     alfabeto = "abcdefghiljkmnopqrstuvwxyz"
#     ALFABETO = alfabeto.upper()
#     print(alfabeto, ALFABETO)
#     lunghezza = len(alfabeto)
#     lista_caratteri = alfabeto + ALFABETO
#     contatore = 0 
#     dizionario_Unicode = {}
#     while contatore < 2 * lunghezza:
#         carattere = lista_caratteri[contatore]
#         dizionario_Unicode[carattere] = ord(carattere)
#         contatore += 1

#     print(dizionario_Unicode)

# def unicodeforeveryletter_short_version():
#     alfabeto = "abcdefghiljkmnopqrstuvwxyz"
#     ALFABETO = alfabeto.upper()
#     print(alfabeto, ALFABETO)
#     lista_caratteri = alfabeto + ALFABETO
#     dizionario_Unicode = {c: ord(c) for c in lista_caratteri}
#     return dizionario_Unicode()

# scrivere un programma che mi faccia inserire dei numeri e mi dica se sono numeri primi.
# poi premo 0 per interrompere

def numeri_primi():
    while True:
        try:
            n = int(input("Inserisci un numero primo: (cliccando 0 si chiude il programma!)"))
            if n == 0: break
            
            primo = True
            contatore = n - 1
            while contatore > 1:
                if n % contatore == 0:
                    primo = False
                    break
                contatore -= 1
                
            if primo: 
                print(f"{n} è un numero primo!")
            else: 
                print(f"{n} NON è un numero primo!")
            
        except ValueError:
            print("hai inserito un carattere!")
            