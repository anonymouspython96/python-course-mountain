"""
This is a comment
written in
more than just one line
"""

#This let as assign 3 different variables with the same value
x = y = z = 'Hello World' 

#Insert the correct syntax to assign values to multiple variables in one line:
x,y,z = "Orange", "Banana", "Cherry"

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# Tipo Testuale
messaggio_benvenuto = "Ciao, Emilian!"
print(isinstance(messaggio_benvenuto, str))  # True

# Tipi Numerici
numero_intero = 42
temperatura_celsius = 36.6
numero_complesso = 3 + 4j
print(isinstance(numero_intero, int))         # True
print(isinstance(temperatura_celsius, float)) # True
print(isinstance(numero_complesso, complex))  # True

# Tipi Sequenza
lista_spesa = ["pane", "latte", "uova"]
coordinate_gps = (45.4642, 9.1900)
numeri_range = range(1, 6)
print(isinstance(lista_spesa, list))       # True
print(isinstance(coordinate_gps, tuple))   # True
print(isinstance(numeri_range, range))     # True

# Tipo Mappatura
dati_utente = {"nome": "Emilian", "età": 30}
print(isinstance(dati_utente, dict))       # True

# Tipi Set
insieme_frutti = {"mela", "banana", "kiwi"}
insieme_immortale = frozenset(["sole", "luna", "stelle"])
print(isinstance(insieme_frutti, set))         # True
print(isinstance(insieme_immortale, frozenset))# True

# Tipo Booleano
utente_loggato = True
print(isinstance(utente_loggato, bool))    # True

# Tipi Binari
dati_binari = b"ciao mondo"
buffer_modificabile = bytearray(dati_binari)
vista_memoria = memoryview(dati_binari)
print(isinstance(dati_binari, bytes))         # True
print(isinstance(buffer_modificabile, bytearray))  # True
print(isinstance(vista_memoria, memoryview))  # True

# Tipo None
risultato_operazione = None
print(isinstance(risultato_operazione, type(None)))  # True

print("1. Singolo apice: L'articolo si intitola \'Il ritorno\'")
print("2. Backslash: Attenzione al percorso C:\\Utenti\\Emilian")
print("3. New Line: Prima strofa...\nSeconda strofa.")
print("4. Carriage Return: Progresso: 100%\rErrore.")  # Sovrascrive parte della riga
print("5. Tabulazione: Voce:\tValore")
print("6. Backspace: Prova\b\b\bOK")  # Rimuove "ova" e mostra "PrOK"
print("7. Form Feed: Pagina 1\fPagina 2")  # Nella console, potrebbe non dare effetto visivo

#per crittografia
print("8. Ottale: Codice segreto: \045\040\123")  # Stampa "% S"
print("9. Esadecimale: Messaggio: \x48\x69!")  # Stampa "Hi!"

'''
Method	Description
capitalize()	Converts the first character to upper case 
capitalize()    Converte il primo carattere in maiuscolo!
casefold()	Converts string into lower case
casefold()  Converte una stringa in minuscolo
center()	Returns a centered string
center()    Restituisce una stringa centrata
count()	Returns the number of times a specified value occurs in a string
count() Ritorna quante volte uno specifico valore appare in una stringa
encode()	Returns an encoded version of the string
encode()    Ritorna una versione codificata di stringa
endswith()	Returns true if the string ends with the specified value
endswith()  Restituisce se la stringa finisce o meno con uno specifico valore dato
expandtabs()	Sets the tab size of the string
expandtabs()    Setta la grandezza del tab in una stringa
find()	Searches the string for a specified value and returns the position of where it was found
find()  Cerca e restituisce la posizione di un determinato valore stringa
format()	Formats specified values in a string
format()    Formatta specifici valori in una stringa
format_map()	Formats specified values in a string
format_map()    Formatta specifici valori in una stringa anche lui
index()	Searches the string for a specified value and returns the position of where it was found
index() Cerca qual'è la posizione di un valore stringa in una stringa
isalnum()	Returns True if all characters in the string are alphanumeric
isalnum()   Ritorna se è un carattere interamente alfanumerico o meno
isalpha()	Returns True if all characters in the string are in the alphabet
isalpha()   Ritorna se è un carattere interamente alfabetico
isascii()	Returns True if all characters in the string are ascii characters
isascii()   Ritorna se i caratteri nella stringa sono di tipo ascii
isdecimal()	Returns True if all characters in the string are decimals
isdecimal() Ritorna se i caratteri della stringa sono decimali 
isdigit()	Returns True if all characters in the string are digits
isdigit()   Ritorna se i caratteri nella stringa sono digits
isidentifier()	Returns True if the string is an identifier
isidentifier()  Ritorna se la stringa è un identificatore
islower()	Returns True if all characters in the string are lower case
islower()   Ritorna se tutti i caratteri sono minuscoli
isnumeric()	Returns True if all characters in the string are numeric
isnumeric() Ritorna se i caratteri nella stringa sono numerici
isprintable()	Returns True if all characters in the string are printable
isprintable()   Ritorna se i caratteri della stringa sono stampabili
isspace()	Returns True if all characters in the string are whitespaces
isspace()   Ritorna se i caratteri della stringa sono spazi bianchi
istitle()	Returns True if the string follows the rules of a title
istitle()   Ritorna se la stringa segue le regole da titolo
isupper()	Returns True if all characters in the string are upper case
isupper()   Ritorna se i caratteri della stringa sono interamente maiuscoli
join()	Joins the elements of an iterable to the end of the string
join()  Converge elementi di un iterabile alla fine della stringa
ljust()	Returns a left justified version of the string
ljust() Ritorna a sinistra giustificando la versione della stringa
lower()	Converts a string into lower case
lower() Converte la stringa in minuscolo
lstrip()	Returns a left trim version of the string
lstrip()    Spoglia la stringa a sinistra dagli spazi bianchi
maketrans()	Returns a translation table to be used in translations
maketrans() Ritorna una tabella di traduzione per essere usata in traduzione 
partition()	Returns a tuple where the string is parted into three parts
partition() Ritorna una tupla dove la stringa è partizzata in un albero con rami
replace()	Returns a string where a specified value is replaced with a specified value
replace()   Ritorna una stringa dove uno specifico valore è sostituito con uno specifico valore
rfind()	Searches the string for a specified value and returns the last position of where it was found
rfind() Cerca la stringa per uno specifico valore e ritorna l'ultima posizione in cui è stato trovato
rindex()	Searches the string for a specified value and returns the last position of where it was found
rindex()    Cerca una stringa per uno specifico valore e ritorna l'ultimo punto in cui è stato trovato 
rjust()	Returns a right justified version of the string
rjust() Ritorna a destra justificata la versione della stringa
rpartition()	Returns a tuple where the string is parted into three parts
rpartition()    Ritorna una tupla dove la stringa è parte di parti di albero
rsplit()	Splits the string at the specified separator, and returns a list
rsplit()    Splitta la stringa ad uno specifico valore e ritorna una lista
rstrip()	Returns a right trim version of the string
rstrip()    Ritorna a destra lo spogliamento degli spazi bianchi nelle stringhe
split()	Splits the string at the specified separator, and returns a list
split() Spezza una striga ad una posizione specifica e ritorna una lista
splitlines()	Splits the string at line breaks and returns a list
splitlines()    Spezza la stringa all'acapo e ritorna una lista
startswith()	Returns true if the string starts with the specified value
startswith()    Ritorna se una stringa inizia o meno con uno specifico valore
strip()	Returns a trimmed version of the string
strip() Ritorna un trim della stringa (usata per controlli input)
swapcase()	Swaps cases, lower case becomes upper case and vice versa
swapcase()  Inverte casi, lower case in upper e upper in lower
title()	Converts the first character of each word to upper case
title() Converte il primo carattere di ogni parola in maiuscolo
translate()	Returns a translated string
translate() Ritorna una stringa tradotta
upper()	Converts a string into upper case
upper() Converte una stringa in MAIUSCOLO
zfill()	Fills the string with a specified number of 0 values at the beginning
zfill() Aggiunge un tot di 0 davanti ad una stringa
'''

