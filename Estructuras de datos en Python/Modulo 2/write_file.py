# -*- coding: utf-8 -*-

# Escribir un string en el archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example3.txt','w') as a_file:
    a_file.write("Hola minions!")

# Escribir muchas lineas en el archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example3.txt','w') as a_file:
    a_file.writelines(['Hola minions!\n','Bello!\n','Bank yu!\n'])

# Escribir un string en el archivo
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\example2.txt','a') as a_file:
    a_file.write("Chau minions!")