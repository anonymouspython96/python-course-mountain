forprint = "ciao mi chiamo Emilian"

# capitalize → Prima lettera maiuscola, il resto minuscolo
# fa della prima lettera di una stringa una maiuscola
print(forprint.capitalize()) # OUTPUT: Ciao mi chiamo emilian

forprint2 = "CIAO MI CHIAMO EMILIAN"
# # casefold → Converte tutto in minuscolo, utile per confronti case-insensitive
# UTILE PER CONFRONTI INSENSITIVE - RENDE UNA STRINGA MINUSCOLA
print(forprint2.casefold()) # OUTPUT: ciao mi chiamo emilian

forprint3 = "Ciaoooo questo è un TEST!"
# # center → Centra la stringa in uno spazio di lunghezza specifica
print(forprint3.center(80, "_")) # OUTPUT: ___________________________Ciaoooo questo è un TEST!____________________________

forprint4 = "Occorrenze di sottostringa"
# # count → Conta le occorrenze di una sottostringa
print(forprint4.count("O")) # OUTPUT: 1

forprint5 = "Questa stringa verrà codificata in bytes grazie a encode()"
# # encode → Codifica la stringa in bytes
print(forprint5.encode()) # OUTPUT: b'Questa stringa verr\xc3\xa0 codificata in bytes grazie a encode()'

forprint6 = "Qua testiamo come se finisce una stringa con un det. valore!"
# # endswith → Verifica se termina con una certa stringa
print(forprint6.endswith("!")) # OUTPUT: True

forprint7 = "   Ciao    "
# # expandtabs → Converte i tab in spazi
print(forprint7.expandtabs(8)) #non ho capito

forprint8 = "Restituisce la posizione di una sotto stringa con find('sottostringa')"
# # find → Restituisce la posizione della sottostringa
print(forprint8.find("sotto")) # OUTPUT: 32

# format → Inserisce valori in una stringa
# dove si inserisce un {} si può sostituire in format("nelle parentesi come sto facendo ora")
print("Ciao {}, oggi impari {}.".format("Emilian", "Python"))

# # format_map → Come format, ma usa un dizionario
#dizionario info
info = {"nome": "Emilian", "linguaggio": "Python"}
print("Ciao {nome}, benvenuto in {linguaggio}!".format_map(info))

forprint9 = "Index tutto minuscolo mi trova la posizione di una parola, e se non la trova triggera un errore!"
# # index → Come find ma lancia un errore se non trova
print(forprint9.index("Index")) # OUTPUT: 0

# # isalnum → Controlla se tutti i caratteri sono alfanumerici
print("Emilian123".isalnum()) # OUTPUT: True

# # isalpha → Solo lettere
print("Emilian".isalpha()) # OUTPUT: True

forprint10 = "()"
# # isascii → Solo caratteri ASCII
print(forprint10.isascii()) # OUTPUT: True

# # isdecimal, isdigit, isnumeric → Tre varianti per numeri
print("123".isdecimal(), "123".isdigit(), "¾".isnumeric()) # OUTPUT: True True True

# # isidentifier → Valido come nome di variabile?
print("variabile_1".isidentifier()) #True

# # islower → Tutto minuscolo?
print("python".islower()) #True

forprint11 = "E' stampabile?!?!?!"
# # isprintable → Tutti i caratteri stampabili?
print(forprint11.isprintable()) #True

# # isspace → Solo spazi?
print("   \t".isspace()) #True

# # istitle → Ogni parola inizia con maiuscola?
print("Ciao Mondo".istitle()) #True

# # isupper → Tutto maiuscolo?
print("CIAo".isupper()) #False

# # join → Unisce elementi iterabili in una stringa
print(" ".join(["Python", "è", "fantastico"])) #output con gli spazi

# # ljust, rjust → Allinea a sinistra o destra 
print("Python".ljust(20, "*"), "Python".rjust(20, "*")) #output: Python************** **************Python

forprint12 = "Tutto controllato che sia minuscolo"
# # lower → Tutto minuscolo per la stringa in questione
print(forprint12.lower())

forprint13 = "  Questi spazi non ci saranno più   "
# # lstrip, rstrip, strip → Rimuove spazi (o caratteri) da sinistra, destra o entrambi
print(forprint13.lstrip()) #a sinistra 
print(forprint13.rstrip()) #a destra
print(forprint13.strip()) #entrambi

forprint14 = "Ciao sono Emi!123"
# # maketrans + translate → Mappatura di caratteri
tabella = str.maketrans("Ciao", "1234") #modifica di stringa avanzata
print(forprint14.translate(tabella))

forprint15 = "Benvenuto, ciao tutto bene? Sei pronto ad imparare Python?"
# # partition, rpartition → Divide in 3 parti al primo/ultimo separatore
print(forprint15.partition("Benvenuto"), forprint15.rpartition("Python")) #primo: partition - ultimo: rpartition

# # removeprefix, removesuffix → Rimuove una parte iniziale/finale
print("TestString".removeprefix("Test").removesuffix("ing")) #rimuove Test e ing : rimane Str

forprint15 = "Python è bella!"
# # replace → Sostituisce testo
print(forprint15.replace("Python", "la programmazione")) # replace() sostituisce la stringa in un altra stringa!

forprint16 = "Troviamo l'ultima occorrenza Python?"
# # rfind, rindex → Trova ultima occorrenza
print(forprint16.rfind("o"), forprint16.rindex("Python")) #stampa l'index dell'ultima occorrenza (33 29)

forprint17 = "Mi splitta quando lo dico io e quanto da destra o da sinistra!"
# # rsplit, split → Divide da destra o da sinistra
print(forprint17.rsplit(" ", 3), forprint17.split()) 
#rsplit prende 2 argomenti separatore logico e index per capire fin dove andare a cercare da destra a sinistra


# # splitlines → Divide sulle nuove righe
multi_line = "prima riga\nseconda riga"
print(multi_line.splitlines())

forprint18 = "Ciao"
# # startswith → Verifica inizio stringa
print(forprint18.startswith("  Ciao")) # OUTPUT: FALSE

forprint19 = "MaiuScole e MinuScole InverTite"
# # swapcase → Inverte maiuscole/minuscole
print(forprint19.swapcase()) # mAIUsCOLE E mINUsCOLE iNVERtITE ( swapcase() )

# # title → Ogni parola con iniziale maiuscola
print("iniziale".title())

# # upper → Tutto maiuscolo
print("upper verrà messo in maiuscolo insieme al resto di questa stringa".upper())

# # zfill → Aggiunge zeri davanti per raggiungere una lunghezza
print("42".zfill(5)) # zfill aggiunge zeri davanti 
#output: 00042




# --------- ALTRI METODI ----------




# Creiamo una lista di esempio
numeri = [10, 20, 30, 40, 50, 60, 70, 80]

# count → Conta quante volte un valore è presente
print(numeri.count(30))  # 1 è IL VALORE DI QUANTE VOLTE ESCE 30 grazie a count(30)

# index → Restituisce la posizione del primo valore trovato
print(numeri.index(50))  # 4

# start, stop, step → Utilizzati nello slicing di liste
# Estraggo elementi dall'indice 2 al 6 escluso, saltando ogni 2
print(numeri[2:6:2])  # [30, 50]

# oppure in un ciclo range()
for i in range(1, 20, 3):  # start=1, stop=10, step=3
    print(i, end=" ")  # Output: 1 4 7 -> stampa 1 e poi aggiunge 3 a uno fino a che non può più (20 limite nel mezzo)

