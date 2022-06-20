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

'''atributos = [100, 100, 100]
opcoes = input(f''{'-' * 62}
              Parabéns você derrotou MASCARIANE!
             1-> Vida     2-> Ataque     3-> Mana
{'-' * 62}
Escolha um dos atributos para aumentar 2 pontos: '')
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
'''

'''class_e_atributos = [input("Escolha: ")]

verificacao = 0
c = 0
if class_e_atributos[0].isnumeric():
    class_e_atributos = int
else:
    while class_e_atributos[0].isnumeric() is not True:
        class_e_atributos.pop()
        class_e_atributos.append(input("letras não são permetidas, utilize números para escolher: "))
    class_e_atributos[0] = int
numeros = [1, 2, 3]
while class_e_atributos[0] not in numeros:
    class_e_atributos.pop()
    class_e_atributos.append(input("Escolha entre os número 1, 2 e 3 para escolher sua classe: "))

    if class_e_atributos[0].isnumeric():
        class_e_atributos = int
    else:'''

'''class_e_atributos = [input("Escolha: ")]
v = 0
while v != 1:
    try:
        while class_e_atributos[0].isnumeric() is not True:
            class_e_atributos.pop()
            class_e_atributos.append(input("Digite um número: "))
        class_e_atributos[0] = int

        while :
            class_e_atributos.pop()
            class_e_atributos.append(input("Número: "))
            print("Não está.")

    except ValueError:
        while True:
            print("Por favor, utilize apénas números para jogar.")

            class_e_atributos.append(int(input("Escolha sua classe: ")))'''

personagens = {
        "p1": ["Guerreiro", 100, 0, 90],
        "p2": ["Elfo", 110, 90, 100],
        "p3": ["Mago", 90, 100, 110],
}

print(personagens["p1"][1:])
print(personagens["p2"][0])
print(personagens.get("p1"))
print(personagens.keys())