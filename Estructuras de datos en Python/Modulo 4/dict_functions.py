# -*- coding: utf-8 -*-

precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75}

# Cantidad de elementos (calve - valor)
len(precios)

# Obtiene el valor de clave indicada, se puede indicar un default si no existe
precios.get('manzana') 
precios.get('melon')
precios.get('melon', 0.00)

# Si existe devuelve el valor, si no lo crea con el valor default o si no se indica el default con none
precios.setdefault('banana')
precios.setdefault('sandia', 6.7)

# Actualizacion de un diccionario
precios.update({'banana': 4.0, 'durazno': 5.5})
precios.update([('durazno': 5.5)])

# Me devuelve una vista con las claves del diccionario
precios.keys()

# Me devuelve una vista con los items del diccionario
precios.items()

# Me devuelve una vista con los valores del diccionario
precios.values()

# Saca el elemento de la clave indicada, se puede poner un default si no existe
precios.pop('manzana')
precios.pop('melon', 0.00)
precios.pop('melon')

# Saca un elemento siguiendo el orden: LIFO
precios.popitem()

# Copia superficial de los diccionarios
copia_precios = precios.copy()

# Borra todos los elementos
precios.clear()