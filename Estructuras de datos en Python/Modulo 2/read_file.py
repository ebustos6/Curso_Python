# -*- coding: utf-8 -*-

# La funcion read lee todo el contenido del archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r') as a_file:
    print(a_file.read())

# La funcion readline lee la linea actual del archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r') as a_file:
    print(a_file.readline())

# La funcion readlines lee las lineas del archivo y las guarda en una lista
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r') as a_file:
    print(a_file.readlines())

# La funcion list genera una lista con las lineas del archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r') as a_file:
    print(list(a_file))

# El for recorre linea a linea 
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r') as a_file:
    for line in a_file:
        print(line)
