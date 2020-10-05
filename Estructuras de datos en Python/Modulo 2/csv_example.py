# -*- coding: utf-8 -*-
import csv

# Leer un archivo CSV
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\csv_example.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

# Escribir un archivo CSV
with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\csv_example.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Carlos','Navarrete','44823456','cnava@gmail.com'])

# Ejercicio
import csv

reader = csv.reader(['Hola|, Mundo', 'Python'], escapechar='|')

file_content = list(reader)