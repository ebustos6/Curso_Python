import random

repeat = True
while repeat:
    dice1, dice2 = random.randint(1,6),random.randint(1,6)
    print("Se tiran los dados el primer dado sale:",dice1,"y el segundo dado sale:",dice2)
    print("La suma de ambos dados es:",(dice1 + dice2))
    answer = input("Desea volver a tirar dados? (s/n): ")
    if(answer == 'n'):
        repeat = False
