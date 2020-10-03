# -*- coding: utf-8 -*-
import math

class NegativeNumber(Exception):
    "Excepcion de numero negativo"
    pass

def raiz_cuadrada(number):
    if number < 0:
        raise NegativeNumber("Numero negativo.")
    return math.sqrt(number)