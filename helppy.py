import keyword
import sys
import pkgutil

def print_help_keywords():
    print("=== KEYWORDS ===")
    for kw in keyword.kwlist:
        print(f"\nHelp for keyword: {kw}")
        help(kw)

def print_help_builtin_objects():
    print("\n=== BUILTIN OBJECTS ===")
    builtins = ['int', 'str', 'list', 'dict', 'set', 'tuple', 'float', 'bool', 'complex', 'bytes', 'object']
    for obj_name in builtins:
        obj = eval(obj_name)
        print(f"\nHelp for {obj_name}:")
        help(obj)

def print_help_modules():
    print("\n=== MODULES ===")
    for module_info in pkgutil.iter_modules():
        name = module_info.name
        try:
            module = __import__(name)
            print(f"\nHelp for module: {name}")
            help(module)
        except Exception as e:
            print(f"Could not import module {name}: {e}")

# Scegli cosa eseguire, per non stampare troppo testo puoi commentare alcune righe

# print_help_keywords()           # ATTENZIONE: Alcune keyword non hanno help!
print_help_builtin_objects()      # Stampa l'help per i tipi base
# print_help_modules()            # MOLTO LUNGO: stampa l'help di tutti i moduli installati

