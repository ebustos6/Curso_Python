# -*- coding: utf-8 -*-

# Abrir archivo
a_file = open('C:\\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r')
a_file = open(r'C:\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r')
# el problema de las "\" cuando abris un archivo se soluciona poniendo r antes del string como lo hice en el ejemplo
# o tambien convirtiendo la primer "\" despues del "C:" en "\\"

# Leer todo el contenido del archivo
a_file.read()

# Cerrar archivo
a_file.close()

# Abrir un archivo con un context manager utilizando la sentencia with

with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example.txt','r') as a_file:
    a_file.read()