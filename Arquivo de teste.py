import pygame

'''itens = [['Poção Pequena', 'Poção Média', 'Poção Grande'],
         [4, 5, 6]]

if itens[1][0] > 0:
    print("É maior.")
else:
    print("Não é maior.")'''

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

'''personagens = {
        "p1": ["Guerreiro", 100, 0, 90],
        "p2": ["Elfo", 110, 90, 100],
        "p3": ["Mago", 90, 100, 110],
}

print(personagens["p1"][1:])
print(personagens["p2"][0])
print(personagens.get("p1"))
print(personagens.keys())'''

'''impacto_na_historia = {

}
impacto_na_historia["IH_1"] = "Não sabe que o ovo estava lá."

print(impacto_na_historia.keys())'''

'''import time, random

def dado():
    return random.randint(1, 3)


class_e_atributos = ["Guerreiro", [100, 100, 90], ["Corte vertical", "Espada sagrada", "H3"]]
inimigo = [200]
numero_tirado = 1
escolha = []
print(numero_tirado)
aux = int(input("Usar habilidade? [1]Sim [2]Não: "))

if numero_tirado == 1:
    print(f"Você usou o ataque {class_e_atributos[2][0]}")
    print(f"Dano: {class_e_atributos[1][1] + (class_e_atributos[1][1] * 0.15) if aux == 1 and class_e_atributos[0] == 'Guerreiro' else class_e_atributos[1][1]}")
    inimigo[0] -= class_e_atributos[1][1] + (class_e_atributos[1][1] * 0.15) if aux == 1 and class_e_atributos[0] == 'Guerreiro' else class_e_atributos[1][1]
    print(f"Vida do inimigo: {inimigo[0]}")

if numero_tirado == 2:
    print(f"Você usou o ataque {class_e_atributos[2][1]}")

if numero_tirado == 3:
    print(f"Você usou o ataque {class_e_atributos[2][2]}")'''

'''personagens = [
    ["Guerreiro", [100, 0, 90]],
    ["Elfo", [110, 90, 100]],
    ["Mago", [90, 100, 110]],
]

print(personagens[0][0]) # Gerreiro
print(personagens[1][0]) # Elfo
print(personagens[2][0]) # Mago
itens = ['Poção de cura M', 'Poção de cura G', 'Poção de mana M', 'Poção de mana G', [0, 0, 0, 0]]
print(itens[4][1])'''
'''class_e_atributos = []
personagens = [
    [["Guerreiro"], [100, 90, 90]],
    [["Elfo"], [110, 90, 100]],
    [["Mago"], [90, 100, 110]],
]

class_e_atributos.append(int(input("Sua escolha: ")))
class_e_atributos = [i for i in personagens if personagens.index(i) == class_e_atributos[0] - 1]
class_e_atributos = [v for v in class_e_atributos[0]]

print(f'{class_e_atributos[1][1] += 5}')'''

'''import time
def txt(texto, tempo):
    for i in texto:
        print(i, end=" ")
        time.sleep(tempo)

txt("Equipe: Jefferson Mangueira Izaquiel Josias Carneiro", 0.2)
'''

'''print(f"{'-' * 40}\n"
       f"{'Continuaremos com os esperimentos agora.':^40}\n" 
       f"{'Sigam o protocolo.':^40}\n"
       "Pela igreja!\n"
       f"{'Ass. Bispo Melo':>40}\n"
       f"{'-'* 40}")'''

'''escolhas = []
escolhas.append(input("Escolhas: "))
opcoes = ["1", "2", "3", "4"]
while escolhas[-1].isnumeric is not True or escolhas[-1].isnumeric:
    try:
        if int(escolhas[-1]):
            if escolhas[-1] in opcoes:
                c = int(escolhas[-1])
                escolhas.pop()
                escolhas.append(c)
                break

            if int(escolhas[-1]) <= 0:
                escolhas[-1] += 2

            else:
                escolhas[-1] += 2


    except ValueError:
        escolhas.pop()
        print("Escolha uma opção válida!")
        escolhas.append(input("Escolha: "))

    except TypeError:
        escolhas.pop()
        print("Escolha uma opção válida!")
        escolhas.append(input("Escolha: "))

print("Terminou o laço e continuou")'''

'''import time


def txt(texto, tempo):
    for i in texto:
        print(i, end="")
        time.sleep(tempo)


txt("Um tempo considerável", 0.06)'''


pygame.init()
pygame.mixer.music.load("Musiquinha de mascariane.mp3")
pygame.mixer.music.play(-1)
pygame.event.wait()


