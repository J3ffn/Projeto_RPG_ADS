# by Jefferson.
####################
import time
import random

####################

print("Atenção, pedimos que utilize apenas números para jogar o jogo, obrigado!")
time.sleep(5)
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


def historia(linha_1, linha_2, linha_3, linha_4, linha_5, linha_6):
    print(f"""
{f'{linha_1}':^60}
{f'{linha_2}':^60}
{f'{linha_3}':^60}
{f'{linha_4}':^60}
{f'{linha_5}':^60}
{f'{linha_6}':^60}""")
    escolha.append(int(input("Qual classe deseja? ")))


##################################
### Lore dos personagens.
# - Guerreiro.
guerreiro = ""

# - Elfa.
elfa = ""

# - Mago.
mago = ""

###

personagens = ["Guerreiro", "Arqueiro", "Mago"]
escolha = []
lista = [0, 0, 0]  # [HP, Força, Mana]

# Início.
historia(
    "Bem-vindo(a) ao [Nome do jogo]",
    "",
    "Selecione uma classe para começar a jornada.",
    "",
    f"1.{personagens[0]}, 2.{personagens[1]}, 3.{personagens[2]}",
    f""
)



