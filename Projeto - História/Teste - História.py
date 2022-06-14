# by Jefferson.
from prettytable import prettytable
####
import time
import random

personagens = ["Guerreiro", "Arqueiro", "Mago"]

lista = [0, 0, 0]  # [HP, Força, XP]


def txt(texto):
    for i in range(1):
        for c in texto:
            print(c, end='')
            # time.sleep(0.03)
        print()


'''txt("=-" * 32)
print(f"""{'|':<0} {'Bem-Vindo(a) ao [NOME DO JOGO]':^60} {'|'}
{'|':<0} {'':^60} {'|'}
{'|':<0} {'Selecione uma classe para começar a jornada!':^60} {'|'}
{'|':<0} {'':^60} {'|'}
{'|':<0} {'1.Guerreiro  2.Elfo  3.Mago':^60} {'|'}""")
txt("=-" * 32)
'''

'''table = prettytable()

table.field_names = ['name', 'age', 'city']
table.add_row(["alice", 20, "adelaide"])
table.add_row(["bob", 20, "brisbane"])
table.add_row(["chris", 20, "cairns"])
table.add_row(["david", 20, "sydney"])
table.add_row(["ella", 20, "melbourne"])'''

def dado():
    x = random.randint(1, 6)
    return x


numero = 0
for i in range(1):
    numero = dado()
    print(numero)

