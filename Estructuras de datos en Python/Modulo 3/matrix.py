# -*- coding: utf-8 -*-

# Definicion de una matriz de 3 filas por 4 columnas
matriz = {
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
}

# Accesos a los elementos
matriz[0][0] # 1
matriz[1][2] # 7

# Ejemplo de funcion suma de matrices
def suma_matrices(A, B):
    """ 
        suma dos matrices.
        Precondicion: A y B son del mismo tamaño y son matrices de numeros.
    """
    cant_filas = len(A)
    cant_cols = len(A[0])

    C = []

    for fila in range(cant_filas):
        fila_suma = []
        for col in range(cant_cols):
            fila_suma.append(A[fila][col] + B[fila][col])
        C.append(fila_suma)
    return C

suma_matrices(matriz,matriz)

# no es la forma mas eficiente de trabajar con matrices en python,
#  la libreria NUMPY es mejor para usar matrices grandes