import math

factorial_10 = str(math.factorial(10))

with open(r'\Users\Administrator\Desktop\Repositorios\Curso_Python\Estructuras de datos en Python\Modulo 2\ejercicio1.txt','w') as a_file:
    a_file.write(factorial_10)