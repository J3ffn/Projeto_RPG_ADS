import time, random

#########Funções#########
def dado():
    return random.randint(1, 6)
def vezinimigo():
    print('O inimigo jogou o dado para se defender!')
    if numtirado == 1:

    elif numtirado == 3 or numtirado == 2:

    elif numtirado == 4:


    elif numtirado == 5:

    elif numtirado == 6:

#########Váriaveis#########
itens = [['Poção Pequena', 'Poção Média', 'Poção Grande'],[0, 0, 0]]
atributos = [90, 100, 110]
inimigo1 = [100, 100, 0]
atributosbatalha = atributos[:]
opcoes = 0

# BATALHA QUE VOU TENTAR TRANSFORMAR EM FUNÇÃO
while inimigo1[0] > 0:
    opcoes = int(input(f'''{'-' * 40}
    1-> Ataque      2-> Especial      

    3-> Itens       4-> Pular rodada
{'-' * 40}
Escolha o que você vai fazer: '''))

    if opcoes == 1:
        controle = int(input('Se você quiser jogar o dado para atacar digite (1), se quiser voltar digite (2): '))
        while 1 != controle != 2:
            controle = int(input("Para jogar o dado digite (1), para voltar digite (2): "))
        if controle == 1:
            print('O dado foi jogado...')
            time.sleep(1)
            numtirado = dado()
            print(f'Você jogou o dado e tirou o número {numtirado}!')
            if numtirado == 1:
                print('Você errou o golpe!')
            elif numtirado == 2:
                print('Você usou CORTE VERTICAL!')
            elif numtirado == 3:
                print('Você usou CORTE VERTICAL!')
            elif numtirado == 4:
                print('Você usou ESPADA SAGRADA!')
            elif numtirado == 5:
                print('Você usou ESPADA SAGRADA!')
            elif numtirado == 6:
                print('Você usou ESPADA SAGRADA!')
        elif controle == 2:
            continue