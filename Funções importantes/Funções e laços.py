import time
import random


def txt(texto):
    for i in range(1):
        for c in texto:
            print(c, end='')
            # time.sleep(0.03) # biblioteca time necessária
        print()

txt("Teste")


def dado():
    x = random.randint(1, 6) # Biblioteca random necessária.
    return x

numero = 0
for i in range(1):
    numero = dado()
    print(numero)

