import time, random

def dado():
    return random.randint(1, 6)

itens = [['Poção Pequena', 'Poção Média', 'Poção Grande'],[1, 1, 0]]
atributos = [90, 100, 110]
inimigo1 = [200, 50, 0]
opcoes = 0
atributosbatalha = atributos[:]


while inimigo1[0] > 0 and atributosbatalha[0] > 0:
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
            if numtirado == 1 or numtirado == 2 or numtirado == 3:
                print(f'Você usou Feitiço')
                time.sleep(1)
                numtirado = dado()
                print('MASCARIANE jogou o dado para se defender!')
                time.sleep(2)
                print(f'Tirou o número {numtirado}')
                time.sleep(2)
                if numtirado == 1:
                    print('MASCARIANE se desviou do golpe!')
                elif numtirado == 2:
                    print(f'MASCARIANE recebeu {atributos[1] * 0.20} de dano!!!')
                    inimigo1[0] -= atributos[1] * 0.20
                elif numtirado == 3:
                    print(f'MASCARIANE recebeu {atributos[1] * 0.40} de dano!!!')
                    inimigo1[0] -= atributos[1] * 0.40
                elif numtirado == 4:
                    print(f'MASCARIANE recebeu {atributos[1] * 0.60} de dano!!!')
                    inimigo1[0] -= atributos[1] * 0.60
                elif numtirado == 5:
                    print(f'MASCARIANE recebeu {atributos[1] * 0.80} de dano!!!')
                    inimigo1[0] -= atributos[1] * 0.80
                elif numtirado == 6:
                    print(f'MASCARIANE recebeu {atributos[1] * 1.00} de dano!!!')
                    inimigo1[0] -= atributos[1] * 1.00
                time.sleep(2)
            elif numtirado == 4:
                if atributosbatalha[2] < 40:
                    print('Você não tem mana o suficiente para dá esse golpe!')
                    time.sleep(2)
                else:
                    atributosbatalha[2] -= 40
                    print('Você usou Bola de Fogo')
                    time.sleep(1)
                    numtirado = dado()
                    print('MASCARIANE jogou o dado para se defender!')
                    time.sleep(2)
                    print(f'Tirou o número {numtirado}')
                    time.sleep(2)
                    if numtirado == 1:
                        print('MASCARIANE se desviou do golpe!')
                    elif numtirado == 2:
                        print(f'MASCARIANE recebeu {120 * 0.40} de dano!!!')
                        inimigo1[0] -= 120 * 0.40
                    elif numtirado == 3:
                        print(f'MASCARIANE recebeu {120 * 0.40} de dano!!!')
                        inimigo1[0] -= 120 * 0.40
                    elif numtirado == 4:
                        print(f'MASCARIANE recebeu {120 * 0.80} de dano!!!')
                        inimigo1[0] -= 120 * 0.80
                    elif numtirado == 5:
                        print(f'MASCARIANE recebeu {120 * 0.80} de dano!!!')
                        inimigo1[0] -= 120 * 0.80
                    elif numtirado == 6:
                        print(f'MASCARIANE recebeu {120 * 1.00} de dano!!!')
                        inimigo1[0] -= 120 * 1.00
                    time.sleep(2)
            elif numtirado == 5:
                if atributosbatalha[2] < 60:
                    print('Você não tem mana o suficiente para dá esse golpe!')
                    time.sleep(2)
                else:
                    atributosbatalha[2] -= 60
                    print('Você usou Raio de gelo')
                    time.sleep(1)
                    numtirado = dado()
                    print('MASCARIANE jogou o dado para se defender!')
                    time.sleep(2)
                    print(f'Tirou o número {numtirado}')
                    time.sleep(2)
                    if numtirado == 1:
                        print('MASCARIANE se desviou do golpe!')
                    elif numtirado == 2:
                        print(f'MASCARIANE recebeu {140 * 0.60} de dano!!!')
                        inimigo1[0] -= 140 * 0.60
                    elif numtirado == 3:
                        print(f'MASCARIANE recebeu {140 * 0.60} de dano!!!')
                        inimigo1[0] -= 140 * 0.60
                    elif numtirado == 4:
                        print(f'MASCARIANE recebeu {140 * 0.80} de dano!!!')
                        inimigo1[0] -= 140 * 0.80
                    elif numtirado == 5:
                        print(f'MASCARIANE recebeu {140 * 0.80} de dano!!!')
                        inimigo1[0] -= 140 * 0.80
                    elif numtirado == 6:
                        print(f'MASCARIANE recebeu {140 * 1.00} de dano!!!')
                        inimigo1[0] -= 140 * 1.00
                    time.sleep(2)
            elif numtirado == 6:
                if atributosbatalha[2] < 80:
                    print('Você não tem mana o suficiente para dá esse golpe!')
                    time.sleep(2)
                else:
                    atributosbatalha[2] -= 80
                    print('Você usou Raio solar')
                    time.sleep(1)
                    numtirado = dado()
                    print('MASCARIANE jogou o dado para se defender!')
                    time.sleep(2)
                    print(f'Tirou o número {numtirado}')
                    time.sleep(2)
                    if numtirado == 1:
                        print('MASCARIANE se desviou do golpe!')
                    elif numtirado == 2:
                        print(f'MASCARIANE recebeu {160 * 0.60} de dano!!!')
                        inimigo1[0] -= 160 * 0.60
                    elif numtirado == 3:
                        print(f'MASCARIANE recebeu {160 * 0.60} de dano!!!')
                        inimigo1[0] -= 160 * 0.60
                    elif numtirado == 4:
                        print(f'MASCARIANE recebeu {160 * 0.80} de dano!!!')
                        inimigo1[0] -= 160 * 0.80
                    elif numtirado == 5:
                        print(f'MASCARIANE recebeu {160 * 0.80} de dano!!!')
                        inimigo1[0] -= 160 * 0.80
                    elif numtirado == 6:
                        print(f'MASCARIANE recebeu {160 * 1.00} de dano!!!')
                        inimigo1[0] -= 160 * 1.00
                    time.sleep(2)
        elif controle == 2:
            continue
    elif opcoes == 2:
        opcoesesp = int(input(f'''{'-' * 40}
        1-> Cura      N-> Voltar
{'-' * 40}
Escolha um especial ou clique em outro qualquer número para voltar: '''))
        if opcoesesp == 1:
            if atributosbatalha[2] >= 60:
                atributosbatalha[2] -= 60
                atributosbatalha[0] += 60
                if atributosbatalha[0] > atributos[0]:
                    atributosbatalha[0] = atributos[0]
                print(f'Sua vida agora é {atributosbatalha[0]}')
            else:
                print('Você não tem mana o suficiente para usar seu especial!')
                continue
        else:
            continue
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
        if opcoesitens == 1:
            if itens[1][0] > 0:
                atributosbatalha[0] += 20
                itens[1][0] -= 1
                print('Você curou a vida!')
                time.sleep(1)
                if atributosbatalha[0] == atributos[0]:
                    print('Você está com a vida cheia!')
                    continue
                elif atributosbatalha[0] > atributos[0]:
                    atributosbatalha[0] = atributos[0]
            else:
                print('Você não tem esse item!')
                time.sleep(1)

        elif opcoesitens == 2:
            if itens[1][1] > 0:
                atributosbatalha[0] += 40
                itens[1][1] -= 1
                print('Você curou a vida!')
                time.sleep(1)
                if atributosbatalha[0] == atributos[0]:
                    print('Você está com a vida cheia!')
                    continue
                elif atributosbatalha[0] > atributos[0]:
                    atributosbatalha[0] = atributos[0]
            else:
                print('Você não tem esse item!')
                time.sleep(1)

        elif opcoesitens == 3:
            if itens[1][2] > 0:
                atributosbatalha[0] += 60
                itens[1][2] -= 1
                print('Você curou a vida!')
                time.sleep(1)
                if atributosbatalha[0] == atributos[0]:
                    print('Você está com a vida cheia!')
                    continue
                elif atributosbatalha[0] > atributos[0]:
                    atributosbatalha[0] = atributos[0]
            else:
                print('Você não tem esse item!')
                time.sleep(1)
        elif opcoesitens == 4:
            continue
    elif opcoes == 4:
        print('Você pulou a rodada!')
        atributosbatalha[2] += 20
        time.sleep(1)
        print('Você recuperou 20 de mana!')
        if atributosbatalha[2] > atributos[2]:
            atributosbatalha[2] = atributos[2]
    if inimigo1[0] > 0:
        print('\033[1;40;31mVez de Mascariane\033[m')
        time.sleep(1)
        numtirado = dado()
        print('MASCARIANE te atacou! Você jogou o dado para tentar se defender!')
        time.sleep(2)
        print(f'Tirou o número {numtirado}')
        time.sleep(1)
        if numtirado == 1:
            print('MASCARIANE errou o golpe!')
        elif numtirado == 2:
            print(f'Você recebeu {inimigo1[1] * 0.20} de dano!!!')
            atributosbatalha[0] -= inimigo1[1] * 0.20
        elif numtirado == 3:
            print(f'Você recebeu {inimigo1[1] * 0.40} de dano!!!')
            atributosbatalha[0] -= inimigo1[1] * 0.40
        elif numtirado == 4:
            print(f'Você recebeu {inimigo1[1] * 0.60} de dano!!!')
            atributosbatalha[0] -= inimigo1[1] * 0.60
        elif numtirado == 5:
            print(f'Você recebeu {inimigo1[1] * 0.80} de dano!!!')
            atributosbatalha[0] -= inimigo1[1] * 0.80
        elif numtirado == 6:
            print(f'Você recebeu {inimigo1[1] * 1.00} de dano!!!')
            atributosbatalha[0] -= inimigo1[1] * 1.00
if inimigo1[0] <= 0:
    opcoes = int(input(f'''{'-' * 62}
              \033[0;32mParabéns você derrotou MASCARIANE!\033[m
             1-> Vida     2-> Ataque     3-> Mana
{'-' * 62}
Escolha um dos atributos para aumentar 2 pontos: '''))
    time.sleep(1)
    if opcoes == 1:
        atributos[0] += 2
        print(f'Seus atributos ficaram assim: {atributos}')
    elif opcoes == 2:
        atributos[1] += 2
        print(f'Seus atributos ficaram assim: {atributos}')
    elif opcoes == 3:
        atributos[2] += 2
        print(f'Seus atributos ficaram assim: {atributos}')
if atributosbatalha[0] <= 0:
    print('\033[1;40;31mQue pena, você perdeu.\033[m')
