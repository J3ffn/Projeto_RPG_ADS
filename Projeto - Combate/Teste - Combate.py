import time
import random
import pygame


def ver(opcao, opcoes_escolhas):
    escolha = [opcao]
    opcoes = [*opcoes_escolhas]
    while escolha[-1].isnumeric() is not True or escolha[-1].isnumeric():
        try:
            if int(escolha[-1]):
                if escolha[-1] in opcoes:
                    c = int(escolha[-1])
                    escolha.pop()
                    escolha = c
                    break

                if int(escolha[-1]) <= 0:
                    escolha[-1] += 2

                else:
                    escolha[-1] += 2

        except ValueError:
            escolha.pop()
            print("Escolha uma opção válida!")
            escolha.append(input("Sua escolha: "))

        except TypeError:
            escolha.pop()
            print("Escolha uma opção válida!")
            escolha.append(input("Sua escolha: "))

    return escolha


class Batalha:
    def combate(self, inimigo_atb, inimigo_nome, final):
        contelfa = 0
        atributosbatalha = class_e_atributos[1][:]
        while inimigo_atb[0] > 0 and atributosbatalha[0] > 0:
            print('-' * 40)
            print(f'[HP: {atributosbatalha[0]}]{f"[HP.I: {inimigo_atb[0]}]":>32}')
            print(f'[MANA: {atributosbatalha[2]}]')
            opcoes = ver(input(f'''{'-' * 40}
        1-> Ataque      2-> Especial      
    
        3-> Itens       4-> Pular rodada
{'-' * 40}
Escolha o que você vai fazer: '''))

            while opcoes > 4 or opcoes < 0:
                print('-' * 40)
                print(f'[HP: {atributosbatalha[0]}]{f"[HP.I: {inimigo_atb[0]}]":>32}')
                print(f'[MANA: {atributosbatalha[2]}]')
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
                    dado = random.randint(1, 6)
                    print(f'Você jogou o dado e tirou o número {dado}!')
                    if dado == 1 or dado == 2 or dado == 3:
                        print(f'Você usou {class_e_atributos[2][0]}')
                        time.sleep(1)
                        dado = random.randint(1, 6)
                        print(f'{inimigo_nome} jogou o dado para se defender!')
                        time.sleep(2)
                        print(f'Tirou o número {dado}')
                        time.sleep(2)
                        if dado == 1:
                            print(f'{inimigo_nome} se desviou do golpe!')
                        elif dado == 2:
                            print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.20} de dano!!!')
                            inimigo_atb[0] -= class_e_atributos[1][1] * 0.20
                        elif dado == 3:
                            print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.40} de dano!!!')
                            inimigo_atb[0] -= class_e_atributos[1][1] * 0.40
                        elif dado == 4:
                            print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.60} de dano!!!')
                            inimigo_atb[0] -= class_e_atributos[1][1] * 0.60
                        elif dado == 5:
                            print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.80} de dano!!!')
                            inimigo_atb[0] -= class_e_atributos[1][1] * 0.80
                        elif dado == 6:
                            print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 1.00} de dano!!!')
                            inimigo_atb[0] -= class_e_atributos[1][1] * 1.00
                        time.sleep(2)
                    elif dado == 4:
                        if atributosbatalha[2] < 40:
                            print('Você não tem mana o suficiente para dar esse golpe!')
                            time.sleep(2)
                        else:
                            atributosbatalha[2] -= 25
                            print(f'Você usou {class_e_atributos[2][1]}')
                            time.sleep(1)
                            dado = random.randint(1, 6)
                            print(f'{inimigo_nome} jogou o dado para se defender!')
                            time.sleep(2)
                            print(f'Tirou o número {dado}')
                            time.sleep(2)
                            if dado == 1:
                                print(f'{inimigo_nome} se desviou do golpe!')
                            elif dado == 2:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.20) + 30} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.20) + 30
                            elif dado == 3:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.40) + 30} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.40) + 30
                            elif dado == 4:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.60) + 30} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.60) + 30
                            elif dado == 5:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.80) + 30} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.80) + 30
                            elif dado == 6:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 1.00) + 30} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 1.00) + 30
                            time.sleep(2)
                    elif dado == 5:
                        if atributosbatalha[2] < 60:
                            print('Você não tem mana o suficiente para dar esse golpe!')
                            time.sleep(2)
                        else:
                            atributosbatalha[2] -= 60
                            print(f'Você usou {class_e_atributos[2][2]}')
                            time.sleep(1)
                            dado = random.randint(1, 6)
                            print(f'{inimigo_nome} jogou o dado para se defender!')
                            time.sleep(2)
                            print(f'Tirou o número {dado}')
                            time.sleep(2)
                            if dado == 1:
                                print(f'{inimigo_nome} se desviou do golpe!')
                            elif dado == 2:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.60) + 40} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.60) + 40
                            elif dado == 3:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.60) + 40} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.60) + 40
                            elif dado == 4:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.80) + 40} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.80) + 40
                            elif dado == 5:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.80) + 40} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.80) + 40
                            elif dado == 6:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 1.00) + 40} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 1.00) + 40
                            time.sleep(2)
                    elif dado == 6:
                        if atributosbatalha[2] < 80:
                            print('Você não tem mana o suficiente para dar esse golpe!')
                            time.sleep(2)
                        else:
                            atributosbatalha[2] -= 80
                            print(f'Você usou {class_e_atributos[2][3]}')
                            time.sleep(1)
                            dado = random.randint(1, 6)
                            print(f'{inimigo_nome} jogou o dado para se defender!')
                            time.sleep(2)
                            print(f'Tirou o número {dado}')
                            time.sleep(2)
                            if dado == 1:
                                print(f'{inimigo_nome} se desviou do golpe!')
                            elif dado == 2:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.80) + 50} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.80) + 50
                            elif dado == 3:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.80) + 50} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.80) + 50
                            elif dado == 4:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.80) + 50} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.80) + 50
                            elif dado == 5:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 0.90) + 50} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 0.90) + 50
                            elif dado == 6:
                                print(f'{inimigo_nome} recebeu {(class_e_atributos[1][1] * 1.00) + 50} de dano!!!')
                                inimigo_atb[0] -= (class_e_atributos[1][1] * 1.00) + 50
                            time.sleep(2)

                    if final == 'onelfa':
                        dado = random.randint(1, 6)
                        print('A elfa e o Yati atacaram!!')
                        print(f'Tiraram o número {dado}')
                        time.sleep(1)
                        if dado == 1:
                            print(f'Eles erraram o golpe!')
                        elif dado == 2:
                            print(f'Mascariane recebeu {200 * 0.20} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.20
                        elif dado == 3:
                            print(f'Mascariane {200 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.40
                        elif dado == 4:
                            print(f'Mascariane {200 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.60
                        elif dado == 5:
                            print(f'Mascariane {200 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.80
                        elif dado == 6:
                            print(f'Mascariane recebeu {200 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 200 * 1.00

                    elif final == 'onmago':
                        dado = random.randint(1, 6)
                        print('O mago atacou!!')
                        print(f'Tirou o número {dado}')
                        time.sleep(1)
                        if dado == 1:
                            print(f'Ele errou o golpe!')
                        elif dado == 2:
                            print(f'Mascariane recebeu {200 * 0.20} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.20
                        elif dado == 3:
                            print(f'Mascariane {200 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.40
                        elif dado == 4:
                            print(f'Mascariane {200 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.60
                        elif dado == 5:
                            print(f'Mascariane {200 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.80
                        elif dado == 6:
                            print(f'Mascariane recebeu {200 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 200 * 1.00

                    elif final == 'onmagoelfa':
                        dado = random.randint(1, 6)
                        print('A elfa e o Yati atacaram!!')
                        print(f'Tiraram o número {dado}')
                        time.sleep(1)
                        if dado == 1:
                            print(f'Eles erraram o golpe!')
                        elif dado == 2:
                            print(f'Mascariane recebeu {200 * 0.20} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.20
                        elif dado == 3:
                            print(f'Mascariane {200 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.40
                        elif dado == 4:
                            print(f'Mascariane {200 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.60
                        elif dado == 5:
                            print(f'Mascariane {200 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.80
                        elif dado == 6:
                            print(f'Mascariane recebeu {200 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 200 * 1.00

                        dado = random.randint(1, 6)
                        print('O mago atacou!!')
                        print(f'Tirou o número {dado}')
                        time.sleep(1)
                        if dado == 1:
                            print(f'Ele errou o golpe!')
                        elif dado == 2:
                            print(f'Mascariane recebeu {200 * 0.20} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.20
                        elif dado == 3:
                            print(f'Mascariane {200 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.40
                        elif dado == 4:
                            print(f'Mascariane {200 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.60
                        elif dado == 5:
                            print(f'Mascariane {200 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.80
                        elif dado == 6:
                            print(f'Mascariane recebeu {200 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 200 * 1.00

                    elif final == 'onmagoguerreiro':
                        dado = random.randint(1, 6)
                        print('O guerreiro atacou!!')
                        print(f'Tirou o número {dado}')
                        time.sleep(1)
                        if dado == 1:
                            print(f'Ele errou o golpe!')
                        elif dado == 2:
                            print(f'Mascariane recebeu {200 * 0.20} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.20
                        elif dado == 3:
                            print(f'Mascariane {200 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.40
                        elif dado == 4:
                            print(f'Mascariane {200 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.60
                        elif dado == 5:
                            print(f'Mascariane {200 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.80
                        elif dado == 6:
                            print(f'Mascariane recebeu {200 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 200 * 1.00

                        dado = random.randint(1, 6)
                        print('O mago atacou!!')
                        print(f'Tirou o número {dado}')
                        time.sleep(1)
                        if dado == 1:
                            print(f'Ele errou o golpe!')
                        elif dado == 2:
                            print(f'Mascariane recebeu {200 * 0.20} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.20
                        elif dado == 3:
                            print(f'Mascariane {200 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.40
                        elif dado == 4:
                            print(f'Mascariane {200 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.60
                        elif dado == 5:
                            print(f'Mascariane {200 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 200 * 0.80
                        elif dado == 6:
                            print(f'Mascariane recebeu {200 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 200 * 1.00

                elif controle == 2:
                    continue

            elif opcoes == 2:
                if class_e_atributos[0] == 'Mago':
                    opcoesesp = int(input(f'''{'-' * 40}
            1-> Cura      N-> Voltar
{'-' * 40}
Escolha um especial ou clique em outro qualquer número para voltar: '''))
                    if opcoesesp == 1:
                        if atributosbatalha[2] >= 60 and atributosbatalha[0] < class_e_atributos[1][0]:
                            atributosbatalha[2] -= 60
                            atributosbatalha[0] += 60
                            if atributosbatalha[0] > class_e_atributos[1][0]:
                                atributosbatalha[0] = class_e_atributos[1][0]
                            print(f'Sua vida agora é {atributosbatalha[0]}.')
                        elif atributosbatalha[0] == class_e_atributos[1][0]:
                            print('Você está com a vida cheia.')
                            continue
                        elif atributosbatalha[2] < 60:
                            print('Você está sem mana para seu especial!.')
                            continue
                    else:
                        continue
                elif class_e_atributos[0] == 'Guerreiro':
                    opcoesesp = int(input(f'''{'-' * 40}
        1-> Fúria      N-> Voltar
{'-' * 40}
Escolha um especial ou clique em outro qualquer número para voltar: '''))
                    if opcoesesp == 1:
                        if atributosbatalha[2] >= 80:
                            atributosbatalha[2] -= 80
                            atributosbatalha[1] += 10
                            print(f'Sua força agora é {atributosbatalha[1]}.')
                        else:
                            print('Você está sem mana para seu especial!.')
                            continue
                    else:
                        continue
                elif class_e_atributos[0] == 'Elfo':
                    opcoesesp = int(input(f'''{'-' * 40}
        1-> Agilidade      N-> Voltar
{'-' * 40}
Escolha um especial ou clique em outro qualquer número para voltar: '''))
                    if opcoesesp == 1:
                        if atributosbatalha[2] >= 50 and contelfa <= 4:
                            atributosbatalha[2] -= 50
                            contelfa += 1
                            print(f'Você usou {class_e_atributos[2][0]}')
                            time.sleep(1)
                            dado = random.randint(1, 6)
                            print(f'{inimigo_nome} jogou o dado para se defender!')
                            time.sleep(2)
                            print(f'Tirou o número {dado}')
                            time.sleep(2)
                            if dado == 1:
                                print(f'{inimigo_nome} se desviou do golpe!')
                            elif dado == 2:
                                print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.20} de dano!!!')
                                inimigo_atb[0] -= class_e_atributos[1][1] * 0.20
                            elif dado == 3:
                                print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.40} de dano!!!')
                                inimigo_atb[0] -= class_e_atributos[1][1] * 0.40
                            elif dado == 4:
                                print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.60} de dano!!!')
                                inimigo_atb[0] -= class_e_atributos[1][1] * 0.60
                            elif dado == 5:
                                print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 0.80} de dano!!!')
                                inimigo_atb[0] -= class_e_atributos[1][1] * 0.80
                            elif dado == 6:
                                print(f'{inimigo_nome} recebeu {class_e_atributos[1][1] * 1.00} de dano!!!')
                                inimigo_atb[0] -= class_e_atributos[1][1] * 1.00
                            time.sleep(2)
                            continue
                        elif atributosbatalha[2] < 50:
                            print('Você está sem mana para seu especial!.')
                            continue
                        elif contelfa > 4:
                            print('Você ja ultilizou o número máximo de Especial nessa batalha!')
            elif opcoes == 3:
                for l in range(len(itens)):
                    for c in range(len(itens[l])):
                        print(f'[{itens[l][c]:^20}]', end='')
                    print()
                opcoesitens = int(input(f'''{'-' * 59}
            1-> Poção de cura M     2-> Poção de cura G     
            
            3-> Poção de mana M     4-> Poção de mana G     
            
                            5-> Voltar 
{'-' * 59}
Escolha um de seus itens: '''))
                while opcoesitens > 5 or opcoesitens < 0:
                    opcoesitens = int(input(f'''{'-' * 59}
            1-> Poção de cura M     2-> Poção de cura G     
            
            3-> Poção de mana M     4-> Poção de mana G     
            
                        5-> Voltar 
{'-' * 59}
Escolha um de seus itens: '''))
                if opcoesitens == 1:
                    if itens[1][0] > 0:
                        if atributosbatalha[0] == class_e_atributos[1][0]:
                            print('Você está com a vida cheia!')
                            continue
                        else:
                            atributosbatalha[0] += 40
                            itens[1][0] -= 1
                            print('Você curou a vida!')
                            time.sleep(1)
                        if atributosbatalha[0] > class_e_atributos[1][0]:
                            atributosbatalha[0] = class_e_atributos[1][0]
                    else:
                        print('Você não tem esse item!')
                        time.sleep(1)
                        continue

                elif opcoesitens == 2:
                    if itens[1][1] > 0:
                        if atributosbatalha[0] == class_e_atributos[1][0]:
                            print('Você está com a vida cheia!')
                            continue
                        else:
                            atributosbatalha[0] += 40
                            itens[1][1] -= 1
                            print('Você curou a vida!')
                            time.sleep(1)
                        if atributosbatalha[0] > class_e_atributos[1][0]:
                            atributosbatalha[0] = class_e_atributos[1][0]
                    else:
                        print('Você não tem esse item!')
                        time.sleep(1)
                        continue

                elif opcoesitens == 3:
                    if itens[1][2] > 0:
                        if atributosbatalha[0] == class_e_atributos[1][0]:
                            print('Você está com a vida cheia!')
                            continue
                        else:
                            atributosbatalha[0] += 40
                            itens[1][2] -= 1
                            print('Você curou a vida!')
                            time.sleep(1)
                        if atributosbatalha[0] > class_e_atributos[1][0]:
                            atributosbatalha[0] = class_e_atributos[1][0]
                    else:
                        print('Você não tem esse item!')
                        time.sleep(1)
                        continue

                elif opcoesitens == 4:
                    if itens[1][3] > 0:
                        if atributosbatalha[0] == class_e_atributos[1][0]:
                            print('Você está com a vida cheia!')
                            continue
                        else:
                            atributosbatalha[0] += 40
                            itens[1][3] -= 1
                            print('Você curou a vida!')
                            time.sleep(1)
                        if atributosbatalha[0] > class_e_atributos[1][0]:
                            atributosbatalha[0] = class_e_atributos[1][0]
                    else:
                        print('Você não tem esse item!')
                        time.sleep(1)
                        continue
                elif opcoesitens == 5:
                    continue

            elif opcoes == 4:
                print('Você pulou a rodada!')
                atributosbatalha[2] += 35
                time.sleep(1)
                print('Você recuperou 35 de mana!')
                if atributosbatalha[2] > class_e_atributos[1][2]:
                    atributosbatalha[2] = class_e_atributos[1][2]

            if inimigo_atb[0] > 0:
                print(f'\033[1;40;31mVez de {inimigo_nome}\033[m'.center(60))
                time.sleep(1)
                dado = random.randint(1, 6)
                print(f'{inimigo_nome} te atacou! Você jogou o dado para tentar se defender!')
                time.sleep(2)
                print(f'Você tirou o número {dado}')
                time.sleep(1)
                if dado == 1:
                    print(f'{inimigo_nome} errou o golpe!')
                elif dado == 2:
                    print(f'Você recebeu {inimigo_atb[1] * 0.20} de dano!!!')
                    atributosbatalha[0] -= inimigo_atb[1] * 0.20
                elif dado == 3:
                    print(f'Você recebeu {inimigo_atb[1] * 0.40} de dano!!!')
                    atributosbatalha[0] -= inimigo_atb[1] * 0.40
                elif dado == 4:
                    print(f'Você recebeu {inimigo_atb[1] * 0.60} de dano!!!')
                    atributosbatalha[0] -= inimigo_atb[1] * 0.60
                elif dado == 5:
                    print(f'Você recebeu {inimigo_atb[1] * 0.80} de dano!!!')
                    atributosbatalha[0] -= inimigo_atb[1] * 0.80
                elif dado == 6:
                    print(f'Você recebeu {inimigo_atb[1] * 1.00} de dano!!!')
                    atributosbatalha[0] -= inimigo_atb[1] * 1.00

                if atributosbatalha[0] <= 50 and final == 'onbreak':
                    break

        if inimigo_atb[0] <= 0:
            opcoes = int(input(f'''{'-' * 60}
            \033[0;32mParabéns você derrotou {inimigo_nome}!\033[m
            1-> Vida     2-> Ataque     3-> Mana
{'-' * 60}
Escolha um dos atributos para aumentar 2 pontos: '''))
            time.sleep(1)
            if opcoes == 1:
                class_e_atributos[1][0] += 2
                print(f'Seus atributos ficaram assim: {class_e_atributos[1]}')
            elif opcoes == 2:
                class_e_atributos[1][1] += 2
                print(f'Seus atributos ficaram assim: {class_e_atributos[1]}')
            elif opcoes == 3:
                class_e_atributos[1][2] += 2
                print(f'Seus atributos ficaram assim: {class_e_atributos[1]}')
        if atributosbatalha[0] <= 0:
            print('\033[1;40;31mQue pena, você perdeu.\033[m')


# pygame.init()

personagens = [
    ["Guerreiro", [100, 110, 90], ["Soco Dinâmico", "Corte Vertical", "Espada secreta", "Espada Sagrada"]],
    ["Elfo", [110, 90, 100], ["Flecha rápida", "Flecha explosiva", "Flecha da Fé", "Chuva de flechas"]],
    ["Mago", [90, 100, 110], ["Feitiço", "Sabor Veneno", "Bola sombria", "Onda infernal"]],
]

class_e_atributos = [ver(input("Escolha: "), ["1", "2"])]
class_e_atributos = [i for i in personagens if personagens.index(i) == class_e_atributos[0] - 1]
class_e_atributos = [v for v in class_e_atributos[0]]

itens = [['Poção de cura M', 'Poção de cura G', 'Poção de mana M', 'Poção de mana G'], [1, 1, 1, 1]]
# music_mascariane = pygame.mixer.music.load('Musiquinha de mascariane.mp3')
# pygame.mixer.music.play(-1)
combate([2000, 500], 'Mascariane', 'off')
print(class_e_atributos[1])
