# -*- coding: utf-8 -*-

tupla = (1, 2.5, 'Hola')

tupla[0]  # 1
tupla[1]  # 2.5
tupla[2]  # 'Hola'

tupla[:2] # (1, 2.5)

# Tupla Vacia
tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

# Tupla de un elemento
tupla_2 = (5,) # es una tupla
numero = (5)   # es un numero

# Son inmutables
tupla[2] = 3   # TypeError

# Longitud de una tupla
len(tupla)