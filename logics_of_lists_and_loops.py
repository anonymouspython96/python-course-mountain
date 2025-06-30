list_non_ordinata = ["non", "alfanumericamente", "ordinato"]
list_non_ordinata.sort()
print(list_non_ordinata) # ['alfanumericamente', 'non', 'ordinato']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # stessa cosa con i numeri -> [23, 50, 65, 82, 100]

thislist_reverse_sorting = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist_reverse_sorting.sort(reverse = True)
print(thislist_reverse_sorting) # ordinati al contrario ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist_reverse_numbers = [100, 50, 65, 82, 23]
thislist_reverse_numbers.sort(reverse = True)
print(thislist_reverse_numbers) # ordinati al contrario grazie a reverse = True in sort() [100, 82, 65, 50, 23]

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist_for_experiments = [100, 50, 65, 82, 23]
thislist_for_experiments.sort(key = myfunc)
print(thislist_for_experiments) # [50, 65, 23, 82, 100]

#Case sensitive sorting can give an unexpected result: 
# per esempio se il sort viene attivato e ci sono dati con maiuscole e minuscole
#  in questo caso meglio usare .lower -> thislist.sort(key = str.lower)