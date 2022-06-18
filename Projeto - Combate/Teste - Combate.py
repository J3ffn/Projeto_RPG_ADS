import time, random

def dado():
    return random.randint(1, 6)

itens = [['Poção Pequena', 'Poção Média', 'Poção Grande'],[0, 0, 0]]
atributos = [90, 100, 110]
inimigo1 = [100, 100, 0]
atributosbatalha = atributos[:]
opcoes = 0
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
        