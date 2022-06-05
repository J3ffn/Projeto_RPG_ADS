import time

historia = f""
nome = "Jefferson"

personagens = ["Guerreiro", "Arqueiro", "Mago"]

lista = [0, 0, 0]   # [HP, Força, XP]

def txt(texto):
    for i in range(1):
        for c in texto:
            print(c, end='')
            time.sleep(0.21)
        print()

print("=-" * 30)
txt("Bem vindo ao RPG!")

print("-=" * 30)

'''historia = "RPG top"
for e, x in enumerate(range(len(historia))):
    time.sleep(0.21)
    print(historia[e], end="")
print()'''


'''import time


def slowprint(texto):
    for e, c in enumerate(texto):
        print(c[e], end='')
        time.sleep(0.2)


slowprint('E lá vamos nós')
slowprint(nome)'''


'''def txt(texto):
    for c in texto:
        print(c, end='')
        time.sleep(0.2)


txt(f'Bom dia! {nome} você escolheu ser um!')'''

