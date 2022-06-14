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

        5-> Pular rodada

Escolha o que você vai fazer: '''))

if opcoes == 1:
    controle = input('Você quer jogar o dado para atacar ou voltar? ')
    if controle == 'atacar':
        print('O dado foi jogado...')
        time.sleep(1)
        numtirado = dado()
        print(f'Você jogou o dado e tirou o número {numtirado}!')
        if numtirado == 1:



