# by Jefferson.
from prettytable import PrettyTable
####
import time
import random

personagens = ["Guerreiro", "Arqueiro", "Mago"]
escolha = []
lista = [0, 0, 0]  # [HP, Força, Mana]


def dado():
    x = random.randint(1, 6)
    return x

'''numero = 0
for i in range(1):
    numero = dado()
    print(numero)'''


def txt(texto):
    for i in range(1):
        for c in texto:
            print(c, end='')
            # time.sleep(0.03)
        print()


table = PrettyTable()
superior = table.field_names = ['Classe', 'Vida', 'Força', 'Mana']
tabela_guerreiro = table.add_row(["Guerreiro", 100, 110, 90])
tabela_elfo = table.add_row(["Elfo", 110, 90, 100])
tabela_mago = table.add_row(["Mago", 90, 100, 110])

txt("=-" * 32)
print(f"""{'|':<0} {'Bem-Vindo(a) ao [NOME DO JOGO]':^60} {'|'}
{'|':<0} {'':^60} {'|'}
{'|':<0} {'Selecione uma classe para começar a jornada!':^60} {'|'}
{'|':<0} {f'{superior}':^60} {'|'}
{'|':<0} {f'{tabela_guerreiro}':^60} {'|'}
{'|':<0} {f'{tabela_elfo}':^60} {'|'}
{'|':<0} {f'{tabela_mago}':^60} {'|'}
{'|':<0} {'1.Guerreiro  2.Elfo  3.Mago':^60} {'|'}""")
txt("=-" * 32)
escolha.append(int(input("Qual classe deseja? ")))


table.field_names = ['Classe', 'Vida', 'Força', 'Mana']
table.add_row(["Guerreiro", 100, 110, 90])
table.add_row(["Elfo", 110, 90, 100])
table.add_row(["Mago", 90, 100, 110])

print(table)

