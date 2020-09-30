# -*- coding: utf-8 -*-

s1 = "Prueba"

# Devuelve el número de ocurrencias de una subcadena de texto en toda la cadena o en un rango.
s1.count('a')
# Indica si la cadena de texto empieza con la subcadena pasada como parametro
s1.startswith('a')
# Indica si la cadena de texto termina con la subcadena pasada como parámetro
s1.endswith('a')
# Busca la subcadena pasada como parametro en la cadena de texto
s1.find('ue')
# Similar a find solo que al no encontrar la subcadena levanta una excepcion de tipo ValueError
s1.index('a')
# Igual a find solo que no devuelve la primera ocurrencia, sino la ultima
s1.rfind()
# Similar a rfind solo que al no encontrar la subcadena levanta una exepcion de tipo ValueError
s1.rindex()
# Indica si todos los caracteres de la cadena son decimales
s1.isdecimal()
# Indica si todos los caracteres de la cadena son digitos
s1.isdigit()
# Indica si todos los caracteres de la cadena son minusculas
s1.islower()
# Indica si todos los caracteres de la cadena son mayusculas
s1.isupper()
# Indica si la cadena de texto esta en estilo titulo
s1.istitle()
# Indica si la cadena de texto son todos espacios
s1.isspace()
# Indica si la cadena de texto son todas letras
s1.isalpha()
# Indica si la cadena de texto esta compuesta por todos caracteres alfanumericos
s1.isalnum()