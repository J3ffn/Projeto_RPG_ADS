import time, random


#########Funções#########
def dado():
    return random.randint(1, 6)
def inimigodef():
    numtirado = dado()
    print('MASCARIANE jogou o dado para se defender!')
    time.sleep(2)
    print(f'Tirou o número {numtirado}')
    time.sleep(2)
    if numtirado == 1:
        print('MASCARIANE se desviou do golpe!')
    elif numtirado == 2:
        print(f'MASCARIANE recebeu {atributos[1] * 0.75} de dano!!!')
        inimigo1[0] -= atributos[1] * 0.75
    elif numtirado == 3:
        print(f'MASCARIANE recebeu {atributos[1] * 0.60} de dano!!!')
        inimigo1[0] -= atributos[1] * 0.60
    elif numtirado == 4:
        print(f'MASCARIANE recebeu {atributos[1] * 0.90} de dano!!!')
        inimigo1[0] -= atributos[1] * 0.90
    elif numtirado == 5:
        print(f'MASCARIANE recebeu {atributos[1] * 1.00} de dano!!!')
        inimigo1[0] -= atributos[1] * 1.00
    elif numtirado == 6:
        print('MASCARIANE se desviou do golpe!')
    time.sleep(2)

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
                print(f'Você usou CORTE VERTICAL!')
                time.sleep(1)
            elif numtirado == 2:
                print('Você usou CORTE VERTICAL!')
                time.sleep(1)
            elif numtirado == 3:
                print('Você usou CORTE VERTICAL!')
                time.sleep(1)
            elif numtirado == 4:
                print('Você usou ESPADA SAGRADA!')
                time.sleep(1)
            elif numtirado == 5:
                print('Você usou ESPADA SAGRADA!')
                time.sleep(1)
            elif numtirado == 6:
                print('Você usou ESPADA SAGRADA!')
                time.sleep(1)
            inimigodef()
        elif controle == 2:
            continue