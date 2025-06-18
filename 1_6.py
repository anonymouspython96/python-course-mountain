# scrivere un programma che oltre a chiedermi i dati personali
# verifichi se sono maggiorenne e me lo dica
# dopo di che mi chieda una password e mi dica in qualche modo se ho diritto o no all'accesso del mio account
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
età = input("Inserisci la tua età: ") #questo input ( leggi sotto )
sesso = input("Scrivi M se sei maschio o F se sei femmina: ")

riepilogo = str(print(f"Questo è il riepilogo dei dati da te inseriti: nome: {nome}, cognome: {cognome}, età: {età}, Sesso: {sesso}. Se i dati sono corretti procedi all'invio! Se invece i dati non sono corretti reinserisci i dati correttamente. \n"))

età_inferiore = int(età) <= 18 #ricordarsi bene che l'input di sopra è una stringa e quindi doveva essere castata in integer per risolvere il problema

print("Sei risultato: ")
print(età_inferiore)
print("al requisito d'età")

#Per fare anche la password usare gli input

password = input("Inserisci la password: ")
passwordCheck = input("Inseriscila nuovamente: ")
confronto = bool(password == passwordCheck)

messaggio = print(f"L'accesso è in stato di: {confronto}")














