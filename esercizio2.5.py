# print("inserisci la mail: ")
# # email = input()

# domini = ["gmail.com", "yahoo.it", "tin.it", "hotmail.com"]

# # dominio_email = email.split("@")[1]
# # print("COntrollo in corso... \n")
# # print("************************")
# # print("Controllo dominio gmail: ", dominio_email == "gmail.com")

# #scrivere se una parola è palindroma

# parola = input("Inserisci una parola: ")

# parola_invertita = parola[::-1]
# print(f"Check se la parola inserita è palindroma: {parola.lower() == parola_invertita}")

# #Scrivere un programma che verifichi se una parola è l'anagramma dell'altra

# print("Prima parola: ")
# parola1 = input().lower()
# print("Seconda parola")
# parola2 = input().lower()
# parola1listata = list(parola1).sort()
# parola2listata = list(parola2).sort()
# print("Check sull'anagramma tra le due parole inserite: " + str( parola1listata == parola2listata))

# #Compito per casa: con la funzione dir visualizzare tutti i 
# # metodi degli oggetti visti finora e provare a testarli

print(dir(str))

#['capitalize', 'casefold', 'center', 
# 'count', 'encode', 'endswith', 'expandtabs', 'find', 
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
# 'islower', 'isnumeric', 'isprintable', 'isspace', 
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 
# 'lstrip', 'maketrans', 'partition', 'removeprefix', 
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 
# 'upper', 'zfill'] QUESTI SI

# '__add__', '__class__', '__contains__', '__delattr__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getnewargs__', 
# '__getstate__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__', 
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
# '__rmul__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__' QUESTI NO!

print(dir(range))

#['__bool__', '__class__', '__contains__', '__delattr__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getstate__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__len__', '__lt__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'count', 'index', 'start', 'step', 'stop']