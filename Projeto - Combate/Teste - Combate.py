#By Josias
import time
import random

def dado():
    return random.randint(1,6)

atributos = [90, 100, 110]
inimigo1 = [50, 100, 0]
opcoes = 0

print('Um inimigo veio em sua direção, se prepare para seu primeiro combate!')
while inimigo1[0] != 0 and inimigo1[0] > 0:
    atributosbatalha = atributos[:]
    while not 0 > opcoes < 6:
        opcoes = int(input(f'''
        1-> Ataque base     2-> Habilidades          3-> Defesa  
    
        4-> Itens           5-> Dados do inimigo     6-> Pular rodada
    
Escolha o que você vai fazer: '''))

    if opcoes == 1:
        controle = int(input('Se você quiser jogar o dado para atacar digite (1), se quiser voltar digite (2): '))
        if controle == 1:
            print('O dado foi jogado...')
            time.sleep(1)
            numtirado = dado()
            print(f'Você jogou o dado e tirou o número {numtirado}!')
            if numtirado == 1:
                inimigo1[0] -= atributos[1] * 0.70
                print(f'Você causou {atributos[1] * 0.70} de dano no seu inimigo!')
            elif 2 == numtirado == 3:
                inimigo1[0] -= atributos[1] * 0.50
                print(f'Você causou {atributos[1] * 0.50} de dano no seu inimigo!')
            elif numtirado == 4:
                inimigo1[0] -= atributos[1] * 0.25
                print(f'Você causou {atributos[1] * 0.25} de dano no seu inimigo!')
            elif numtirado == 5:
                print('Você errou o golpe!')
            elif numtirado == 6:
                atributosbatalha[0] -= atributos[1] * 0.25
                print(f'Você errou o golpe e se machucou causando {atributos[1] * 0.25} em si mesmo')



