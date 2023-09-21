

VT = ["DerParen", "IzqParen", "PuntoYComa", "Entonces", "Equal", "FinFunc", "FinSi", "Func",
      "Hasta", "Leer", "Mostrar", "Repetir", "Si", "Sino", "Oprel", "Opmult", "Opsuma", "Num", "Id"]

VN = ["Program", "ListaSentencias", "ListaSentencias_p", "Sentencia", "SentenciaSi", "SentenciaSi_p", "SentenciaRepetir", "SentenciaAsig", "SentenciaLeer",
      "SentenciaMostrar", "SentenciaFun", "Proc", "ListaPar", "ListaPar_p", "Expresion", "Expresion_p", "Expresion2", "Expresion2_p", "Termino", "Termino_p", "Factor", ]
P = {
    "Program": [
        ["ListaSentencias"]
    ],

    "ListaSentencias": [
        ["Sentencia", "ListaSentencias_p"],
    ],

    "ListaSentencias_p": [
        ["PuntoYComa", "Sentencia", "ListaSentencias_p"],
        [],
    ],

    "Sentencia": [
        ["SentenciaSi"],
        ["SentenciaRepetir"],
        ["SentenciaAsig"],
        ["SentenciaLeer"],
        ["SentenciaMostrar"],
        ["SentenciaFun"],
    ],

    "SentenciaRepetir": [
        ["Repetir", "ListaSentencias", "Hasta", "Expresion"]
    ],

    "SentenciaSi": [
        ["Si", "Expresion", "Entonces", "ListaSentencias", "SentenciaSi_p"]
    ],

    "SentenciaSi_p": [
        ["Sino", "ListaSentencias", "FinSi"],
        ["FinSi"]
    ],

    "SentenciaAsig": [
        ["Id", "Equal", "Expresion"]
    ],

    "SentenciaLeer": [
        ["Leer", "Id"]
    ],

    "SentenciaMostrar": [
        ["Mostrar", "Expresion"]
    ],

    "SentenciaFun": [
        ["Func", "Proc", "FinFunc"]
    ],

    "Proc": [
        ["Id", "IzqParen", "ListaPar", "DerParen", "ListaSentencias"]
    ],

    "ListaPar": [
        ["Id", "ListaPar_p"],
    ],

    "ListaPar_p": [
        ["PuntoYComa", "Id", "ListaPar_p"],
        []
    ],

    "Expresion": [
        ["Expresion2", "Expresion_p"],
    ],

    "Expresion_p": [
        ["oprel", "Expresion2"],
        [],
    ],

    "Expresion2": [
        ["Termino", "Expresion2_p"]
    ],

    "Expresion2_p": [
        ["Opsuma", "Termino", "Expresion2_p"],
        []
    ],

    "Termino": [
        ["Factor", "Termino_p"]
    ],

    "Termino_p": [
        ["Opmult", "Factor", "Termino_p"],
        []
    ],

    "Factor": [
        ["IzqParen", "Expresion", "DerParen"],
        ["Num"],
        ["Id"]
    ]
}

SD = {
    "Program": {
        "Si": ["ListaSentencias"],
        "Repetir": ["ListaSentencias"],
        "Id": ["ListaSentencias"],
        "Leer": ["ListaSentencias"],
        "Mostrar": ["ListaSentencias"],
        "Func": ["ListaSentencias"],

    },

    "ListaSentencias": {
        "Si": ["Sentencia", "ListaSentencias_p"],
        "Repetir": ["Sentencia", "ListaSentencias_p"],
        "Id": ["Sentencia", "ListaSentencias_p"],
        "Leer": ["Sentencia", "ListaSentencias_p"],
        "Mostrar": ["Sentencia", "ListaSentencias_p"],
        "Func": ["Sentencia", "ListaSentencias_p"],
    },

    "ListaSentencias_p": {
        "PuntoYComa": ["PuntoYComa", "Sentencia", "ListaSentencias_p"],
        "#": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
    },

    "Sentencia": {
        "Si": ["SentenciaSi"],
        "Repetir": ["SentenciaRepetir"],
        "Id": ["SentenciaAsig"],
        "Leer": ["SentenciaLeer"],
        "Mostrar": ["SentenciaMostrar"],
        "Func": ["SentenciaFun"],
    },

    "SentenciaRepetir": {
        "Repetir":  ["Repetir", "ListaSentencias", "Hasta", "Expresion"],
    },

    "SentenciaSi": {
        "Si":  ["Si", "Expresion", "Entonces", "ListaSentencias",
                "SentenciaSi_p"],
    },

    "SentenciaSi_p": {
        "Sino": ["Sino", "ListaSentencias", "FinSi"],
        "FinSi": ["FinSi"],
    },

    "SentenciaAsig": {
        "Id": ["Id", "Equal", "Expresion"],
    },

    "SentenciaLeer": {
        "Leer": ["Leer", "Id"],
    },

    "SentenciaMostrar": {
        "Mostrar": ["Mostrar", "Expresion"],
    },

    "SentenciaFun": {
        "Func": ["Func", "Proc", "FinFunc"],
    },

    "Proc": {
        "Id": ["Id", "IzqParen", "ListaPar", "DerParen", "ListaSentencias"],
    },

    "ListaPar": {
        "Id": ["Id", "ListaPar_p"],
    },

    "ListaPar_p": {
        "PuntoYComa": ["PuntoYComa", "Id", "ListaPar_p"],
        "DerParen": [],
    },

    "Expresion": {
        "IzqParen": ["Expresion2", "Expresion_p"],
        "Num": ["Expresion2", "Expresion_p"],
        "Id": ["Expresion2", "Expresion_p"],
    },

    "Expresion_p": {
        "Oprel": ["oprel", "Expresion2"],
        "DerParen": [],
        "#": [],
        "PuntoYComa": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
        "Entonces": [],
    },

    "Expresion2": {
        "IzqParen": ["Termino", "Expresion2_p"],
        "Num": ["Termino", "Expresion2_p"],
        "Id": ["Termino", "Expresion2_p"],
    },

    "Expresion2_p": {
        "Opsuma": ["Opsuma", "Termino", "Expresion2_p"],
        "Oprel": [],
        "DerParen": [],
        "#": [],
        "PuntoYComa": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
        "Entonces": [],
    },

    "Termino": {
        "IzqParen": ["IzqParen", "Expresion", "DerParen"],
        "Num": ["Num"],
        "Id": ["Id"],
    },

    "Termino_p": {
        "Opmult": ["Opmult", "Factor", "Termino_p"],
        "Opsuma": [],
        "Oprel": [],
        "DerParen": [],
        "#": [],
        "PuntoYComa": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
        "Entonces": [],
    }
}
