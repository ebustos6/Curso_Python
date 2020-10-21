# -*- coding: utf-8 -*-

# Empaquetado
a = 30
b = "T"
C = "A"

tupla = a,b,c

# Desempaquetado
x,y,z = tupla

# Errores por distintos tamaños al desempaquetar
x,y = tupla     # ValueError
w,x,y,z = tupla # ValueError