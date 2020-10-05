# -*- coding: utf-8 -*-
import json

# serializar un objeto
json.dumps([1, 2, 3])

# deserializar un objeto
json.loads('[1, 2, 3]')

# Escribir como json directamente a un archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\json_example.txt','w') as a_file:
    json.dump([1, 2, 3, 4], a_file)

# Leer un json directamente desde un archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\json_example.txt','r') as a_file:
    a_list = json.load(a_file)