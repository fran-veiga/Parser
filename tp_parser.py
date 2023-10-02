from gramatica import VN, VT, P, SD, simbolo_inicial
from lexer.lexer import lexer


def parser(lista):
    lista.append(("#", "#"))
    datos_locales = {
        'tokens': lista,
        'index': 0,
        'error': False,
        'error_t': None,
        'derivaciones': []
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
                    break
            elif simbolo in VN:
                procedimiento_PNI(simbolo)
                if datos_locales['error']:
                    break

    def procedimiento_PNI(simbolo):
        datos_locales['error'] = False
        actual = datos_locales['tokens'][datos_locales['index']][0]
        simbolos_directrices = SD[simbolo]

        if actual in simbolos_directrices:
            cadena_derivacion = simbolos_directrices[actual]
            derivacion = [simbolo, cadena_derivacion]
            datos_locales["derivaciones"].append(derivacion)
            procesar(cadena_derivacion)
        else:
            datos_locales['error'] = True

    def principal():
        procedimiento_PNI(simbolo_inicial)
        if datos_locales['error']:
            print('La cadena no pertenece al lenguaje.')
            return False
        actual = datos_locales['tokens'][datos_locales['index']][0]
        if actual == '#':
            print('La cadena pertenece al lenguaje.')
            print('Derivaciones utilizadas:\n')
            for deriv in datos_locales['derivaciones']:
                print(deriv[0] + " -> ", end="")
                if deriv[1]:
                    print(' '.join(deriv[1]))
                else:
                    print("(lambda)")
            return True

    return principal()


tests = [
    # test 1
    '''
x equal 98234;

si 6 < 7 entonces
    x equal x / 4
sino
    x equal x / 3
finsi
''',

    # test 2
    '''
func mult(n1; n2)
    x equal n1 * n2;
    mostrar x
finfunc
''',

    # test 3
    '''
leer x;

i equal 0;
repetir
    mostrar i;
    i equal i + 1
hasta i = x
''',

    # test 4
    '''
23hola+-sifinsi
''',

    # test 5
    '''
repetir
    iequali+1;
    leerx;
    x=x*x;
    mostrarx
hasta i=33
''',

    # test 6
    '''
vmax=0;
leer y;
si y>vmax entonces
    vmax equal y
sino
    e equal e+1
finsi
mostrar vmax;
mostrar e
''',

    # test 7
    '''
repetir
    i equal i+1;
    leer nombre;
    leer edad;
    si edad>=18 entonces
        mostrar nombre
    sino
        vdif equal 18-edad;
        mostrar vdif
    finsi
hasta i=20
''',

    # test 8
    '''
leer x;
leer y;
si x>y entonces
    x equal x+y
sino
    y equal x+y
finsi
''',

    # test 9
    '''
func rest(n1; n2)
    x equal n1 - n2;
    mostrar x
finfunc
''',

    # test 10
    '''
vmax equal 0;
repetir
    i equal i+1;
    leer socio;
    leer dni;
    leer edad;
    si edad>vmax entonces
        msocio equal socio;
        mdni equal dni;
        medad equal edad
    finsi
hasta i=50;
mostrar msocio;
mostrar mdni;
mostrar medad
''',
]


for i in range(len(tests)):
    print(f'=========TEST N°{i+1}=========')
    print(tests[i])
    print(f'---- RESULTADO \t {parser(lexer(tests[i]))}')
    print("")
    print("")
