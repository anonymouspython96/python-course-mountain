generic_list = ["acqua", "succo", "coca_cola"]
for y in generic_list:
    print(y) # stanpa tutto ciò che trova in una lista 
    
an_other_loop = ["Ho", "usato", "un", "while", "loop", "!"]
i = 0
while i < len(an_other_loop):
    print(an_other_loop[i])
    i += 1 # !!! WARNING occhio ad usare bene il while 
    
copia_per_verificare_la_memoria_muscolare = ["copia", "per", "verificare", "la", "memoria", "muscolare"]
g = 0
while g < len(copia_per_verificare_la_memoria_muscolare):
    print(copia_per_verificare_la_memoria_muscolare[g])
    g += 1
    
ancora_una_volta_per_la_memoria = ["Ancora", "ancora", "ancora"]
p = 0
while p < len(ancora_una_volta_per_la_memoria):
    print(ancora_una_volta_per_la_memoria[p])
    p += 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list_with_a = []
for x in fruits:
    if "a" in x:
        list_with_a.append(x)

print(list_with_a) # filtra una lista secondo un criterio

newest_list = [item for item in fruits if "a" in item]
print(newest_list) #come su ma più veloce

list_of_cars = ["Volvo", "Mercedes", "Mustang"]
fast_sort_of_a_list = [objecT for objecT in list_of_cars if "o" in objecT]
print(fast_sort_of_a_list) #Volvo 