cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

list(map(lambda x: x**2,range(10)))     # V
list(filter(lambda x: x**2,range(10)))  # F
list(map(lambda x: x**2 > 0,range(10))) # F
[x**2 for x in range(10)]               # V

a_list = [1, 3, 5, 7, 9]

[x*2 + 1 for x in range(5)]          # V
[x for x in range(10) if x % 2 == 0] # F
[x for x in range(10) if x % 2 != 0] # V
[x for x in range(10) if x % 2 == 1] # V
[x for x in range(10) if x % 2 != 1] # F

[x*y for x in [1, 2, 3] for y in [3, 1, 4] if x!=y]