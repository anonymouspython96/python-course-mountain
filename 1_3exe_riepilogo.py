#scrivere un programma che simuli la compilazione di un modulo.
# Dovrà salutare l'utente e chiedere tutti i dati personali.
#dopodichè dovrà mostrare all'utente un riepilogo in modo che l'utente
#stesso possa controllare i dati inseriti. Questo riepilogo deve essere
#una sorta di "Scheda personale".



nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
età = input("Inserisci la tua età: ")
sesso = input("Scrivi M se sei maschio o F se sei femmina: ")

riepilogo = str(print(f"Questo è il riepilogo dei dati da te inseriti: nome: {nome}, cognome: {cognome}, età: {età}, Sesso: {sesso}. Se i dati sono corretti procedi all'invio! Se invece i dati non sono corretti reinserisci i dati correttamente. \n"))

# \n \t questi comandi sono escapes
# \n mette uno spazio riga sotto una riga
# \t questo è un tab

print("Ora facciamo un esempio per scrivere le virgolette: \t \"")
print("Tra il \"dire\" ed il \"fare\" c'è di mezzo il mare")