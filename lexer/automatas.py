# Todos los automatas reciben un lexema y devuelven:
#   - FINAL     : si el lexema es aceptado por el automata.
#   - NO FINAL  : si el lexema no es aceptado pero tiene posibilidad de serlo.
#   - TRAMPA    : si el lexema nunca va a poder ser aceptado por el automata.

def afd_der_paren(lexema):
    if lexema == ")":
        return "FINAL"
    else:
        return "TRAMPA"


def afd_izq_paren(lexema):
    if lexema == "(":
        return "FINAL"
    else:
        return "TRAMPA"


def afd_id(lexema):
    estados = ['A', 'B', 'T']
    estados_finales = ['B']
    estado_actual = 'A'
    for c in lexema:
        if estado_actual == 'A' and c.isalpha():
            estado_actual = 'B'
        elif estado_actual == 'B' and c.isalnum():
            estado_actual = 'B'
        else:
            estado_actual = 'T'
            break

    if estado_actual in estados_finales:
        return "FINAL"
    else:
        return "TRAMPA"


def afd_num(lexema):
    if lexema.isnumeric():
        return "FINAL"
    else:
        return "TRAMPA"


def afd_puntoycoma(lexema):
    if lexema == ";":
        return "FINAL"
    else:
        return "TRAMPA"


# Esta funcion toma un lexema, una tabla de transicion en forma de un
# diccionario de python, una lista de estados finales, y un estado inicial.
# Es usada por los automatas debajo para calcular si un lexema es aceptado o no.
def automata_por_tabla(lexema, tabla, estados_finales, estado_inicial):
    estado_actual = estado_inicial
    for c in lexema:
        if c in tabla[estado_actual]:
            estado_actual = tabla[estado_actual][c]
        else:
            estado_actual = 'T'
            break
    if estado_actual in estados_finales:
        return "FINAL"
    elif estado_actual == 'T':
        return "TRAMPA"
    else:
        return "NO FINAL"


def afd_entonces(lexema):
    tabla = {
        'A': {'e': 'B'},
        'B': {'n': 'C'},
        'C': {'t': 'D'},
        'D': {'o': 'E'},
        'E': {'n': 'F'},
        'F': {'c': 'G'},
        'G': {'e': 'H'},
        'H': {'s': 'I'},
        'I': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["I"], "A")


def afd_equal(lexema):
    tabla = {
        'A': {'e': 'B'},
        'B': {'q': 'C'},
        'C': {'u': 'D'},
        'D': {'a': 'E'},
        'E': {'l': 'F'},
        'F': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["F"], "A")


def afd_finfunc(lexema):
    tabla = {
        'A': {'f': 'B'},
        'B': {'i': 'C'},
        'C': {'n': 'D'},
        'D': {'f': 'E'},
        'E': {'u': 'F'},
        'F': {'n': 'G'},
        'G': {'c': 'H'},
        'H': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["H"], "A")


def afd_finsi(lexema):
    tabla = {
        'A': {'f': 'B'},
        'B': {'i': 'C'},
        'C': {'n': 'D'},
        'D': {'s': 'E'},
        'E': {'i': 'F'},
        'F': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["F"], "A")


def afd_func(lexema):
    tabla = {
        'A': {'f': 'B'},
        'B': {'u': 'C'},
        'C': {'n': 'D'},
        'D': {'c': 'E'},
        'E': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["E"], "A")


def afd_hasta(lexema):
    tabla = {
        'A': {'h': 'B'},
        'B': {'a': 'C'},
        'C': {'s': 'D'},
        'D': {'t': 'E'},
        'E': {'a': 'F'},
        'F': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["F"], "A")


def afd_leer(lexema):
    tabla = {
        'A': {'l': 'B'},
        'B': {'e': 'C'},
        'C': {'e': 'D'},
        'D': {'r': 'E'},
        'E': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["E"], "A")


def afd_mostrar(lexema):
    tabla = {
        'A': {'m': 'B'},
        'B': {'o': 'C'},
        'C': {'s': 'D'},
        'D': {'t': 'E'},
        'E': {'r': 'F'},
        'F': {'a': 'G'},
        'G': {'r': 'H'},
        'H': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["H"], "A")


def afd_repetir(lexema):
    tabla = {
        'A': {'r': 'B'},
        'B': {'e': 'C'},
        'C': {'p': 'D'},
        'D': {'e': 'E'},
        'E': {'t': 'F'},
        'F': {'i': 'G'},
        'G': {'r': 'H'},
        'H': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["H"], "A")


def afd_opmult(lexema):
    tabla = {
        'A': {"*": "B", "/": "B"},
        'B': {},
        'T': {},
    }
    return automata_por_tabla(lexema, tabla, ["B"], "A")


def afd_oprel(lexema):
    tabla = {
        'A': {">": "B", "<": "C", "=": "D"},
        'B': {"=": "D"},
        'C': {">": "D", "=": "D"},
        'D': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["B", "C", "D"], "A")


def afd_opsuma(lexema):
    tabla = {
        'A': {"+": "B", "-": "B"},
        'B': {},
        'T': {},
    }
    return automata_por_tabla(lexema, tabla, ["B"], "A")


def afd_si(lexema):
    tabla = {
        'A': {'s': 'B'},
        'B': {'i': 'C'},
        'C': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["C"], "A")


def afd_sino(lexema):
    tabla = {
        'A': {'s': 'B'},
        'B': {'i': 'C'},
        'C': {'n': 'D'},
        'D': {'o': 'E'},
        'E': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["E"], "A")
