# -*- coding: utf-8 -*-

frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana', 'kiwi'}

'pera' in frutas
'yerba' in frutas

# Conjunto vacio
set()

# Otra forma de crear conjuntos
a = set('abrakadabra')
b = set('alakazam')

# Operaciones de conjuntos
a - b # letras en a pero no en b
a | b # letras en a o en b o en ambas
a & b # letras en a y en b
a ^ b # letras en a o b pero no en ambas

# Comprension de conjuntos
a = {x for x in 'abrakadabra' if x not in 'abc'}

# Agregar al conjunto
a.add('z')

# Eliminar un elemento
a.remove('z')