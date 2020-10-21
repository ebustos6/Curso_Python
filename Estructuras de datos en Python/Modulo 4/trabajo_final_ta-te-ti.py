tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
se_esta_jugando = True
ganador = None
jugador_actual = "X"

def mostrar_tablero():
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("-" + "-+-" + "-" + "-+-" + "-")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("-" + "-+-" + "-" + "-+-" + "-")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

def jugar():
    mostrar_tablero()

    while se_esta_jugando:
        dar_turno(jugador_actual)

        ver_si_termino()

        cambiar_jugador()

    if ganador == "X" or ganador == "O":
        print(ganador + " ganó!")
    elif ganador == None:
        print("Empate!")

    if se_esta_jugando == False:
        jugar_nuevamente()

def ver_si_termino():
    ver_si_gano()
    ver_si_empato()

def ver_si_gano():
    global ganador

    ganador_filas = ver_filas()
    ganador_columnas = ver_columnas()
    ganador_diagonales = ver_diagonales()

    if ganador_filas:
        ganador = ganador_filas
    elif ganador_columnas:
        ganador = ganador_columnas
    elif ganador_diagonales:
        ganador = ganador_diagonales
    else:
        ganador = None
    

def ver_filas():
    global se_esta_jugando
    fila_1 = tablero[0] == tablero[1] == tablero[2] != ' '
    fila_2 = tablero[3] == tablero[4] == tablero[5] != ' '
    fila_3 = tablero[6] == tablero[7] == tablero[8] != ' '
    if fila_1 or fila_2 or fila_3:
        se_esta_jugando = False
    if fila_1:
        return tablero[0]
    elif fila_2:
        return tablero[3]
    elif fila_3:
        return tablero[6]
    

def ver_columnas():
    global se_esta_jugando
    columna_1 = tablero[0] == tablero[3] == tablero[6] != ' '
    columna_2 = tablero[1] == tablero[4] == tablero[7] != ' '
    columna_3 = tablero[2] == tablero[5] == tablero[8] != ' '
    if columna_1 or columna_2 or columna_3:
        se_esta_jugando = False
    if columna_1:
        return tablero[0]
    elif columna_2:
        return tablero[1]
    elif columna_3:
        return tablero[2]

def ver_diagonales():
    global se_esta_jugando
    diagonal_1 = tablero[0] == tablero[4] == tablero[8] != ' '
    diagonal_2 = tablero[6] == tablero[4] == tablero[2] != ' '
    if diagonal_1 or diagonal_2:
        se_esta_jugando = False
    if diagonal_1:
        return tablero[0]
    elif diagonal_2:
        return tablero[6]

def ver_si_empato():
    global se_esta_jugando
    if " " not in tablero:
        se_esta_jugando = False

def cambiar_jugador():
    global jugador_actual
    if jugador_actual == "X":
        jugador_actual = "O"
    elif jugador_actual == "O":
        jugador_actual = "X"

def dar_turno(jugador):
    print("Turno de " + jugador)
    posicion = input("Elegir posicion(1 - 9): ")
    es_valido = False
    while not es_valido:
        while posicion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            posicion = input("Posición inválida. Elegir posición(1 - 9): ")
        posicion = int(posicion) - 1

        if tablero[posicion] == " ":
            es_valido = True
        else:
            print("No se puede sobreescribir, intente nuevamente")

    tablero[posicion] = jugador
    mostrar_tablero()

def jugar_nuevamente():
    global se_esta_jugando
    global tablero
    global ganador
    global jugador_actual
    print("Desea jugar nuevamente?(s / n): ")
    respuesta = input()
    while not (respuesta == "s" or respuesta == "S" or respuesta == "n" or respuesta == "N"):
        print("No es una respuesta válida. Desea jugar nuevamente?(s / n): ")
    if (respuesta == "s" or respuesta == "S"):
        se_esta_jugando = True
        tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        ganador = None
        jugador_actual = "X"
        jugar()
    elif (respuesta == "n" or respuesta == "N"):
         print("Gracias por jugar!")   

jugar()