# Ciclo for 
# help('for') 
# The "for" statement
# *******************

# The "for" statement is used to iterate over the elements of a sequence
# (such as a string, tuple or list) or other iterable object:

#    for_stmt ::= "for" target_list "in" starred_list ":" suite
#                 ["else" ":" suite]

# The "starred_list" expression is evaluated once; it should yield an
# *iterable* object.  An *iterator* is created for that iterable. The
# first item provided by the iterator is then assigned to the target
# list using the standard rules for assignments (see Assignment
# statements), and the suite is executed.  This repeats for each item
# provided by the iterator.  When the iterator is exhausted, the suite
# in the "else" clause, if present, is executed, and the loop
# terminates.

# A "break" statement executed in the first suite terminates the loop
# without executing the "else" clause\u2019s suite.  A "continue" statement
# executed in the first suite skips the rest of the suite and continues
# with the next item, or with the "else" clause if there is no next
# item.

# The for-loop makes assignments to the variables in the target list.
# This overwrites all previous assignments to those variables including
# those made in the suite of the for-loop:

#    for i in range(10):
#        print(i)
#        i = 5             # this will not affect the for-loop
#                          # because i will be overwritten with the next
#                          # index in the range

# Names in the target list are not deleted when the loop is finished,
# but if the sequence is empty, they will not have been assigned to at
# all by the loop.  Hint: the built-in type "range()" represents
# immutable arithmetic sequences of integers. For instance, iterating
# "range(3)" successively yields 0, 1, and then 2.

# Changed in version 3.11: Starred elements are now allowed in the
# expression list.

# Related help topics: break, continue, while
'''
    Try strings, 
    lists, 
    dictionaries, and even 
    custom iterables.
'''

mia_stringa = "Ciao"
mia_stringa = "Bohhh"
# mia_stringa[2] = "z" TypeError: 'str' object does not support item assignment

for x in mia_stringa:
    print(x)
    
mia_lista = ["abba", "acdc", "iron mainden", "metallica"]
for y in mia_lista:
    print(y)
    
dictio = {
    "Reno" : "Matematica",
    "Giuseppe" : "Geografia"  ,
    "Lordo" : "Fisica"  
}

for nome in dictio:
    print(f"L'alunno {nome} studia {dictio[nome]}")
    
# nome da solo nel for ci prende il valore della chiave
# nome del dizionario con nome tra [] concatenati nel print mi stampano le chiavi
