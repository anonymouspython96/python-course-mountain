# l'overloading degli operatori. 
# esempio: palazzo1 + palazz2 = sommaDeiValori(altezza)
# esempio: bambino1 + bambino2 = somma_dei_bambini(peso)
# Python ha un interprete
# Non compila ma interpreta
# Potenzialità ancora da eviscerare

# Concatenazione delle stringhe

num1 = 4
num2 = 5
print(num1 + num2)

# Da input le considera delle stringhe per questo abbiamo bisogno del casting
num3 = str(7)
num4 = str(35)

print(num3+num4) #735 concatenazione

char1 = "s"
char2 = "a"

print(char1+char2) # concatenazione di lettere

#python è case sensitive
#False fa parte delle parole "proibite"
#false minuscolo no
#and è "proibito"
#And è utilizzabile ma è sconsigliato

nome = "Emilian"
Nome = "Giuseppe" # python vede le variabili in maniera differente.
cognome = "Timofei"
# False = "Luigi" Syntax Error: can't assign to false!

#False, così come tutte le parole protette, non possono stare alla sinistra 
#dell'operatore di assegnazione.
#Le parole riservate sono "proibite": 
#esempi: True, False, if, not, and. while. for. in . is . open. None. ecceteraaa
#+ somma 
#- sottrazione
#* moltiplicazione
#** potenza

print(3**3)
print(3**2.5)

#l'elevamento a potenza è una operazione che è ben definita nel campo dei numeri Reali
# solo se l'esponente p un numero razional, cioè che può essere messo sotto forma di frazione.

#/ divisione float, cioè il quoziente è un float, anche se un intero.
print(7/5)
print(10/5) # output float anche se intero

print(10//5) # floor 
# Tronca l'eccesso verzo il basso. [ // ]
print(7/5)
print(10/5)
print(10//5)
print(7//5)

print(-12//7) # Il floor come si vede da questo esempio è 0. Quindi se usiamo // ci avviciniamo a 0 da positivo e ci allontaniamo da negativo.
# Esempio: 1.5 sarà sempre 0. -1.5 sarà sempre 2.

print(-6/5)
print(-6//5)

#resto intero %
print(10%4) #2
print(100%70) #30
print(20%3) #2

#Utilissimo per verificare o generare numeri pari o dispari perchè 
#Qual è la proprietà che definisce un numero pari? [ %2 = 0 ] Even numbers
#La proprietà che definisce un numero dispari è %2 = 1 Odd numbers 

numero1 = 4
numero2 = -6
print(numero1 ** numero2, numero1 // numero2, numero1 % numero2)
