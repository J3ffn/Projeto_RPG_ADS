# by Jefferson.
####################
import time
import random
####################

##################################
## DADO.
def dado():
    x = random.randint(1, 6)
    return x


'''numero = 0
for i in range(1):
    numero = dado()
    print(numero)'''

## Impressão de texto.
def txt(texto):
    for i in range(1):
        for c in texto:
            print(c, end='')
            time.sleep(0.03)
        print()


def quadrado_historia(t):
    txt("=-" * 32)
    print(f"""{'|':<0} {'Bem-Vindo(a) ao [NOME DO JOGO]':^60} {'|'}
    {'|'} {'':^60} {'|'}
    {'|'} {'Selecione uma classe para começar a jornada!':^60} {'|'}
    {'|'} {f'':^60} {'|'}
    {'|'} {'1.Guerreiro  2.Elfo  3.Mago':^60} {'|'}
    {'|'} {'|':^20}{f'':^20}{'|':^20} {'|'}""")
    txt("=-" * 32)
    escolha.append(int(input("Qual classe deseja? ")))


##################################

personagens = ["Guerreiro", "Arqueiro", "Mago"]
escolha = []
lista = [0, 0, 0]  # [HP, Força, Mana]


quadrado_historia()
