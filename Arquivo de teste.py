'''itens = [['Poção Pequena', 'Poção Média', 'Poção Grande'],
         [4, 5, 6]]

if itens[1][0] > 0:
    print("É maior.")
else:
    print("Não é maior.")'''

import time

'''texto = f"""SOIDJAODIAJSOIJASDIAJS
poiasjdpiodsajdpasoj 
KdACBasadkopACS 
doaiwjopaisdjasdpasdojad´paso"""
print(texto)'''

atributos = [100, 100, 100]
opcoes = input(f'''{'-' * 62}
              Parabéns você derrotou MASCARIANE!
             1-> Vida     2-> Ataque     3-> Mana
{'-' * 62}
Escolha um dos atributos para aumentar 2 pontos: ''')
if opcoes == 1:
    atributos[0] += 2
    print(f'Seus atributos ficaram assim: {atributos}')
elif opcoes == 2:
    atributos[1] += 2                  # VOU AJEITAR UMAS COISAS AQUI
    print(f'Seus atributos ficaram assim: {atributos}')
elif opcoes == 3:
    atributos[2] += 2
    print(f'Seus atributos ficaram assim: {atributos}')
time.sleep(3)
