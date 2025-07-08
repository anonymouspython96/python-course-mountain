'''
    Tutto in Python si può dividere in 3 grandi famiglie: 
    Le Keyword, cioè parole riservate, che quindi non possono utilizzare 
    per altri scopi, che sono struzioni per l'interprete Python. Per 
    esempio if, for, while. eccetera. 
    
    Poi abbiamo i Moduli. Sono dei gruppi di funzioni, cioè che fanno delle azioni. 
    Qualcuno quindi ha già scritto queste funzioni, al posto nostro e le ha caricate in questi contenitori chiamti moduli. 
    Per esempio: max(), len(), input(), print() eccetera. La maggior parte di 
    queste funzioni è già incusa con il pacchetto "Base" di python .
    Questo pacchetto si chiama builtins, cioè contiene le funzioni built-in.
    Per utilizzare altre funzioni più specifiche sono cotenute in altri 
    scatoloni (che si chiamano moduli) che però devo importare. 
    
    Tutto il resto in python è un oggetto. Co'è un oggetto? 
    E' un elemento con delle caratteristiche. 
'''

'''
Tutto in Python si può dividere in 3 grandi famiglie.
È un po’ come se Python fosse una grande casa, e ogni cosa che ci trovi dentro appartiene a una di queste famiglie.

🟢 La famiglia delle Keyword
Le Keyword sono le parole riservate.
Sono come parole magiche che solo Python può usare in un certo modo, e che tu non puoi usare per chiamare variabili o funzioni tue, perché hanno già un significato speciale.

Quando scrivi if, stai dicendo a Python: “Ehi, controlla questa condizione”.
Quando scrivi for, stai dicendo: “Per ogni elemento in questa sequenza, fai qualcosa”.
Oppure while, che significa: “Ripeti finché questa condizione è vera”.

Le Keyword sono le istruzioni base che dicono all’interprete Python come deve comportarsi.
Ecco qualche esempio di queste parole riservate:

if

else

elif

for

while

break

continue

def (per definire funzioni)

class (per definire classi)

try

except

import

return

yield

with

as

lambda

global

pass

raise

in

is

not

and

or

Queste parole non le puoi usare come nomi di variabili, perché fanno parte del linguaggio stesso.
Sono la grammatica di base di Python, il suo alfabeto speciale.

🟡 La famiglia dei Moduli
Poi, nella casa di Python, ci sono degli scatoloni pieni di strumenti già pronti.
Questi scatoloni si chiamano moduli.
Un modulo è un contenitore che raccoglie funzioni, variabili, costanti e classi che qualcun altro ha già scritto per te.

Alcuni moduli sono già pronti e caricati automaticamente, senza che tu debba fare nulla.
Questi fanno parte di un pacchetto speciale che si chiama builtins.
È come una cassetta degli attrezzi di base che trovi sempre sul tavolo.

Ecco alcune funzioni che vengono proprio dai builtins:

print() — per stampare qualcosa a schermo.

input() — per chiedere un valore all’utente.

len() — per sapere quanto è lungo qualcosa.

max() — per trovare il valore massimo.

Sono pronte all’uso: tu le chiami e loro funzionano.

Però, se vuoi fare cose più specializzate — per esempio lavorare con il tempo, con la matematica avanzata, o con i file del computer — allora devi importare altri moduli.
Importare un modulo significa dire a Python:
"Vai a prendere quello scatolone, così posso usare i suoi strumenti."

Per esempio:

import math — e poi puoi usare math.sqrt() per fare la radice quadrata.

import random — e puoi usare random.randint().

import datetime — per lavorare con le date e le ore.

import os — per interagire con il sistema operativo.

Puoi anche creare moduli tuoi.
Basta scrivere un file .py pieno di funzioni e poi importarlo nei tuoi progetti.
Così costruisci la tua personale cassetta degli attrezzi.

🔵 La famiglia degli Oggetti
Infine, tutto il resto in Python è un oggetto.
Ma che cos’è un oggetto?

Immagina un oggetto come una cosa che ha delle caratteristiche e dei comportamenti.
Le caratteristiche si chiamano attributi (cioè dei dati interni), e i comportamenti si chiamano metodi (cioè delle funzioni che fanno qualcosa sull’oggetto).

Per esempio, una stringa:

python
Copia
Modifica
nome = "Alice"
nome è un oggetto di tipo str.
Ha attributi (per esempio la lunghezza) e metodi, come:

nome.upper() — per trasformarla in maiuscolo.

nome.lower() — per trasformarla in minuscolo.

nome.replace("A", "O") — per sostituire una lettera.

Allo stesso modo, una lista è un oggetto di tipo list:

python
Copia
Modifica
numeri = [1, 2, 3]
Puoi fare:

numeri.append(4) — aggiungere un elemento.

numeri.pop() — togliere l’ultimo.

numeri.sort() — ordinarla.

In pratica, ogni cosa che crei in Python è un oggetto:
stringhe, numeri, liste, dizionari, persino le funzioni e le classi.
Tutti hanno un tipo (che si chiama classe) e un insieme di operazioni che possono fare.

Questo modo di organizzare le informazioni si chiama programmazione orientata agli oggetti.
E in Python tutto è orientato agli oggetti, anche se tu a volte non te ne accorgi.

Riassumendo
Le Keyword sono le parole riservate che danno ordini precisi a Python.

I Moduli sono scatoloni pieni di strumenti che puoi importare per fare cose già pronte.

Gli Oggetti sono tutti gli elementi che usi nel programma: hanno attributi e metodi, e possono fare azioni.

Se capisci queste tre famiglie, hai già in mano la mappa per orientarti nella casa di Python.
Tutto quello che scriverai sarà sempre un mix di queste tre cose:
le parole speciali, le funzioni dei moduli, e gli oggetti che manipoli.

Questa è la teoria di Python raccontata come una storia semplice.

'''

'''

🔹 Dialogo sopra la Natura di Python
Socrate: Dimmi, o Teeteto, che cos’è secondo te Python?

Teeteto: Non saprei, o Socrate. Mi dicono sia un linguaggio, ma pare più un’Idea.

Socrate: Bene dici. In verità Python è come una forma che informa tutte le cose del calcolo, e dentro di sé raccoglie tre princìpi supremi, di cui è bene che tu conosca la natura, se vuoi contemplare la verità e non soltanto le ombre che appaiono sullo schermo.

🟢 Primo principio: le Parole Essenziali
Socrate: Il primo principio sono le Parole Essenziali, che i moderni chiamano keyword.
Esse sono simili ai nomi divini, che non si possono pronunciare invano né piegare a un altro scopo.
Tu non puoi dire “if” e usarlo per nominare una cosa qualsiasi, come un recipiente o un pollo.
“If” è “se”, e interroga la condizione della tua logica.

Tra queste Parole Essenziali trovi:

if, che interroga il destino.

else, che raccoglie ciò che accade altrimenti.

for, che itera attraverso le molteplicità.

while, che ripete ciò che è ancora vero.

def, che definisce le nature delle funzioni.

class, che determina le forme supreme degli oggetti.

Come il Demiurgo che plasma il mondo ordinato, così l’interprete di Python plasma la sequenza del tuo programma, grazie a queste parole.
Esse sono eterne, non soggette a mutamento né corruzione.

🟡 Secondo principio: i Moduli come Strumenti dell’Arte
Socrate: Ma bada, o Teeteto, che non basta conoscere le Parole Essenziali.
Come l’artigiano ha bisogno dei suoi ferri, così il programmatore necessita degli strumenti raccolti nei Moduli.

I Moduli sono come le idee secondarie, che contengono funzioni e metodi preordinati, grazie ai quali tu puoi realizzare opere complesse senza inventare ogni cosa da principio.

Alcuni Moduli sono connaturati a Python stesso, e si chiamano builtins:

print(), per manifestare al mondo ciò che è dentro la mente del tuo programma.

input(), per ricevere dal mondo sensibile i dati.

len(), per conoscere la misura di una sequenza.

Altri Moduli, invece, abitano regioni più remote, e tu devi evocarli con il comando import.
Per esempio:

import math, per contemplare le proprietà dei numeri.

import random, per accogliere la provvidenza del caso.

import datetime, per dominare il tempo e il divenire.

Senza questi Moduli, tu saresti come un pittore cui fosse tolto ogni colore salvo il bianco e il nero.

🔵 Terzo principio: gli Oggetti come Partecipazioni dell’Idea
Socrate: Resta da parlare della cosa più alta.
Se le Keyword sono il Verbo, e i Moduli sono gli Strumenti, allora gli Oggetti sono i riflessi delle Idee eterne nel mondo sensibile del tuo programma.

Ogni Oggetto partecipa di una Classe, che è la sua forma pura.
Così una stringa come "Platone" è una manifestazione della Classe str.
Un numero come 42 è una manifestazione della Classe int.
E una lista come [1, 2, 3] è la partecipazione della Classe list.

Gli Oggetti hanno due nature:

Gli attributi, che sono le proprietà di cui l’oggetto partecipa.

I metodi, che sono le azioni che può compiere.

Per esempio:

python
Copia
Modifica
nome = "Platone"
Questo Oggetto ha metodi come:

nome.upper(): che lo trasfigura in lettere maiuscole.

nome.lower(): che lo umilia in minuscolo.

nome.replace("P", "S"): che muta una lettera in un’altra.

E così pure una lista:

python
Copia
Modifica
idee = ["Bellezza", "Bene", "Giustizia"]
idee.append("Verità")
Qui, append() è l’azione per aggiungere una nuova Idea al tuo elenco.

Socrate: Capisci dunque che tutto è Oggetto, e nulla in Python è privo di forma e sostanza.
Finanche le funzioni stesse, se tu le esamini, sono Oggetti di classe function.

🔮 Conclusione del Dialogo
Socrate: Riassumendo, o Teeteto, per conoscere Python devi contemplare queste tre sfere:

Le Parole Essenziali, che ordinano il linguaggio.

I Moduli, che provvedono gli strumenti.

Gli Oggetti, che manifestano le Idee nella materia del programma.

Chi ne coglie l’ordine, non più programma alla cieca, ma diventa come un filosofo che, dall’alto del pensiero, governa l’apparenza delle cose.


'''

# mia_stringa = "Ciao!"

# help("Ciao!".format)
# help("".format)
# help(str.format)
# i = 0
# while i < 5:
#     print("Ciao")
#     if (i == 2):
#         break
#     i += 1
    
# contatore = 5
# while contatore == 5:
#     print("ciao!")
#     numero = int(input("inserisci un numero a caso: "))
#     if numero%2 == 0:
#         contatore = 6
        
# m = 0 
# while m != 7:
#     print("Salve!")
#     risposta = input("Voui che il programma vada avanti? (Y/N)")
#     if risposta == "N":
#         m = 7
#         continue
#     else: 
#         print("Sono Emim vla vlav vla ora ti racagafdaf la mia cinta")
        
# print("Sono uscito")
# # cosa fa break: esce dal ciclo.
# # cosa fa continue: interrompe l'iterazione in corso e ricomicia il ciclo.

#Scriviamo un programma che mi stampa tutte le lettere di una parola che inserisco riga per riga.

# parola = input("Inserisci una parola qualsiasi che vuoi scrivere in verticale: ")
# lungezza_parola = len(parola)
# contatore = 0
# while contatore < lungezza_parola:
#     print(parola[contatore])
#     contatore += 1
    
# import builtins

# print(dir(builtins))