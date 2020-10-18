# -*- coding: utf-8 -*-

a_list = [(6, 2), (1, 5), (2, 3), (4, 1), (5, 2), (1, 3)]

a_list.sort(lambda x: x[0] + x[1])        # F ---> TypeError
a_list.sort(key= x[0] + x[1])             # F ---> TypeError
sorted(a_list,key= lambda x: x[0] + x[1]) # F ---> Funciona pero crea otra lista
a_list.sort(key= lambda x: x[0] + x[1])   # V