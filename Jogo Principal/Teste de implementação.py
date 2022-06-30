# Testar o código juntando história e combate.
import time
import random

def combate(inimigo_atb, inimigo_nome):
    atributosbatalha = atributos[:]
    while inimigo_atb[0] > 0 and atributosbatalha[0] > 0:
        print('-' * 40)
        print(f'[HP: {atributosbatalha[0]}]{f"[HP.I: {inimigo_atb[0]}]":>32}')
        print(f'[MANA: {atributosbatalha[2]}]')
        opcoes = int(input(f'''{'-' * 40}
    1-> Ataque      2-> Especial      

    3-> Itens       4-> Pular rodada
{'-' * 40}
Escolha o que você vai fazer: '''))
        while opcoes > 4 or opcoes < 0:
            print('-' * 40)
            print(f'[HP: {atributosbatalha[0]}]{f"[HP.I: {inimigo_atb[0]}]":>32}')
            print(f'[MANA: {atributosbatalha[2]}]')
            opcoes = int(input(f'''{'-' * 40}
    1-> Ataque      2-> Especial      

    3-> Itens       4-> Pular rodada
{'-' * 40}
Escolha o que você vai fazer: '''))


        if opcoes == 1:
            controle = int(input('Se você quiser jogar o dado para atacar digite (1), se quiser voltar digite (2): '))
            while 1 != controle != 2:
                controle = int(input("Para jogar o dado digite (1), para voltar digite (2): "))
            if controle == 1:
                print('O dado foi jogado...')
                time.sleep(1)
                dado = random.randint(1, 6)
                print(f'Você jogou o dado e tirou o número {dado}!')
                if dado == 1 or dado == 2 or dado == 3:
                    print(f'Você usou Feitiço')
                    time.sleep(1)
                    dado = random.randint(1, 6)
                    print(f'{inimigo_nome} jogou o dado para se defender!')
                    time.sleep(2)
                    print(f'Tirou o número {dado}')
                    time.sleep(2)
                    if dado == 1:
                        print(f'{inimigo_nome} se desviou do golpe!')
                    elif dado == 2:
                        print(f'{inimigo_nome} recebeu {atributos[1] * 0.20} de dano!!!')
                        inimigo_atb[0] -= atributos[1] * 0.20
                    elif dado == 3:
                        print(f'{inimigo_nome} recebeu {atributos[1] * 0.40} de dano!!!')
                        inimigo_atb[0] -= atributos[1] * 0.40
                    elif dado == 4:
                        print(f'{inimigo_nome} recebeu {atributos[1] * 0.60} de dano!!!')
                        inimigo_atb[0] -= atributos[1] * 0.60
                    elif dado == 5:
                        print(f'{inimigo_nome} recebeu {atributos[1] * 0.80} de dano!!!')
                        inimigo_atb[0] -= atributos[1] * 0.80
                    elif dado == 6:
                        print(f'{inimigo_nome} recebeu {atributos[1] * 1.00} de dano!!!')
                        inimigo_atb[0] -= atributos[1] * 1.00
                    time.sleep(2)
                elif dado == 4:
                    if atributosbatalha[2] < 40:
                        print('Você não tem mana o suficiente para dá esse golpe!')
                        time.sleep(2)
                    else:
                        atributosbatalha[2] -= 40
                        print('Você usou Bola de Fogo')
                        time.sleep(1)
                        dado = random.randint(1, 6)
                        print(f'{inimigo_nome} jogou o dado para se defender!')
                        time.sleep(2)
                        print(f'Tirou o número {dado}')
                        time.sleep(2)
                        if dado == 1:
                            print(f'{inimigo_nome} se desviou do golpe!')
                        elif dado == 2:
                            print(f'{inimigo_nome} recebeu {120 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 120 * 0.40
                        elif dado == 3:
                            print(f'{inimigo_nome} recebeu {120 * 0.40} de dano!!!')
                            inimigo_atb[0] -= 120 * 0.40
                        elif dado == 4:
                            print(f'{inimigo_nome} recebeu {120 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 120 * 0.80
                        elif dado == 5:
                            print(f'{inimigo_nome} recebeu {120 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 120 * 0.80
                        elif dado == 6:
                            print(f'{inimigo_nome} recebeu {120 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 120 * 1.00
                        time.sleep(2)
                elif dado == 5:
                    if atributosbatalha[2] < 60:
                        print('Você não tem mana o suficiente para dá esse golpe!')
                        time.sleep(2)
                    else:
                        atributosbatalha[2] -= 60
                        print('Você usou Raio de gelo')
                        time.sleep(1)
                        dado = random.randint(1, 6)
                        print(f'{inimigo_nome} jogou o dado para se defender!')
                        time.sleep(2)
                        print(f'Tirou o número {dado}')
                        time.sleep(2)
                        if dado == 1:
                            print(f'{inimigo_nome} se desviou do golpe!')
                        elif dado == 2:
                            print(f'{inimigo_nome} recebeu {140 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 140 * 0.60
                        elif dado == 3:
                            print(f'{inimigo_nome} recebeu {140 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 140 * 0.60
                        elif dado == 4:
                            print(f'{inimigo_nome} recebeu {140 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 140 * 0.80
                        elif dado == 5:
                            print(f'{inimigo_nome} recebeu {140 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 140 * 0.80
                        elif dado == 6:
                            print(f'{inimigo_nome} recebeu {140 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 140 * 1.00
                        time.sleep(2)
                elif dado == 6:
                    if atributosbatalha[2] < 80:
                        print('Você não tem mana o suficiente para dá esse golpe!')
                        time.sleep(2)
                    else:
                        atributosbatalha[2] -= 80
                        print('Você usou Raio solar')
                        time.sleep(1)
                        dado = random.randint(1, 6)
                        print(f'{inimigo_nome} jogou o dado para se defender!')
                        time.sleep(2)
                        print(f'Tirou o número {dado}')
                        time.sleep(2)
                        if dado == 1:
                            print(f'{inimigo_nome} se desviou do golpe!')
                        elif dado == 2:
                            print(f'{inimigo_nome} recebeu {160 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 160 * 0.60
                        elif dado == 3:
                            print(f'{inimigo_nome} recebeu {160 * 0.60} de dano!!!')
                            inimigo_atb[0] -= 160 * 0.60
                        elif dado == 4:
                            print(f'{inimigo_nome} recebeu {160 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 160 * 0.80
                        elif dado == 5:
                            print(f'{inimigo_nome} recebeu {160 * 0.80} de dano!!!')
                            inimigo_atb[0] -= 160 * 0.80
                        elif dado == 6:
                            print(f'{inimigo_nome} recebeu {160 * 1.00} de dano!!!')
                            inimigo_atb[0] -= 160 * 1.00
                        time.sleep(2)
            elif controle == 2:
                continue


        elif opcoes == 2:
            opcoesesp = int(input(f'''{'-' * 40}
        1-> Cura      N-> Voltar
{'-' * 40}
Escolha um especial ou clique em outro qualquer número para voltar: '''))
            if opcoesesp == 1:
                if atributosbatalha[2] >= 60:
                    atributosbatalha[2] -= 60
                    atributosbatalha[0] += 60
                    if atributosbatalha[0] > atributos[0]:
                        atributosbatalha[0] = atributos[0]
                    print(f'Sua vida agora é {atributosbatalha[0]}')
                else:
                    print('Você não tem mana o suficiente para usar seu especial!')
                    continue
            else:
                continue


        elif opcoes == 3:
            for l in range(len(itens)):
                for c in range(len(itens[l])):
                    print(f'[{itens[l][c]:^13}]', end='')
                print()
            opcoesitens = int(input(f'''{'-' * 89}
        1-> Poção Pequena     2-> Poção Média     3-> Poção Grande     4-> Voltar
{'-' * 89}
Escolha um de seus itens: '''))
            while opcoesitens > 4 or opcoesitens < 0:
                opcoesitens = int(input(f'''{'-' * 89}
        1-> Poção Pequena     2-> Poção Média     3-> Poção Grande     4-> Voltar
{'-' * 89}
Escolha um de seus itens: '''))
            if opcoesitens == 1:
                if itens[1][0] > 0:
                    atributosbatalha[0] += 20
                    itens[1][0] -= 1
                    print('Você curou a vida!')
                    time.sleep(1)
                    if atributosbatalha[0] == atributos[0]:
                        print('Você está com a vida cheia!')
                        continue
                    elif atributosbatalha[0] > atributos[0]:
                        atributosbatalha[0] = atributos[0]
                else:
                    print('Você não tem esse item!')
                    time.sleep(1)

            elif opcoesitens == 2:
                if itens[1][1] > 0:
                    atributosbatalha[0] += 40
                    itens[1][1] -= 1
                    print('Você curou a vida!')
                    time.sleep(1)
                    if atributosbatalha[0] == atributos[0]:
                        print('Você está com a vida cheia!')
                        continue
                    elif atributosbatalha[0] > atributos[0]:
                        atributosbatalha[0] = atributos[0]
                else:
                    print('Você não tem esse item!')
                    time.sleep(1)

            elif opcoesitens == 3:
                if itens[1][2] > 0:
                    atributosbatalha[0] += 60
                    itens[1][2] -= 1
                    print('Você curou a vida!')
                    time.sleep(1)
                    if atributosbatalha[0] == atributos[0]:
                        print('Você está com a vida cheia!')
                        continue
                    elif atributosbatalha[0] > atributos[0]:
                        atributosbatalha[0] = atributos[0]
                else:
                    print('Você não tem esse item!')
                    time.sleep(1)
            elif opcoesitens == 4:
                continue


        elif opcoes == 4:
            print('Você pulou a rodada!')
            atributosbatalha[2] += 20
            time.sleep(1)
            print('Você recuperou 20 de mana!')
            if atributosbatalha[2] > atributos[2]:
                atributosbatalha[2] = atributos[2]


        if inimigo_atb[0] > 0:
            print(f'\033[1;40;31mVez de {inimigo_nome}\033[m')
            time.sleep(1)
            dado = random.randint(1, 6)
            print(f'{inimigo_nome} te atacou! Você jogou o dado para tentar se defender!')
            time.sleep(2)
            print(f'Você tirou o número {dado}')
            time.sleep(1)
            if dado == 1:
                print(f'{inimigo_nome} errou o golpe!')
            elif dado == 2:
                print(f'Você recebeu {inimigo_atb[1] * 0.20} de dano!!!')
                atributosbatalha[0] -= inimigo_atb[1] * 0.20
            elif dado == 3:
                print(f'Você recebeu {inimigo_atb[1] * 0.40} de dano!!!')
                atributosbatalha[0] -= inimigo_atb[1] * 0.40
            elif dado == 4:
                print(f'Você recebeu {inimigo_atb[1] * 0.60} de dano!!!')
                atributosbatalha[0] -= inimigo_atb[1] * 0.60
            elif dado == 5:
                print(f'Você recebeu {inimigo_atb[1] * 0.80} de dano!!!')
                atributosbatalha[0] -= inimigo_atb[1] * 0.80
            elif dado == 6:
                print(f'Você recebeu {inimigo_atb[1] * 1.00} de dano!!!')
                atributosbatalha[0] -= inimigo_atb[1] * 1.00


    if inimigo_atb[0] <= 0:
        opcoes = int(input(f'''{'-' * 60}
                  \033[0;32mParabéns você derrotou {inimigo_nome}!\033[m
            1-> Vida     2-> Ataque     3-> Mana
{'-' * 60}
Escolha um dos atributos para aumentar 2 pontos: '''))
        time.sleep(1)
        if opcoes == 1:
            atributos[0] += 2
            print(f'Seus atributos ficaram assim: {atributos}')
        elif opcoes == 2:
            atributos[1] += 2
            print(f'Seus atributos ficaram assim: {atributos}')
        elif opcoes == 3:
            atributos[2] += 2
            print(f'Seus atributos ficaram assim: {atributos}')
    if atributosbatalha[0] <= 0:
        print('\033[1;40;31mQue pena, você perdeu.\033[m')

itens = [['Poção Pequena', 'Poção Média', 'Poção Grande'], [1, 1, 0]]
atributos = [90, 100, 100]

print("Atenção, pedimos que utilize apenas números para jogar o jogo, obrigado!")
time.sleep(0.4)

'''print(f"""Tutorial da tela de combate:
{'-' * 98}
\033[1;32m[HP: 000]\033[m \033[1;31m<-\033[m Sua VIDA atual.     Vida atual do inimiso. \033[1;31m->\033[m \033[1;35m[HP.i: 000]\033[m 
\033[1;34m[MANA: 000]\033[m \033[1;31m<-\033[m Sua MANA atual.
    1-> Ataque      2-> Especial      

    3-> Itens       4-> Pular rodada
Opção 1(Ataque): Nele será você poderá escolher dentre os 3 ataques disponíveis.
Opção 2(Especial): Cada classe possui um especial único, que é explicado após a escolha da classe.
Opção 3(Itens): Aqui terá poções de cura e mana, mas a quantidade varia por classe.
Opção 4(Pular rodada): Você pode pular a rodada para recuperar mana.
{'-' * 98}""")

time.sleep(20)'''

## Impressão de texto.
def txt(texto, tempo):
    for i in range(1):
        for c in texto:
            print(c, end='')
            time.sleep(tempo if "-" not in texto else 0)
        print()


##################################
nome_do_jogador = ""
# # # Lore dos personagens.

# - Guerreiro.
guerreiro_historia = f"""    Em um reino conhecido como Mambla, era acolhido um bebê recém-nascido que estava 
boiando numa cesta no rio por uma das filhas do rei Alexandre, na cesta estava escrito apenas 
seu nome, {nome_do_jogador}, por sorte, a família real era conhecida por sua bondade com o seupovo, 
{nome_do_jogador} estava em boas mãos. Ao completar 15 anos já era reconhecido pelo rei pela sua bravura 
e qualidade em lutas com espadas. No seu aniversário de 16 anos é comunicado ao rei que o 
papa da igreja central faria uma visita ao reino no mesmo dia, logo foram se programar para a 
chegada do papa, porém, ao longe se avista um homem que usava uma capa preta com um
capuz cobrindo seu rosto, parecia estar falando algo, quando do nada uma rocha era invocada, 
cobria todo o céu do reino e estava bem em cima do castelo, parecia estar de noite, mas também 
uma carta era entregue ao rei, dizendo: "Entregue o ovo, ou será amassado.", Soando frio o rei 
convoca seus melhores homens para levar sua família até um local seguro, mas não era possível 
sair, pois o mago havia criado uma espécie de barreira, mas existia uma falha, porém, nela só 
podiam passar pessoas baixas, e o único que conseguiu passar por ela foi {nome_do_jogador}, tendo que 
deixar sua família e amigos para trás. Seu pai tentaria combater o mago ao invés de fazer o que 
foi pedido na carta, pois dizia ser perigoso entregá-lo a igreja. Percebendo a aproximação de 
tropas no portão, o misterioso mago solta a rocha em cima do reino, destruindo tudo, mas por 
causa dos destroços ele acaba se ferindo e rasgando sua capa, revelando assim sua marca da 
igreja, ele não ligava de ter a marca exposta, pois deduzia que todos estavam mortos, porém, 
do outro lado estava {nome_do_jogador}, se engasgando com as próprias lágrimas, mas atento a marca. 
Depois disso, {nome_do_jogador} jura vingança à igreja. E assim sua ambição escolhida, e sua história 
começará a ser escrita."""

# - Elfa.
elfa_historia = """    Logo abaixo das cidadelas de Kalezar, em Trozar, no campo, há uma pequena vila
escondida do resto do reino, no qual vive Elírio, filho de Jor e Maraine, um jovem sem
posses que almeja uma vida melhor para ele e sua família. Filho de uma costureira e um
artesão, não teve muitas oportunidades, e agora, após homem feito, quer uma aventura
que garantirá uma vida melhor.
    Os pais trabalham confeccionando peças de roupa e objetos para a igreja a mando do
Bispo Mascariane, que a todo fim de estação encomenda vários objetos, porém o ganho
é mínimo. O bispo aproveita da boa-fé da família para não pagar quase nada e embora
os esforços de Elírio para livrar os pais dessa ilusão, nada resolve-se.
    Então, um dia, enquanto entregava os tapetes pedidos pelo cardeal, ouviu de um dos
vassalos, que algo da igreja foi roubado e o bispo está louco, disse que queimará vivo o
ladrão.
    Elírio entrou em choque, sabia o que era e não era do Bispo de modo algum... Sua vó
contava que eras atrás em Trozar, que outrora fora um reino majestoso, havia certos
tesouros, que garantiram o sustento do reino por um tempo, um em especial, era fonte
da riqueza de Trozar. Só que durante um festival de inverno, o objeto foi roubado e
Trozar caiu em desgraça, sua avó ainda dizia que Trozar era um reino de elfos. Sua mãe
irritava-se sempre que sua avó contava isso, então não sabia mais nada.  Ela morreu
depois tempos, e a única coisa que insistiu foi que ele usasse o arco e flecha como arma,
e assim ele o fez, mesmo que escondido.
    E agora tinha essa oportunidade! Iria atrás do quer que foi roubado e ficaria rico! E mais,
tiraria os pais do controle sofrido por a igreja. Tudo daria certo..."""

# - Mago.
mago_historia = """"""

######
personagens = [
    ["Guerreiro", [100, 0, 90]],
    ["Elfo", [110, 90, 100]],
    ["Mago", [90, 100, 110]],
]
class_e_atributos = []
escolhas = []
continuar = "s"
# Início.
# while continuar != "n":
print(f"""
{'-' * 60}
{'Bem-vindo(a) ao [Nome do jogo]'.center(60)}

{'Selecione uma classe para começar a jornada.':^60}
{"[1]":^20} {"[2]":^20} {"[3]":^20}
{personagens[0][0]:^20} {personagens[1][0]:^20} {personagens[2][0]:^20}
{'-' * 60}""")
class_e_atributos.append(int(input("Sua escolha: ")))

# Depis colocar aqui uma verificação de erro.

class_e_atributos = [i for i in personagens if personagens.index(i) == class_e_atributos[0] - 1]
class_e_atributos = [v for v in class_e_atributos[0]]

nome_do_jogador = input(f"Nós diga o seu nome/nick, ó grande {class_e_atributos[0]}: ")

if class_e_atributos[0] == "Guerreiro":
    # txt(guerreiro_historia)
    txt(f"""
    Você sabe que sozinho não consegue vingar sua famíla,
então decide ir a Minic, onde o rei era o melhor amigo de
seu pai.
""", 0.06)
    escolhas.append(int(input("Reinos:\n"
                              "[1]. Minic\n"
                              "[2]. Blugg\n"
                              "Sua escolha: ")))
# Adicionar verificação de erro.

    if escolhas[0] == 1:
        txt("À caminho de Minic, você encontra saqueadores. Eles ainda não\n"
            "o viram, mas deve decidir se deverá desviar(demorando mais) ou\n"
            "atacar antes que eles te vejam", 0.04)

        escolhas.append(int(input("Escolhas:\n"
                                  "[1].Desviar caminho.\n"
                                  "[2].Conversar.\n"
                                  "[3].Batalhar.\n"
                                  "Sua escolha: ")))
        # Adicionar verificação de erro à escolha.
        if escolhas[1] == 1:
            txt("\nDesviando o caminho você encontra um ansião antes do reino.\n", 0.11)
            txt("Ele te alerta sobre os perigos eminentes daquela floresta!\n"
                "Nela há ógros, ursos e lobos terríveis.\n", 0.14)
            txt("Seguinto em frente você encontra um buraco", 0.13)
            escolhas.append(int(input("Escolhas:"
                                      "[1].Seguir em frente.\n"
                                      "[2].Analisar o buraco.\n"
                                      "Sua escolha: ")))
            if escolhas[2] == 1:
                txt("Seguindo em frente um bando de lobos o esperava, era"
                    "estranho, todos do bando agiam como um só alí.\n", 0.14)
                txt("Prepare-se, uma batalha está para começar!!", 0.15)
                time.sleep(0.2)
                # Combate:
                # inimigo_nome = "Lobos"
                # inimigo_atb = [400, 90] # HP # Força
                # Luta normal com o código.
                txt("A noite está chegando e você está exausto.", 0.13)
                escolhas.append(int(input("Escolhas:\n"
                                          "[1].Ascender uma fogueira e descansar.\n"
                                          "[2].Continuar para não encontrar monstros.\n"
                                          "Sua escolha: ")))
                if escolhas[3] == 1:
                    txt("No dia seguinte, segue viágem para o reino.", 0.12)
                    txt("Chegando lá, é muito bem recebido pela realeza, pois\n"
                        "seu pai era amigo do rei Julius.", 0.11)
                    txt('O rei o pergunta, "o que trás o jovem príncipe ao meu humilde reino?"', 0.1)
                    escolhas.append(int(input("Escolhas:\n"
                                              "[1].Contar o que aconteceu com o reino e seu pai.\n"
                                              "[2].Não contar, mas, tentar converte-lo a ficar\n"
                                              "contra a catedral.")))
                    # Adicionar verificação de erro.
                    if 1 == escolhas[4] == 2:  # Final bom
                        if escolhas[4] == 2:
                            txt("O rei não vê necessidade em entra em guerra contra a catedral.\n"
                                "Porém, tenta entrar em contato com o seu pai, descobrindo que\n"
                                "ele está morto. Te forçando a contar o que aconteceu.", 0.5)
                        elif escolhas[4] == 1:
                            txt(f"Por ser amigo da família de {nome_do_jogador}, o rei acredita\n"
                                f"sem pestanejar", 0.11)
                        txt("Fica horrorizado com o que a igreja foi capaz de fazer nas sombras.", 0.11)
                        txt(f'O rei diz a {nome_do_jogador} que sozinhos não serão capazes de\n'
                            'derrotar a igreja pelo tamanho descrito por você.', 0.1)
                        txt("Então terão que convencer outros reinos que a igreja\n"
                            "não é o que aparenta.", 0.1)
                        txt("Além de terem que bolar uma estratégia!\n", 0.1)
                        time.sleep(0.3)
                        txt("Aproximadamente 2 anos mais tarde..", 0.05)
                        time.sleep(0.2)
                        txt("Apenas conseguiram fazer o reino Blugg aliar-se a eles para derrubar a\n"
                            "igreja. Mesmo falando outra lingua, se comunicavam com desenhos.", 0.12)
                        txt("Mesmo sendo misteriosa, mostrou ser muito poderosa em combate,\n"
                            "pois por teram sua própria lingua, tornam suas técnicas exclusividade\n"
                            "do povo local", 0.12)
                        time.sleep(1.2)
                        txt("\nRei Julius:\n"
                            "-Estão todos prontos?!\n"
                            "Tropas:\n"
                            "-Siim!!\n"
                            "-̪ɐ̃s̪kr̩t̪ɐm\n", 0.11)
                        txt(f"{nome_do_jogador}:\n"
                            f"-AVANTE!!\n", 0.11)
                        time.sleep(0.4)
                        txt("À caminho da capital.\n"
                            "Mascarine já estava ciente da guerra eminente.\n"
                            'Então reuniu todos os reinos "aliados" da catedral tornando eminente\n'
                            'uma guerra entre 3 reinos(Catedral, Vinicta e Juna) vs 2(Minic e Blugg)\n'
                            "Sendo considerado até mesmo pelos aliados da catedral uma guerra injusta\n", 0.11)
                        txt("Uma guerra de proporções gigantescas se inicia entre os reinos.\n"
                            "Entretanto, a catedral parece estar evitando usar os seus conhecimentos\n"
                            "mágicos nesta batalha, sendo considerado o reino mais fraco na batalha.\n", 0.11)
                        txt(f'"Mascariane se pergunta:\n'
                            f'Onde está {nome_do_jogador}??!!"', 0.11)
                        txt("Mas você aparece atrás dele, mas não consegue corta-lo.\n"
                            "Mesmo assim, o assustou.", 0.11)
                        txt("Logo começará uma batalha entre os dois, mas Mascariane "
                            "não quer usar a magia.", 0.11)
                        # Combate 1:
                        # inimigo_nome = "Mascariane"
                        # inimigo_atb = [800, 100]
                        # Fazer o código parar no meio da batalha.
                        # Fazer a jogadora achar que está ganhando de Mascariane.
                        txt("Mascariane se vê sem alternativas, e utiliza seus poderes.\n"
                            "Os reis não conseguem ver isso, pois a catedral ficou muito\n"
                            "atrás dos outros.", 0.12)
                        txt("Iniciando combate...", 0.12)
                        # Combate 2:
                        # inimigo_nome = "Mascariane"
                        # inimigo_atb = [2000, 100]
                        # Fazer o código parar no meio da batalha, na quase morte do jogador.
                        txt("Quase sem forças para continuar...\n"
                            "Eis que aparece um mago, aprendiz,"
                            "mas mostrou ser poderoso.\n", 0.12)
                        # Combate Final:
                        # inimigo_nome = "Mascariane"
                        # inimigo_atb = [2000, 100]
                        txt("Após a derrota de Mascariane, todos os magos presentes começaram\n"
                            "a utilizar magia no combate. Porém, as tropas aliadas da catedral\n"
                            "pediram explicação, e com a falta dela começaram a se rebelar e\n"
                            "notar que a catedral havia manipulado eles para defendelos nesta\n"
                            "guerra.", 0.13)
                        txt("Os magos não tiveram chance, pois, além de serem a minoria, não sabiam\n"
                            "usar a magia que Mascariane utilizava.", 0.14)
                        txt("Com isso, a catedral foi lentamente conquistada para devolve-lo ao\n"
                            f"rei por direito, {nome_do_jogador}", 0.13)
                        time.sleep(2)
                        txt("...", 1)
                        txt(f"Após derrotar Mascarine, {nome_do_jogador} consegue recuperar\n"
                            "o reino de seu pai, tornando-se por direito, rei.\n"
                            "Concluindo assim a sua jornada.\n"
                            "Diz estar em dívida com os reinos Minic e Blugg, porém, acreditam\n"
                            "estar em dívida com o príncipe, pois ele os alertou antes que\n"
                            "acontecesse algo maior.", 0.12)
                        txt(f"Anos mais tarde, o mago vem se tornar conselheiro do novo rei({nome_do_jogador})\n"
                            "por se mostrar leal e ter coração puro.", 0.11)


                elif escolhas[3] == 2:
                    print("Voltar aqui!")

            elif escolhas[2] == 2:
                txt("Era uma armadilha de um urso, sim, um urso apareceu e admitiu.", 0.12)
                txt("-Urso:\n"
                    "-Você será o nosso almoço de hoje!", 0.14)
                print("Voltar aqui!")

        elif escolhas[1] == 2:
            txt("Você tenta dialogar, mas acaba sendo sequestado\n"
                "após perceberem que você é o principe.\n", 0.11)
            time.sleep(0.11)

            txt("...", 0.5)

            txt("MATA!\n"
                "MATA!\n"
                "MATA!", 0.2)

            txt(f"MORTE!\n"
                f"{nome_do_jogador}\n"
                "MORTE!\n"
                f"{nome_do_jogador}, acorde!\n", 0.11)

            txt("Uma lâmina está sendo afiada.\n"
                "Mas por estar encapuzado não consegue ver muita coisa!\n", 0.11)

            txt("Uma voz começa a sussurrar na sua cabeça,\n"
                "mas não é nenhum pouco familiar.\n", 0.15)

            txt("Uma voz vem vindo até você dizendo que está na hora.\n", 0.11)

            txt("Mas no momento em que você teria a cabeça decaptada,\n"
                "a flecha(ainda em seu peito) brilha e se transforma\n"
                "em uma serpente, livrando você da morte eminente,\n", 0.11)

            txt("Peguem ele!!", 0.11)
            time.sleep(0.3)
            # Combate:
            # inimigo_nome = "???"
            # inimigo_atb = [100, 100]

            txt("URrrr, você está morto quando Mas..cariane souber que\n"
                "vo..cê es..tá vivo!!"
                "☠", 0.1)

            txt("Agora sem capuz, você percebe que está dentro do antigo\n"
                "reino de seu pai, seu reino por direito!\n", 0.1)

            txt("Logo entra em uma taberna.\n"
                "Lá todos pensam ser só mais um futuro servo.", 0.1)

            escolhas.append(int(input("[1].Pedir informações.\n"
                                      "[2].ir a outro pub.\n"
                                      "Sua escolha: ")))
            # Adicionar verificação depois.

            if escolhas[1] == 1:
                escolhas.append(int(input("[1].Falar com barman.\n"
                                          "[2].Falar com bêbados.\n"
                                          "Sua escolha: ")))
                # Adicionar verificação depois.

                if escolhas[2] == 1:
                    time.sleep(0.15)
                    txt('"Eu poderia contar a eles que você está por aqui.."\n', 0.08)
                    txt('"-O que você quer?"\n'
                        '"-Não tenho dinheiro!"', 0.1)
                    txt('"Relaxa!"\n'
                        '"Aqui você está seguro!"\n'
                        '"Todos que estão aqui não são devotos a igreja!"\n'
                        '"Acreditamos que a igreja.."\n'
                        '"Antes de contar, por que não toma uma bebida?"', 0.1)
                    escolhas.append(int(input("[1].Tomar bebida.\n"
                                              "[2].Não tomar.\n"
                                              "Sua escolha: ")))

                elif escolhas[2] == 2:
                    time.sleep(0.18)
                    txt("Bêbados geralmente não sabem guardar segredo!", 0.1)
                    txt("Os bêbados estão falando sobre um ovo.", 0.1)
                    txt("Estão tão bêbados que nem percebem você alí", 0.12)
                    txt('"-Ele pertencia a uma família de Elfos tempos atrás.\n'
                        'Mas nunca tentaram recupera-lo.. o será que aconteceu?"'
                        '"-Tinh. uma pass.. atr... da igr.. [Desmaiou]"\n', 0.13)
                    escolhas.append(int(input("Escolhas:\n"
                                              "[1].Falar com barman\n"
                                              "[2].Ir embora\n"
                                              "Sua escolha: ")))
                    if escolhas[3] == 1:
                        time.sleep(0.18)
                        txt("O barman está te espeando a um tempo.", 0.13)
                        txt('"Se mascariane estivesse aqui não deixaria um vivo\n'
                            'por estar falando do ovo."\n', 0.13)
                        print('"Escute!!"')
                        time.sleep(0.2)
                        txt('"O ovo é necessário para derrotar Mascariane.\n"'
                            '"Encontre uma Elfa, ela possui a mesma ambição que\n'
                            'a sua de derrotar Mascariane, mas está atrás do ovo."', 0.13)
                        txt('"Ela acabou de sair! Disse que ia para a igreja principal.\n"', 0.15)
                        print("Ao sair pela porta você se depara com duas ruas.")
                        escolhas.append("Escolha:\n"
                                        "[1].OudriKan\n"
                                        "[2].DaLarrai\n"
                                        "Sua escolha: ")
                        if 1 == escolhas[4] == 2:
                            time.sleep(0.18)
                            txt("\nUm Guarda o encontrou!", 0.1)
                            txt("Preparando parao combate!", 0.13)
                            time.sleep(0.2)
                            # Combate:
                            # inimigo_nome = "Soulja Boy - Bispo"
                            # inimigo_atb = [500, 90] # HP # Força
                            txt("Indo em direção a igreja principal você avista uma multidão!", 0.16)
                            txt("Mascariane está lá! Mas é impossível ataca-lo agora.", 0.12)
                            txt("Ele está rodeado por seus dicípulos e padres.", 0.13)
                            txt("Até que 2/3 do povo que o cercavam tentam asassina-lo.", 0.14)
                            time.sleep(0.25)
                            txt("Logo o escoltam para dentro da igreja pelos padres.\n"
                                "Mas o deixam sozinho dentro da igreja\n", 0.13)
                            escolhas.append("Escolhas:\n"
                                            "[1].Ir atrás dele para mata-lo\n"
                                            "[2].Ir ajudar a Elfa.\n"
                                            "Sua escolha: ")
                            if escolhas[5] == 1:
                                time.sleep(0.2)
                                txt("Um bêbado falou tentou falar de algo atrás\n"
                                    "da Igreja", 0.16)
                                escolhas.append(int(input("Escolhas:\n"
                                                          "[1].Ver o que tem atrás da igreja.\n"
                                                          "[2].Tentar ir pela multidão.\n"
                                                          "Sua escolha: ")))
                                if escolhas[6] == 1:  # Final com batalha
                                    time.sleep(0.07)
                                    txt("\nVocê encontra uma passagem escondida!", 0.12)
                                    txt("No corredor você dá de cara com Mascariane!!\n", 0.13)
                                    time.sleep(1.3)
                                    txt("Uma grande batalha está prestes a acontecer!!", 0.13)
                                    # Combate:
                                    # inimigo_nome = "Mascariane"
                                    # inimigo_atb = [2000, 90] # HP # Força
                                    # Quando o personágem do jogador estiver quase perdendo,
                                    # Fazer o código dar break para continuar o texto a baixo.
                                    txt("A parede é quebrada e dela sai a Elfa e, um Yet???!!", 0.21)
                                    txt("Por um acaso vocês 3 agora se únem para derrotar Mascariane.", 0.23)
                                    time.sleep(0.3)
                                    # Combate final!!
                                    # inimigo_nome = "Mascariane"
                                    # inimigo_atb = [2000, 90] # HP # Força
                                    txt("Ao derrotar Mascariane, a catedral começa a sucumbir!\n"
                                        "Porém, alguns acharam importante preservar o lado bom\n"
                                        "da igreja. Preservando assim sua menságem de bomdade e\n"
                                        "acolhimento a qualquer pessoa!\n", 0.17)
                                    txt(f"{nome_do_jogador} conseguiu, recuperou o reino de seu pai,\n"
                                        f"e se tornou o novo rei, renomeando a 'catedral' para seu nome\n"
                                        f"original, Mambla.\n"
                                        f"Deixou que a a idelogia boa da igreja fosse possível ser\n"
                                        f"transmitida, porém, desassociando ela da antiga catedral!\n", 0.14)
                                    txt("Depois da batalha final ele nunca mais viu a Elfa, mas teme suas"
                                        "intençõs agora com o ovo.", 0.16)

                                if escolhas[6] == 2:  # Final RUIM
                                    time.sleep(0.17)
                                    txt("Passando pela multidão você é esfaqueado!", 0.22)
                                    txt("Um triste fim para um guerreiro tão habilidoso.", 0.22)
                                    txt("Morreu sem concluir seu objetivo.", 0.19)
                                    print("É o fim!")
                                    print("Agradescemos por jogar o nosso jogo!")

            elif escolhas[1] == 2:  # Final ruim.
                txt("Ao sair do pub é cercado por padres que são magos", 0.1)
                txt("Sendo capturado novamente, porém, dessa vez sua\n"
                    "execução acaba acontecendo.", 0.1)

    elif escolhas[0] == 2:
        txt("Indo em direção a Blugg, você encontra ógros perambulando\n"
            "pela estrada, mas por algum motivo eles são inofensíveis.\n"
            "O clima é calmo, aconchegante.", 0.1)
        txt("Chegando em Blugg, é acolhido pelos guardas e levado até o\n"
            "rei(Bluff) filho de Gluff que é filho de Tlugg que é filho\n"
            "de Blugg", 0.1)
        txt("Eles não falam a nossa língua, então pedem para que você\n"
            "desenhe sua intenção alí.", 0.1)
        txt("Mesmo por desenho eles entenderam o sentido. Desenharam uma\n"
            "caixa com um gato dentro com a Igreja sendo uma igualdade.", 0.1)
        txt("Aparentam já estarem desconfiando da igreja a bastante tempo.", 0.1)
        escolhas.append(int(input("Escolhas:\n"
                                  "[1].Contar a eles sobre o que aconteceu\n"
                                  "[2].Falar que suspeita que a igreja está\n"
                                  "envolvida com um poder obscuro.\n"
                                  "Sua escolha: ")))
        if escolhas[1] == 1:
            txt("Pelos desenhos parece que eles já sabiam disso.", 0.1)
            txt("Aparentemente querem além da sa ajuda na guerra, mas também\n"
                "em tentar convencer o rei de Minic(Julius) a ficar do nosso\n"
                "lado.", 0.1)
            txt(f"Deve ser por Julius ser o melhor amigo de seu pai, tornando\n"
                "sua palavra mais amigável.", 0.1)
            escolhas.append(int(input("Escolhas:\n"
                                      "[1].Aceitar.\n"
                                      "[2].Não aceitar.\n"
                                      "Sua escolha: ")))
            if escolhas[2] == 1:
                txt("Você vai ao reino de Minic para falar com Julius.", 0.12)
                txt("Ao falar o que a igreja fez com o reino de seu pai, ele\n"
                    "declara guerra contra a catedral.", 0.1)
                txt("Então os reinos Blug e Minic agora estão juntos para atacar a catedral,\n"
                    "porém, de alguma forma a informação vazou. A catedral ficou sabendo do\n"
                    "plano de guerra e logo providenciou um mago para tentar silenciar os\n"
                    "dois reinos.", 0.1)
                time.sleep(0.13)
                txt("O problema é que ele nunca mais foi visto!", 0.12)
                time.sleep(0.5)
                txt("Percebendo isso a catedral convoca os reinos manipulados por eles para\n"
                    "tentar fazer Minic e Blug serem os vilõs da história.", 0.1)
                txt("Entretanto, acharam estranho a guerra, pois Minic e blug sempre foram\n"
                    "amigáveis. Então não vão arriscar seu laços de amizade para proteger a\n"
                    "catedral.", 0.1)
                time.sleep(0.4)
                txt("A catedral agora está sozinha!", 0.1)
                txt("Ao ver isso, terão que utilizar magia na guerra.", 0.1)
                time.sleep(0.3)
                txt("Voltando a reino Blug...", 0.14)
                txt("Você deve escolher qual estratégia você usará.", 0.12)
                txt("Já estão partindo para o campo de batalha.", 0.12)

            elif escolhas[2] == 2:
                print("Voltar aqui!")

        elif escolhas[1] == 2:
            print("Voltar aqui!")

elif class_e_atributos[0] == "Elfo":
    print("H1")

elif class_e_atributos[0] == "Mago":
    print("H2")