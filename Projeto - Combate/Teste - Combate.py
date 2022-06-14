#By Josias
import time
import random

def dado():
    return random.randint(1,6)

atributos = [90, 100, 110]
inimigo1 = [50, 100, 0]

print('Um inimigo veio em sua direção, se prepare para seu primeiro combate!')
opcoes = int(input(f'''
1-> Ataque base     2-> Habilidades

3-> Defesa          4-> Itens

Escolha o que você vai fazer: '''))

if opcoes == 1:

