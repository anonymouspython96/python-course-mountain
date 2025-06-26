mia_stringa="Ciao"

print(type("Ciao")) #string

mio_dict = type({
    "nome": "Emilian"
})

print(mio_dict) #dictionary

print(dir(mio_dict))

mia_lista = [1, 2, 3]

print(type(mia_lista))
print(dir(mia_lista))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', 
'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', 
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 
'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 
'sort'] 
'''

mio_set = {3, 5, 6, 9}
print(dir(mio_set))

'''
['__and__', '__class__', '__class_getitem__', '__contains__', 
'__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__iand__', '__init__', '__init_subclass__', 
'__ior__', '__isub__', '__iter__', '__ixor__', '__le__', 
'__len__', '__lt__', '__ne__', '__new__', '__or__', 
'__rand__', '__reduce__', '__reduce_ex__', '__repr__', 
'__ror__', '__rsub__', '__rxor__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', 
'__xor__', 'add', 'clear', 'copy', 'difference', 
'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 
'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']
'''

mio_frozenset = ([3, 5, 6, 9])
print(type(mio_frozenset))
print(dir(mio_frozenset))

# BASTA RICORDARSI DI USARE dir pe le built-in

'''
Le funzioni build-in son quindi metodi ch non appartengono a 
nessuna classe, ma sono globalmente riconosciute dall'interprete.
'''