# by Josias.
import time


def txt(texto):
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
txt("=-" * 32)
