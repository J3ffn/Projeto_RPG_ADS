# ESSE NÃO É O RESULTADO FINAL, ESTÁ CHEIO DE ERROS
import time, random


#########Funções#########
def dado():
    return random.randint(1, 6)

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
        elif controle == 2:
            continue
    elif opcoes == 2:
        print('Você usou o especial')   # AINDA VOU FAZER OS BUFFS
    elif opcoes == 3:
        for l in range(len(itens)):
            for c in range(len(itens[l])):
                print(f'[{itens[l][c]:^13}]', end='')
            print()
        opcoesitens = int(input(f'''{'-' * 89}
        1-> Poção Pequena     2-> Poção Média     3-> Poção Grande     4-> Voltar
{'-' * 89}
Escolha um de seus itens: '''))
        while opcoesitens > 4 or opcoesitens < 0:
            opcoesitens = int(input(f'''{'-' * 89}
        1-> Poção Pequena     2-> Poção Média     3-> Poção Grande     4-> Voltar
{'-' * 89}
Escolha um de seus itens: '''))
        if opcoesitens == 1:                                # VOU AJEITAR UMAS COISAS AINDA AQUI
            if itens[1][0] > 0:
                atributosbatalha[0] += atributos[0] * 0.20
                itens[1][0] -= 1
                print('Você curou a vida!')
                time.sleep(1)
            else:
                print('Você não tem esse item!')
                time.sleep(1)
        elif opcoesitens == 2:
            if itens[1][1] > 0:
                atributosbatalha[0] += atributos[0] * 0.40
                itens[1][1] -= 1
                print('Você curou a vida!')
                time.sleep(1)
            else:
                print('Você não tem esse item!')
                time.sleep(1)
        elif opcoesitens == 3:
            if itens[1][2] > 0:
                atributosbatalha[0] += atributos[0] * 0.20
                itens[1][2] -= 1
                print('Você curou a vida!')
                time.sleep(1)
            else:
                print('Você não tem esse item!')
                time.sleep(1)
        elif opcoesitens == 4:
            continue
    elif opcoes == 4:
        print('Você pulou a rodada!')       # AINDA VOU COLOCAR A MANA QUE ELE VAI GANHAR
if inimigo1[0] <= 0:
    opcoes = int(input(f'''{'-' * 62}
              Parabéns você derrotou MASCARIANE!
             1-> Vida     2-> Ataque     3-> Mana
{'-' * 62}
Escolha um dos atributos para aumentar 2 pontos: '''))
    time.sleep(1)
    if opcoes == 1:
        atributos[0] += 2
        print(f'Seus atributos ficaram assim: {atributos}')
    elif opcoes == 2:
        atributos[1] += 2                  # VOU AJEITAR UMAS COISAS AQUI
        print(f'Seus atributos ficaram assim: {atributos}')
    elif opcoes == 3:
        atributos[2] += 2
        print(f'Seus atributos ficaram assim: {atributos}')