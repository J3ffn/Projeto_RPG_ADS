# by Josias.
import time
import random
'''def txt(texto):
    for i in range(1):
        for c in texto:
            print(c, end='')
            # time.sleep(0.03)
        print()


txt("=-" * 32)
print(f"""{'|':<0} {'Bem-Vindo(a) ao [NOME DO JOGO]':^60} {'|'}
{'|':<0} {'':^60} {'|'}
{'|':<0} {'Selecione uma classe para começar a jornada!':^60} {'|'}
{'|':<0} {'':^60} {'|'}
{'|':<0} {'1-> Guerreiro  2-> Elfo  3-> Mago':^60} {'|'}""")
txt("=-" * 32)'''
def dado():
    return random.randint(1,6)

atributos = [90, 100, 110]
inimigo1 = [50, 100, 0]

print('Um inimigo veio em sua direção, se prepare para seu primeiro combate!')
opcoes = int(input(f'''
1-> Ataque base     2-> Habilidades

3-> Defesa          4-> Itens

Escolha o que você vai fazer: '''))

if opcoes == 1:
    
