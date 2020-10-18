# -*- coding: utf-8 -*-

nombre = 'Emanuel'

lista = list(nombre)

# El indexado funciona de igual manera
nombre[0]
lista[0]

# El slicing funciona de igual manera
nombre[:3]
lista[:3]

# La funcion len funciona de igual manera
len(nombre)
len(lista)

# El in funciona en ambas
'E' in nombre
'E' in lista

# El not funciona en ambas
'z' not in nombre
'z' not in lista

# Los strings tambien se pueden recorrer con un for
for letra in nombre:
    print(letra)

# Los strings son inmutables
lista[2] = 'o'
nombre[2] = 'o' # TypeError

'Hola ' + nombre
nombre + '!!'
nombre[:2] + 'o' + nombre [3:]