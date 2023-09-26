from gramatica import VN, VT, P, SD, simbolo_inicial
from lexer.lexer import lexer


def parser(lista):
    lista.append(("#", "#"))
    datos_locales = {
        'tokens': lista,
        'index': 0,
        'error': False,
    }

    def procesar(cadena):
        for simbolo in cadena:
            actual = datos_locales['tokens'][datos_locales['index']][0]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == actual:
                    datos_locales['index'] += 1
                else:
                    datos_locales['error'] = True
            elif simbolo in VN:
                procedimiento_PNI(simbolo)
                if datos_locales['error']:
                    break

    def procedimiento_PNI(simbolo):
        datos_locales['error'] = False
        actual = datos_locales['tokens'][datos_locales['index']][0]
        simbolos_directrices = SD[simbolo]
        if actual in simbolos_directrices:
            procesar(simbolos_directrices[actual])
        else:
            datos_locales['error'] = True

    def principal():
        procedimiento_PNI(simbolo_inicial)
        actual = datos_locales['tokens'][datos_locales['index']][0]
        if actual != '#' or datos_locales['error']:
            print('la cadena no pertenece al lenguaje ')
            return False
        print('la cadena pertence al lenguaje')
        return True

    return principal()


program = '''
func hello(x)
    hello equal 1234;
    mostrar hello
finfunc
'''

tokens = lexer(program)
print(tokens)
parser(tokens)


