# by Jefferson.
####################
import time, random

####################

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


##################################
# Verificação
def ver(opcao, opcoes_escolhas):
    escolha = [opcao]
    opcoes = [*opcoes_escolhas]
    while escolha[-1].isnumeric() is not True or escolha[-1].isnumeric():
        try:
            if int(escolha[-1]):
                if escolha[-1] in opcoes:
                    c = int(escolha[-1])
                    escolha.pop()
                    escolha = c
                    break

                if int(escolha[-1]) <= 0:
                    escolha[-1] += 2

                else:
                    escolha[-1] += 2

        except ValueError:
            escolha.pop()
            print("Escolha uma opção válida!")
            escolha.append(input("Sua escolha: "))

        except TypeError:
            escolha.pop()
            print("Escolha uma opção válida!")
            escolha.append(input("Sua escolha: "))

    return escolha


## DADO.
def dado():
    x = random.randint(1, 6)
    return x


'''numero = 0
for i in range(1):
    numero = dado()
    print(numero)'''


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
    Elírio entrou em choque, sabia o que era e não era do Bispo de modo algum... Sua avó
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
    ["Guerreiro", [100, 110, 90], ["Soco Dinâmico", "Corte Vertical", "Espada secreta", "Espada Sagrada"]],
    ["Elfo", [110, 90, 100], ["Flecha rápida", "Flecha explosiva", "Flecha da Fé", "Chuva de flechas"]],
    ["Mago", [90, 100, 110], ["Feitiço", "Sabor Veneno", "Bola sombria", "Onda infernal"]],
]

dinheiro = 0
itens = []
escolhas = []
'''print(f"""
{'-' * 60}
{'Bem-vindo(a) ao [Nome do jogo]'.center(60)}

{'Selecione uma classe para começar a jornada.':^60}
{"[1]":^20} {"[2]":^20} {"[3]":^20}
{personagens[0][0]:^20} {personagens[1][0]:^20} {personagens[2][0]:^20}
{'-' * 60}""")'''

class_e_atributos = [ver(input("Sua escolha: "), ["1", "2", "3"])]

class_e_atributos = [i for i in personagens if personagens.index(i) == class_e_atributos[0] - 1]
class_e_atributos = [v for v in class_e_atributos[0]]

nome_do_jogador = input(f"Nos diga o seu nome/nick, ó grande {class_e_atributos[0]}: ")

if class_e_atributos[0] == "Guerreiro":
    # txt(guerreiro_historia)
    txt(f"""
    Você sabe que sozinho não consegue vingar sua famíla,
então decide ir a Minic, onde o rei era o melhor amigo de
seu pai.
""", 0.06)
    escolhas.append(ver(input("""Reinos:
        [1]. Minic
        [2]. Blugg
Sua escolha: """), ["1", "2"]))
    # Adicionar verificação de erro.

    if escolhas[0] == 1:
        txt("\nÀ caminho de Minic, você encontra saqueadores. Eles ainda não\n"
            "o viram, mas deve decidir se deverá desviar(demorando mais) ou\n"
            "atacar antes que eles te vejam", 0.04)

        escolhas.append(ver(input("Escolhas:\n"
                                  "[1].Desviar caminho.\n"
                                  "[2].Conversar.\n"
                                  "[3].Batalhar.\n"
                                  "Sua escolha: "), ["1", "2", "3"]))
        # Adicionar verificação de erro à escolha.
        if escolhas[1] == 1:
            txt("\nDesviando o caminho você encontra um ansião antes do reino.\n", 0.08)
            txt("Ele te alerta sobre os perigos eminentes daquela floresta!\n"
                "Nela há ógros, ursos e lobos terríveis.\n", 0.08)
            txt("Seguinto em frente você encontra um buraco", 0.08)
            escolhas.append(ver(input("Escolhas:"
                                      "[1].Seguir em frente.\n"
                                      "[2].Analisar o buraco.\n"
                                      "Sua escolha: "), ["1", "2"]))
            if escolhas[2] == 1:
                txt("\nSeguindo em frente um bando de lobos o esperava, era"
                    "estranho, todos do bando agiam como um só alí.\n", 0.14)
                txt("Prepare-se, uma batalha está para começar!!", 0.1)
                time.sleep(0.2)
                # Combate:
                # inimigo_nome = "Lobos"
                # inimigo_atb = [400, 90] # HP # Força
                # Luta normal com o código.
                txt("A noite está chegando e você está exausto.", 0.08)
                escolhas.append(ver(input("Escolhas:\n"
                                          "[1].Ascender uma fogueira e descansar.\n"
                                          "[2].Continuar para não encontrar monstros.\n"
                                          "Sua escolha: "), ["1", "2"]))
                if escolhas[3] == 1:
                    txt("No dia seguinte, segue viágem para o reino.", 0.07)
                    txt("Chegando lá, é muito bem recebido pela realeza, pois\n"
                        "seu pai era amigo do rei Julius.", 0.06)
                    txt('O rei o pergunta, "o que trás o jovem príncipe ao meu humilde reino?"', 0.1)
                    escolhas.append(ver(input("Escolhas:\n"
                                              "[1].Contar o que aconteceu com o reino e seu pai.\n"
                                              "[2].Não contar, mas, tentar converte-lo a ficar\n"
                                              "contra a catedral.\n"
                                              "Sua escolha: "), ["1", "2"]))
                    # Adicionar verificação de erro.
                    if 1 == escolhas[4] == 2:  # Final bom
                        if escolhas[4] == 2:
                            txt("O rei não vê necessidade em entra em guerra contra a catedral.\n"
                                "Porém, tenta entrar em contato com o seu pai, descobrindo que\n"
                                "ele está morto. Te forçando a contar o que aconteceu.", 0.5)
                        elif escolhas[4] == 1:
                            txt(f"Por ser amigo da família de {nome_do_jogador}, o rei acredita\n"
                                f"sem pestanejar", 0.06)
                        txt("Fica horrorizado com o que a igreja foi capaz de fazer nas sombras.", 0.06)
                        txt(f'O rei diz a {nome_do_jogador} que sozinhos não serão capazes de\n'
                            'derrotar a igreja pelo tamanho descrito por você.', 0.1)
                        txt("Então terão que convencer outros reinos que a igreja\n"
                            "não é o que aparenta.", 0.1)
                        txt("Além de terem que bolar uma estratégia!\n", 0.1)
                        time.sleep(0.3)
                        txt("Aproximadamente 2 anos mais tarde..", 0.05)
                        time.sleep(0.2)
                        txt("Apenas conseguiram fazer o reino Blugg aliar-se a eles para derrubar a\n"
                            "igreja. Mesmo falando outra lingua, se comunicavam com desenhos.", 0.07)
                        txt("Mesmo sendo misteriosa, mostrou ser muito poderosa em combate,\n"
                            "pois por teram sua própria lingua, tornam suas técnicas exclusividade\n"
                            "do povo local", 0.07)
                        time.sleep(1.2)
                        txt("\nRei Julius:\n"
                            "-Estão todos prontos?!\n"
                            "Tropas:\n"
                            "-Siim!!\n"
                            "-̪ɐ̃s̪kr̩t̪ɐm\n", 0.06)
                        txt(f"{nome_do_jogador}:\n"
                            f"-AVANTE!!\n", 0.06)
                        time.sleep(0.4)
                        txt("À caminho da capital.\n"
                            "Mascarine já estava ciente da guerra eminente.\n"
                            'Então reuniu todos os reinos "aliados" da catedral tornando eminente\n'
                            'uma guerra entre 3 reinos(Catedral, Vinicta e Juna) vs 2(Minic e Blugg)\n'
                            "Sendo considerado até mesmo pelos aliados da catedral uma guerra injusta\n", 0.06)
                        txt("Uma guerra de proporções gigantescas se inicia entre os reinos.\n"
                            "Entretanto, a catedral parece estar evitando usar os seus conhecimentos\n"
                            "mágicos nesta batalha, sendo considerado o reino mais fraco na batalha.\n", 0.06)
                        txt(f'"Mascariane se pergunta:\n'
                            f'Onde está {nome_do_jogador}??!!"', 0.06)
                        txt("Mas você aparece atrás dele, mas não consegue corta-lo.\n"
                            "Mesmo assim, o assustou.", 0.06)
                        txt("Logo começará uma batalha entre os dois, mas Mascariane "
                            "não quer usar a magia.", 0.06)
                        # Combate 1:
                        # inimigo_nome = "Mascariane"
                        # inimigo_atb = [800, 100]
                        # Fazer o código parar no meio da batalha.
                        # Fazer a jogadora achar que está ganhando de Mascariane.
                        txt("Mascariane se vê sem alternativas, e utiliza seus poderes.\n"
                            "Os reis não conseguem ver isso, pois a catedral ficou muito\n"
                            "atrás dos outros.", 0.07)
                        txt("Iniciando combate...", 0.07)
                        # Combate 2:
                        # inimigo_nome = "Mascariane"
                        # inimigo_atb = [2000, 100]
                        # Fazer o código parar no meio da batalha, na quase morte do jogador.
                        txt("Quase sem forças para continuar...\n"
                            "Eis que aparece um mago, aprendiz,"
                            "mas mostrou ser poderoso.\n", 0.07)
                        # Combate Final:
                        # inimigo_nome = "Mascariane"
                        # inimigo_atb = [2000, 100]
                        txt("Após a derrota de Mascariane, todos os magos presentes começaram\n"
                            "a utilizar magia no combate. Porém, as tropas aliadas da catedral\n"
                            "pediram explicação, e com a falta dela começaram a se rebelar e\n"
                            "notar que a catedral havia manipulado eles para defendelos nesta\n"
                            "guerra.", 0.07)
                        txt("Os magos não tiveram chance, pois, além de serem a minoria, não sabiam\n"
                            "usar a magia que Mascariane utilizava.", 0.14)
                        txt("Com isso, a catedral foi lentamente conquistada para devolve-lo ao\n"
                            f"rei por direito, {nome_do_jogador}", 0.07)
                        time.sleep(2)
                        txt("...", 1)
                        txt(f"Após derrotar Mascarine, {nome_do_jogador} consegue recuperar\n"
                            "o reino de seu pai, tornando-se por direito, rei.\n"
                            "Concluindo assim a sua jornada.\n"
                            "Diz estar em dívida com os reinos Minic e Blugg, porém, acreditam\n"
                            "estar em dívida com o príncipe, pois ele os alertou antes que\n"
                            "acontecesse algo maior.", 0.07)
                        txt(f"Anos mais tarde, o mago vem se tornar conselheiro do novo rei({nome_do_jogador})\n"
                            "por se mostrar leal e ter coração puro.", 0.06)


                elif escolhas[3] == 2:
                    txt("\nVários olhos te observam na caminhada até Minic. Estão todos imóveis,\n"
                        "aparentemente inofensivos.", 0.08)
                    txt("Até que um lobisomem aparece e parece estar com fome.", 0.08)
                    txt("Você terá que mata-lo!", 0.08)
                    # Batalha:
                    # Nome: Lobisomem
                    # ATB: [700, 60]

                    txt("Ao matar ele você recebe um ítem. 'Presa sedenta' contendo um líquido.", 0.08)
                    escolhas.append(ver(input("Escolhas:\n"
                                              "[1].Tomar líquido.\n"
                                              "[2].Não tomar, mas guardar.\n"
                                              "Sua escolha: "), ["1", "2"]))
                    if escolhas[4] == 1:
                        class_e_atributos[1][0] += 100
                        class_e_atributos[1][1] += 100

                    elif escolhas[4] == 2:
                        itens.append("Presa Sedenta")

            elif escolhas[2] == 2:
                txt("\nEra uma armadilha de um urso, sim, um urso apareceu e admitiu isso.", 0.07)
                txt("-Urso:\n"
                    "-Você será o nosso almoço de hoje!", 0.14)
            print("Voltar aqui!")

        elif escolhas[1] == 2:
            txt("Você tenta dialogar, mas acaba sendo sequestado\n"
                "após perceberem que você é o principe.\n", 0.08)
            time.sleep(0.06)

            txt("...", 0.5)

            txt("MATA!\n"
                "MATA!\n"
                "MATA!", 0.2)

            txt(f"MORTE!\n"
                f"{nome_do_jogador}\n"
                "MORTE!\n"
                f"{nome_do_jogador}, acorde!\n", 0.08)

            txt("Uma lâmina está sendo afiada.\n"
                "Mas por estar encapuzado não consegue ver muita coisa!\n", 0.06)

            txt("Uma voz começa a sussurrar na sua cabeça,\n"
                "mas não é nenhum pouco familiar.\n", 0.1)

            txt("Uma voz vem vindo até você dizendo que está na hora.\n", 0.06)

            txt("Mas no momento em que você teria a cabeça decaptada,\n"
                "a flecha(ainda em seu peito) brilha e se transforma\n"
                "em uma serpente, livrando você da morte eminente,\n", 0.06)

            txt("Peguem ele!!", 0.06)
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

            escolhas.append(ver(input("Escolhas: \n"
                                      "[1].Pedir informações.\n"
                                      "[2].ir a outro pub.\n"
                                      "Sua escolha: "), ["1", "2"]))
            # Adicionar verificação depois.

            if escolhas[1] == 1:
                escolhas.append(ver(input("Escolhas: \n"
                                          "[1].Falar com barman.\n"
                                          "[2].Falar com bêbados.\n"
                                          "Sua escolha: "), ["1", "2"]))
                # Adicionar verificação depois.

                if escolhas[2] == 1:
                    time.sleep(0.2)
                    txt('"\nEu poderia contar a eles que você está por aqui.."\n', 0.08)
                    txt('"-O que você quer?"\n'
                        '"-Não tenho dinheiro!"', 0.1)
                    txt('"Relaxa!"\n'
                        '"Aqui você está seguro!"\n'
                        '"Todos que estão aqui não são devotos a igreja!"\n'
                        '"Acreditamos que a igreja.."\n'
                        '"Antes de contar, por que não toma uma bebida?"', 0.1)
                    escolhas.append(ver(input("[1].Tomar bebida.\n"
                                              "[2].Não tomar.\n"
                                              "Sua escolha: "), ["1", "2"]))

                elif escolhas[2] == 2:
                    time.sleep(0.18)
                    txt("\nBêbados geralmente não sabem guardar segredo!", 0.1)
                    txt("Os bêbados estão falando sobre um ovo.", 0.1)
                    txt("Estão tão bêbados que nem percebem você alí", 0.07)
                    txt('"-Ele pertencia a uma família de Elfos tempos atrás.\n'
                        'Mas nunca tentaram recupera-lo.. o será que aconteceu?"'
                        '"-Tinh. uma pass.. atr... da igr.. [Desmaiou]"\n', 0.07)
                    escolhas.append(ver(input("Escolhas:\n"
                                              "[1].Falar com barman\n"
                                              "[2].Ir embora\n"
                                              "Sua escolha: "), ["1", "2"]))
                    if escolhas[3] == 1:
                        time.sleep(0.18)
                        txt("\nO barman está te espeando a um tempo.", 0.07)
                        txt('"Se mascariane estivesse aqui não deixaria um vivo\n'
                            'por estar falando do ovo."\n', 0.07)
                        print('"Escute!!"')
                        time.sleep(0.2)
                        txt('"O ovo é necessário para derrotar Mascariane.\n"'
                            '"Encontre uma Elfa, ela possui a mesma ambição que\n'
                            'a sua de derrotar Mascariane, mas está atrás do ovo."', 0.07)
                        txt('"Ela acabou de sair! Disse que ia para a igreja principal.\n"', 0.08)
                        print("Ao sair pela porta você se depara com duas ruas.")
                        escolhas.append(ver(input("Escolha:\n"
                                                  "[1].OudriKan\n"
                                                  "[2].DaLarrai\n"
                                                  "Sua escolha: "), ["1", "2"]))
                        if 1 == escolhas[4] == 2:
                            time.sleep(0.18)
                            txt("\nUm Guarda o encontrou!", 0.1)
                            txt("Preparando parao combate!", 0.07)
                            time.sleep(0.2)
                            # Combate:
                            # inimigo_nome = "Soulja Boy - Bispo"
                            # inimigo_atb = [500, 90] # HP # Força
                            txt("Indo em direção a igreja principal você avista uma multidão!", 0.11)
                            txt("Mascariane está lá! Mas é impossível ataca-lo agora.", 0.07)
                            txt("Ele está rodeado por seus dicípulos e padres.", 0.07)
                            txt("Até que 2/3 do povo que o cercavam tentam asassina-lo.", 0.14)
                            time.sleep(0.25)
                            txt("Logo o escoltam para dentro da igreja pelos padres.\n"
                                "Mas o deixam sozinho dentro da igreja\n", 0.07)
                            escolhas.append(ver(input("Escolhas:\n"
                                                      "[1].Ir atrás dele para mata-lo\n"
                                                      "[2].Ir ajudar a Elfa.\n"
                                                      "Sua escolha: "), ["1", "2"]))
                            if escolhas[5] == 1:
                                time.sleep(0.2)
                                txt("\nUm bêbado falou tentou falar de algo atrás\n"
                                    "da Igreja", 0.08)
                                escolhas.append(ver(input("Escolhas:\n"
                                                          "[1].Ver o que tem atrás da igreja.\n"
                                                          "[2].Tentar ir pela multidão.\n"
                                                          "Sua escolha: "), ["1", "2"]))
                                if escolhas[6] == 1:  # Final com batalha
                                    time.sleep(0.07)
                                    txt("\nVocê encontra uma passagem escondida!", 0.07)
                                    txt("No corredor você dá de cara com Mascariane!!\n", 0.07)
                                    time.sleep(1.3)
                                    txt("Uma grande batalha está prestes a acontecer!!", 0.07)
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
                                        "intençõs agora com o YETI.", 0.08)

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
        escolhas.append(ver(input("Escolhas:\n"
                                  "[1].Contar a eles sobre o que aconteceu\n"
                                  "[2].Falar que suspeita que a igreja está\n"
                                  "envolvida com um poder obscuro.\n"
                                  "Sua escolha: "), ["1", "2"]))
        if escolhas[1] == 1:
            txt("\nPelos desenhos parece que eles já sabiam disso.", 0.1)
            txt("Aparentemente querem além da sa ajuda na guerra, mas também\n"
                "em tentar convencer o rei de Minic(Julius) a ficar do nosso\n"
                "lado.", 0.1)
            txt(f"Deve ser por Julius ser o melhor amigo de seu pai, tornando\n"
                "sua palavra mais amigável.", 0.1)
            escolhas.append(ver(input("Escolhas:\n"
                                      "[1].Aceitar.\n"
                                      "[2].Não aceitar.\n"
                                      "Sua escolha: "), ["1", "2"]))
            if escolhas[2] == 1:
                txt("\nVocê vai ao reino de Minic para falar com Julius.", 0.07)
                txt("Ao falar o que a igreja fez com o reino de seu pai, ele\n"
                    "declara guerra contra a catedral.", 0.1)
                txt("Então os reinos Blug e Minic agora estão juntos para atacar a catedral,\n"
                    "porém, de alguma forma a informação vazou. A catedral ficou sabendo do\n"
                    "plano de guerra e logo providenciou um mago para tentar silenciar os\n"
                    "dois reinos.", 0.1)
                time.sleep(0.2)
                txt("O problema é que ele nunca mais foi visto!", 0.07)
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
                txt("Você deve escolher qual estratégia você usará.", 0.07)
                txt("Já estão partindo para o campo de batalha.", 0.07)

            elif escolhas[2] == 2:
                print("Voltar aqui!")

        elif escolhas[1] == 2:
            print("Voltar aqui!")

elif class_e_atributos[0] == "Elfo":
    # txt(elfa_historia, 0.06)
    escolhas.append(ver(input("Escolhas:\n"
                              "[1].Falar com a mãe sobre o ovo perdido.\n"
                              "[2].Ir atrás de mais informações.\n"
                              "Sua escolha: "), ["1", "2"]))

    if escolhas[0] == 1:
        print("Voltar aqui!")

    elif escolhas[0] == 2:
        txt(f"\nSaindo de Trozar, {nome_do_jogador} parte em busca de sua aventura!\n", 0.1)
        txt(f"Para descobrir mais sobre o que foi roubado, será necessário conversar com os guardas,\n"
            "por sorte um deles já foi da família, mas continua sendo da família.\n", 0.07)
        txt("Porém, Mascariane talvez mascariane te remunere se conseguir recupera-lo para ele", 0.08)
        time.sleep(0.4)
        escolhas.append(ver(input("Escolhas:\n"
                                  "[1].Falar com antigo familiar\n"
                                  "[2].Falar com Mascariane.\n"
                                  "Sua escolha: "), ["1", "2"]))
        if escolhas[1] == 1:
            txt("\nDentro da capital, só existe um local para ele estar.\n"
                "O bar S, o único bar liberal da catedral, bar esse não conhecido por Mascariane.", 0.06)
            time.sleep(0.3)
            txt("Lá está ele!! Tomando uma breja gelada daquelas.", 0.04)
            txt("Bébado ele diz:"
                "-'Minha garota. O que lhe traz aqui?'", 0.08)
            escolhas.append(ver(input("Escolhas:\n"
                                      "[1].Perguntar sobre ítem roubado.\n"
                                      "[2].Falar sobre família.\n"
                                      "Sua escolha: "), ["1", "2"]))
            time.sleep(0.2)
            if escolhas[2] == 1:
                txt("\n-'Ítem? Que ítem? Aaaa, você está falando, Burp!.., do ovo'", 0.07)
                txt("OVO??", 0.1)
                txt("[Ele apénas sorri e se deita.]", 0.1)
                time.sleep(0.3)
                txt("-'Eu não deveria ter te contado isso, mas agora já era.'", 0.06)
                txt("-'O ovo é uma erança de sua família, tempos atrás eu cudava dele, até que..'", 0.08)
                time.sleep(0.2)
                txt("ATÉ QUE O QUE?!", 0.2)
                txt("-'Até que o chefia chegou de ameaçou matar a todos se não entregassem sua última\n"
                    "erança, que era o OVO, ainda não sabemos o que o ovo vai gerar, mas é algo diferente'\n", 0.08)
                txt("-'Não posso mais falar nada sobre, senão serei morto.'", 0.08)
                time.sleep(0.2)
                txt("O barman está te chamando!", 0.08)
                escolhas.append(ver(input("Escolhas:\n"
                                          "[1].Falar com Barman.\n"
                                          "[2].Ir embora.\n"
                                          "Sua escolha: "), ["1", "2"]))
                time.sleep(0.3)
                if escolhas[3] == 1:
                    txt("\n-Shhhhh..", 0.2)
                    txt("-'Você está em búsca do que foi roubado? Eu ouvi dizer que eles foram para\n"
                        "o reino Vinicta'", 0.09)
                    txt("Por que você está me ajudando?", 0.09)
                    txt("-'Digamos que eu tenho uma dívida com os Elfos. [Mostra uma perna de pau]'", 0.06)
                    escolhas.append(ver(input("Escolhas:\n"
                                              "[1].Confiar e ir para Vinicta\n"
                                              "[2].Perguntar sobre a história da perna\n"
                                              "Sua escolha: "), ["1", "2"]))
                    if escolhas[4] == 1:
                        txt("\n-'Antes de ir, tome isso!'\n"
                            "-'O colar da sua avó, ela me pediu para entregar à você, mas nunca a ví antes deste dia.\n"
                            "Eu não sei se é mágico ou é apénas um colar normal, mas ele agora é seu!!'\n", 0.08)
                        # Adicionar Colar
                        txt("Muito Obrigado!!", 0.06)

                    elif escolhas[4] == 2:
                        txt("-'Digamos que eu era apénas ideialista. Antigamente eu fazia espadas para as tropas do reino,\n"
                            "até que um dia Mascariane me pede uma mão humana de verdade. Para tentar conseguir a mão eu\n"
                            "conversei com sua avó, que antigamente era uma bruxa do reino. A mão não importava mais, eu dei\n"
                            "um jeito.\n"
                            "Foi amor a primeira vista, ela era tão linda.. Tempos depois nós namoramos,", 0.06)
                        time.sleep(0.2)
                        txt("[Suspiro]", 0.05)
                        time.sleep(0.4)
                        txt("mas Mascariane não concordou com isso, ele odiava quando eu estava perto dela, então, revolveu\n"
                            "me afastar, me jogar aos menos afortunados, mas sua avó me ajudou a fugir, só que na fuga acabei\n"
                            "com a perna dessecada. Me colocou aqui onde estou até hoje. Devo minha vida a ela.\n", 0.06)
                        txt("Agora vá, você deve ir! Siga seu destino!", 0.06)

                        time.sleep(0.3)

                    txt(f"[Indo em direção de Vinicta. {nome_do_jogador} se depara com um chupa cabra.]", 0.08)
                    # Batalha:
                    # Nome: Chupa Cabra
                    # Atributos: [500, 60, 100]
                    dinheiro += 100
                    txt("Chegando lá, é recebido(a) muito bem por ser de uma família bem falada.", 0.06)
                    escolhas.append(ver(input("Escolhas:\n"
                                              "[1].Buscar pelo ítem.\n"
                                              "[2].Falar com o rei sobre.\n"
                                              "Sua escolha: "), ["1", "2"]))
                    if escolhas[5] == 1:
                        escolhas.append(ver(input("\nEscolhas:\n"
                                                  "[1].Pedir informações a alguém.\n"
                                                  "[2].Ir para bares coletar informações.\n"
                                                  "Sua escolha: "), ["1", "2"]))
                        time.sleep(0.3)
                        if escolhas[6] == 1:
                            txt("\nNinguém parece querer te ajudar quanto a isso!", 0.08)
                            txt("Além de estarem começando a desconfiar de você.", 0.08)
                            txt("Perto de um lago tem um velho que todos dizem ser maluco", 0.08)
                            escolhas.append(ver(input("Escolhas:\n"
                                                      "[1].Falar com o velho.\n"
                                                      "[2].Ignorar.\n"
                                                      "Sua escolha: "), ["1", "2"]))
                            time.sleep(0.4)
                            if escolhas[7] == 1:
                                txt("\nO velho fica feliz por alguém estar indo falar com ele.\n"
                                    "Ao perguntar sobre o ítem perdido ele diz que sabe aonde está, mas antes preciso almoçar né..", 0.08)
                                # Descontar das moedas quando tiver.
                                txt("Ao pagar o almoço ele começa a falar sobre a localização.", 0.08)
                                txt("-'Estão de baixo da ponte daquele lago, estão tentando cortar ele.'", 0.08)
                                txt("Chegando lá você se depara com 3 pessoas com capuz, mas uma está com uma tatuágem da igreja.", 0.08)
                                time.sleep(0.4)
                                txt("Uma batalha para recuperar o ovo se inicia.", 0.08)
                                # Batalha:
                                # Nome do inimigo: Trio cabeça de prego
                                # Atributos: [700, 70, 100]
                                dinheiro += 100
                                time.sleep(0.4)
                                txt("\nVocê conseguiu recuperar o OVO, mas quando foi tocalo, você vê todo o passado de sofrimento dele.", 0.08)
                                txt("Mascariane estava lá, fazendo todo tipo de experimento, até mesmo envolvendo inocentes. Um horror\n"
                                    "Cada segundo naquela lembrança parecia o inferno.", 0.08)
                                time.sleep(0.4)
                                txt("Mascariane agora é uma ameaça, ameaça essa que não pode ser deixada de lado! Alguém tem que agir.", 0.08)
                                time.sleep(0.4)
                                txt("Voltando ao seu reino você mostra o ovo a sua mãe, ela não faz idéia do que é aquilo, então você explica", 0.08)
                                txt("Sua mãe não acredita no que Mascariane fez, acha que está mentindo, nem precebeu o colar.", 0.08)
                                txt("-'Não existe esse negócio de visão, você deve ter comido algum cogumelo de zangle'", 0.08)
                                txt("Desapontado você está sozinho nesta jornada, então decide treinar para deter Mascariane", 0.08)
                                txt("Existe uma floresta não muito conhecida em que lá habitam criaturas fortes, é um ótimo lugar para treinar.", 0.08)
                                escolhas.append(ver(input("Escolhas:\n"
                                                          "[1].Treinar para rivalizar com Mascariane.\n"
                                                          "[2].Ir direto a Mascariane.\n"
                                                          "Sua escolha: "), ["1", "2"]))
                                time.sleep(0.08)
                                while escolhas[-1] == 2:
                                    txt("\nPéssima escolha! Você morreu na primeira tentativa.", 0.08)
                                    escolhas.pop()
                                    escolhas.append(ver(input("Escolhas:\n"
                                                              "[1].Treinar para rivalizar com Mascariane.\n"
                                                              "[2].Ir direto a Mascariane.\n"
                                                              "Sua escolha: "), ["1", "2"]))

                                if escolhas[8] == 1:
                                    class_e_atributos[0] += 100
                                    class_e_atributos[1] += 100
                                    class_e_atributos[2] += 100
                                    txt("\nPassou-se 2 anos...", 0.1)
                                    time.sleep(0.4)
                                    txt("Seus atributos melhoraram bastante.", 0.08)
                                    print(f"Vida: {class_e_atributos[0]}\n"
                                          f"Força: {class_e_atributos[1]}\n"
                                          f"Mana: {class_e_atributos[2]}\n")
                                    txt("Chegou a hora de livar o mundo de Mascariane.", 0.08)
                                    txt("Junto com o colar de sua avó e sua erança, o ovo, você parte para a jornada final.", 0.08)
                                    txt("Chegando lá vários guardas estão guardando o portão da igreja onde Mascariane está.", 0.08)
                                    txt("Entrando pelo telhado você dá de cara com Mascariane. Que finge simpatia, mas você sabe quem ele realmente é.", 0.08)
                                    txt("Uma batalha extrema está prestes a começar.", 0.08)
                                    # Batalha Final:
                                    # Nome: Mascariane
                                    # ATB: [70, 1000, 150]
                                    txt("Com Mascariane derrotado, você livrou sua família do trabalho miserável dele e se tornou o novo rei da catedral!", 0.08)
                                    txt("Podendo dar uma vida melhor para a sua família e acabar com a desgraça que a catedral fazia com os outros.", 0.08)
                                    txt("\nGoverne bem, seja melhor do que mascariane foi!", 0.08)
                                    time.sleep(0.4)
                                    txt("Sua avó ficaria orgulhosa!", 0.1)

                            elif escolhas[7] == 2:
                                txt("\n Ao entrar em uma rua é surpreendido por 3 pessoas encapuzadas, com um tendo uma tatuágem de cruz.", 0.08)
                                txt("Uma batalha se inicia.", 0.08)
                                # Batalha
                                # Nome: Os cabeça de prego
                                # Atbt: [600, 50, 100]
                                dinheiro += 100
                                time.sleep(0.3)
                                txt("Um deles tinha uma carta com uma localização, e por incrível que pareça era do ovo.", 0.08)
                                txt("Você vai até a localização mas o ovo não está mais lá, apénas marcas de cinzas no chão", 0.08)
                                txt("Deixaram um pergaminho para tráz, nele dizia:", 0.08)
                                print(f"{'-' * 40}\n"
                                      f"{'Continuaremos com os esperimentos agora.':^40}\n"
                                      f"{'Sigam o protocolo.':^40}\n"
                                      "Pela igreja!\n"
                                      f"{'Ass. Mascariane':>40}\n"
                                      f"{'-' * 40}")

                                time.sleep(0.6)
                                txt("Enfurecido, você vai direto mara a Catedral", 0.08)
                                time.sleep(0.1)
                                txt("Um guerreiro estava lá, mas conversando o guerreiro revela que também está atráz de Mascariane, só que para matalo.", 0.08)
                                txt("Sem exitar você se junta a ele na jornada até que uma mulher grávida fala sobre experimentos dentro de uma masmorra.", 0.08)
                                escolhas.append(ver(input("Escolhas:\n"
                                                          "[1].Ir para Masmorra\n"
                                                          "[2].Continuar com Guerreiro.\n"
                                                          "Sua Escolha: "), ["1", "2"]))
                                time.sleep(0.3)
                                if escolhas[8] == 1:
                                    txt("\nEra uma pessagem atrás da igreja, bem escondida!", 0.08)
                                    txt("Entrando lá, várias pessoas estavam enjauladas, várias multiladas, órgãos estavam jogados sobre uma mesa.\n"
                                        "Aparentemante não havia ninguém alí, mas descendo mais 4 magos são avistados, e..", 0.08)
                                    txt("Lá está! O ovo, dentro de algo com.. água?!", 0.08)
                                    escolhas.append(ver(input("Escolhas:\n"
                                                              "[1].Lutar de frente.\n"
                                                              "[2].Esperar todos irem embora.\n"
                                                              "Sua escolha: "), ["1", "2"]))
                                    if escolhas[9] == 1:
                                        txt("\nUma batalha está prestes a começar!!", 0.08)
                                        time.sleep(0.2)
                                        # Batalha
                                        # Nome: Os blenk
                                        # Atb: [900, 70]
                                        dinheiro += 100

                                    elif escolhas[9] == 2:
                                        txt("Parece que eles já iriam saír.", 0.08)
                                        txt("Ao tocar no ovo, você recebe um choque, várias visões de tortura, seria os experimentos que fizeram com o ovo?!", 0.08)
                                        txt("Indo embora o ovo começa a chocar!!?", 0.08)
                                        time.sleep(0.2)
                                        txt("Um YETI?!", 0.08)
                                        txt("Ele parece achar que você é a mamãe dele.", 0.08)
                                        escolhas.append(ver(input("Escolhas:\n"
                                                                  "[1].Subir em cima dele.\n"
                                                                  "[2].Não subir em cima.\n"
                                                                  "Sua escolha: "), ["1", "2"]))
                                        if escolhas[10] == 1:
                                            txt("\nApós isso ele quebra a parece ao seu lado.", 0.08)
                                            txt("Lá estão Mascariane e o Guerreiro se matando, com a quebra da parede foi uma obrigação intervir no combate,\n"
                                                "se aliando ao lado do guerreiro.", 0.08)

                                        elif escolhas[10] == 2:
                                            txt("Do nada ele quebra a parede!", 0.08)
                                            txt("Lá estão Mascariane e o Guerreiro se matando, com a quebra da parede foi uma obrigação intervir no combate, \n"
                                                "se aliando ao lado do guerreiro.", 0.08)

                                        # Batalha final
                                        # Nome: Mascariane
                                        # Atributos: [2000, 90]
                                        dinheiro += 100
                                        txt("Após a morte de mascariane, Vinicta agora está em paz, podendo seguir com sua cultura local e não ficando mais\n"
                                            "dependente de Mascariane", 0.08)
                                        txt(f"Após matar Mascariane, {nome_do_jogador}", 0.08)
                                        txt("Se mudou com sua família para algum reino ao norte para poder cuidar do YETI, que consequentemente é a sua cultura.", 0.08)
                                        txt("Nunca mais voltando para o Vinicta ou a antiga Catedral que agora é Mambla", 0.08)

                                elif escolhas[8] == 2:
                                    txt("\nMascariane estava repleto de magos para discursar, porém, antes de começar começou uma rebelião na porta da\n"
                                        "igreja, o que o fez recuar para dentro da igreja.", 0.08)
                                    txt("Indo pelo telhado é possível pegar Mascariane desprevinido.", 0.08)
                                    txt("Lá está ele! Levou um susto ao nos ver.", 0.08)
                                    txt("Uma batalha está para acontecer.", 0.08)
                                    time.sleep(0.3)
                                    # Batalha Final 1:
                                    # Nome: Mascariane
                                    # Atb: [2000, 60, 100]
                                    # Quando ele estiver quase morrendo parara o código.
                                    txt("Grrr..", 0.08)
                                    txt("Grrr....", 0.08)
                                    txt("Do nada a parede é quebrada, revelando ser um.. YETI?!", 0.08)
                                    txt("Infelizmente Mascariane o Matou assim que tentou o atacar.", 0.08)
                                    txt("E assim reiniciando a batalha.", 0.08)
                                    txt("Batalha Final iniciando...", 0.08)
                                    # Batalha Final 2 (Final msm):
                                    # Nome: Mascariane
                                    # Atb: [2000, 60, 100]
                                    txt("Após a batalha você percebe que o YETI na verdade era a criatura dentro do ovo, tocando nela consegue ter visões\n"
                                        "das torturas praticadas por Mascariane com o OVO para tentar conseguir a exência pura dele.",
                                        0.08)
                                    txt("Após um enterro dígno, o YETI agora poderá descansar em paz.\n", 0.08)
                                    time.sleep(0.4)
                                    txt("Sua família agora está solta das mãos de Mascariane. Está livre para terem sua cultura local novamente!", 0.08)
                                    txt("Soube que o Guerreiro virou o rei da Catedral, até mudou o nome dela para Mambla. Tudo parece muito bem!", 0.08)
                                    txt("Algumas pessoas preferiram cultivar a idéia inicial da igreja, a idéia da bondade, causando assim a criação de várias\n"
                                        "igrajas, mas agora supervisionadas pelo Guerreiro.", 0.08)

                        elif escolhas[6] == 2:
                            txt("\nIndo a um bar de esquina você escuta sobre um ovo, e se aproxima para ouvir..", 0.08)
                            txt("-'Aquele ovo estava uma delícia'", 0.08)
                            txt("Não tinha nada a ver com o que procura!", 0.08)
                            txt("Ao sair do bar, um algúem estava sendo decaptado, mas antes de morrer ele disse: ", 0.08)
                            txt("-'O OVO, NÃO O DEIXEM PEGAR, NA PONTE OS AGUARD..'", 0.08)
                            txt("O que será que ele quis dizer?", 0.08)
                            txt("Passando por uma rua, ladrões tentam roubar o seu dinheiro a força.", 0.08)
                            txt("Uma batalha estaria começando...", 0.08)
                            # Batalha:
                            # Nome: Bandidos
                            # ATB: [350, 40, 80]
                            txt("Derrotando eles um portal se abre, mostrando a entrada da Catedral.", 0.08)
                            escolhas.append(ver(input("Escolhas:\n"
                                                      "[1].Entrar no Portal.\n"
                                                      "[2].Não entrar.\n"
                                                      "Sua escolha: "), ["1", "2"]))
                            if escolhas[7] == 1:
                                txt("\nOlhando para trás, alguém estava te observando, logo após ve-lo o portal se fecha", 0.08)

                            elif escolhas[7] == 2:
                                txt("Alguém lhe empurra e te faz passar pelo portal.", 0.08)
                                txt("Em seguida o portal se fechou.", 0.08)

                            txt("Guardas estavam te esperando!!", 0.08)
                            time.sleep(0.3)
                            txt("-'Você foi recrutado para o experimento de algo horroso.', disse o Padre.", 0.08)
                            txt("Descendo uma masmorra, percebe que está sendo levada para um experimento.", 0.08)
                            txt("Eles te deixam sozinho com o OVO, talvez por acha que você virará alimento.", 0.08)
                            txt("Mas pelo contrário, no momento em que se sentou ao lado dele ele rachou, como se estivesse chocando", 0.08)
                            txt("E estava. Assim que os guardas saíram ele chocou, mostrou ser um YETI, só que te você como a mamãe dele.", 0.08)
                            txt("Os guardas estão votando!!", 0.08)
                            time.sleep(0.4)
                            txt("Uma batalha está se aproximando.", 0.08)
                            # Batalha:
                            # Nome: Os gandias
                            # Atb: [700, 70]
                            dinheiro += 100
                            txt("Agora vocês estão livres, e estão juntos!!", 0.08)
                            txt("Finalmente conseguiu recuperar o que antes era de sua avó.", 0.08)
                            txt("Após isso, você se apresanda o YETI para a família de Vinicta.", 0.08)
                            txt("Todos estão perplexos, a muito tempo não viam tal ser.", 0.08)
                            txt("-'As histórias dos livros eram verdadeiras, nós tinhamos um passado.'", 0.08)
                            txt("Após isso começaram a reconstruír sua antiga cultura!", 0.08)

                    elif escolhas[5] == 2:
                        txt("\nO rei está ciente do ocorrido.", 0.08)
                        txt("-'Como você sabe sobre o ovo?!'", 0.08)
                        txt("-'Nós estamos envolvidos!! A igreja nós deve benefícios.'", 0.08)
                        txt("-'Nos ofereceu prosperidade perante os demais reinos, entretanto, não cumpriram o trato.'", 0.08)
                        txt("-'Nosso plano aqui é negociar com Mascariane.'", 0.08)
                        txt("-'Não quer se juntar a nós? Você ficará rica também! Talvez possa ter até um reino para você!'", 0.08)
                        time.sleep(0.4)
                        escolhas.append(ver(input("Escolhas:\n"
                                                  "[1].Aceitar proposta.\n"
                                                  "[2].Não aceitar proposta.\n"
                                                  "Sua escolha: "), ["1", "2"]))
                        if escolhas[6] == 1:
                            txt("\n-'Então está feito! Estaremos juntos nessa conquista jovem Elfo.'", 0.08)
                            txt("-'O ovo está debaixo da ponte, vá ajudar a defende-lo do padre que está vindo'", 0.08)
                            time.sleep(0.4)
                            txt("Chegando lá você se depara com 3 pessoas encapuzadas com o ovo, mas você diz vir a mando do rei.", 0.08)
                            txt("Em seguida aparece não 1, mas 2 padres. \n"
                                "-'Devolva-no, ainda não terminaomos.'", 0.08)
                            txt("Você pega um padre, e os outros pegam o outro.", 0.08)
                            # Batalha:
                            # Nome: Padre benel, O caído!
                            # atb: [700, 60, 100]
                            txt("-'Nós voltaremos!! Apartir do dia de hoje haverá guerra!!'", 0.08)
                            time.sleep(0.4)
                            txt("O rei está repensando no que fez agora. Não consegue ver uma vitória em uma guerra contra a igreja.", 0.08)
                            txt("Até que.. O rei te pede para ir falar com Mascariane.", 0.08)
                            txt("-'Já que sua família é próxima a ele a bastante tempo talvez seja mais fácil.'", 0.08)
                            txt("Não há outro jeito. Se não for talvez seja o fim de Vinicta", 0.08)
                            time.sleep(0.4)
                            print()
                            txt("Chegando lá você é recebido pelos guardas, algo não parece normal.", 0.08)
                            txt("É dito que os padres que voltaram falaram de um elfo que estava envolvido com um roubo a igreja",
                                0.08)
                            txt("Chegando aos pés de Mascariane ele pergunta do porque você estar alí.", 0.08)
                            txt("Ao falar sobre o acordo não cumprido pela igreja, Mascariane fica furioso.", 0.08)
                            txt("-'Isso não é da sua conta, um mero pedaço de escória. Você não deveria ter se envolvido com isso.'",
                                0.08)
                            txt("-'Joguem-na na masmorra.'", 0.08)
                            time.sleep(0.5)
                            print()
                            txt("No caminho para a masmorra alguém com uma espada e uma coroa estava no caminho.", 0.08)
                            txt("-'Parem, eu preciso desta Elfa!!'", 0.08)
                            time.sleep(0.4)
                            txt("-'Saia do caminho, LIXO.'", 0.08)
                            time.sleep(0.4)
                            txt("Uma batalha estava prestes a acontecer!!", 0.08)
                            txt("O Guerreiro mostrou sua força, mas são muitos guardas reais.", 0.08)
                            txt("Até que um dos guardas deixa cair a chave de suas algemas", 0.08)
                            txt("Uma batalha está se iniciando.", 0.08)
                            time.sleep(0.4)
                            # Batalha:
                            # Nome: Guardas
                            # Atb: [600, 70, 100]
                            dinheiro += 100
                            txt("Após derrotar os guardas o guerreiro explica que precisa da sua ajuda para matar Mascariane", 0.08)
                            txt("-'Infelizmente ele é muito forte, não consigo sozinho. Soube que você está tentando\n"
                                "mudar a vida da sua família, vamos derrota-lo!!'", 0.08)
                            time.sleep(0.4)
                            txt("No caminho tem muitos guardas! Terão que derrotar um por um", 0.08)
                            # Batalha 1:
                            # Nome: Guardas Nivelo
                            # Atb: [450, 50]
                            dinheiro += 100
                            txt("\nMais um trio a frente!\n", 0.08)
                            time.sleep(0.4)
                            # Batalha 2:
                            # Nome: Prego na
                            # Atb: [450, 50]
                            txt("\nAos poucos vão chegando ao portão da igreja!", 0.08)
                            txt("Lá encontram um mago que ós ajudou a entrar na igreja, diz ele que quer ajudar o mundo.", 0.08)
                            txt("Ele os leva até Mascariane.", 0.08)
                            txt("Lá está ele. Comendo úvas se assusta com a presansa dos 3.", 0.08)
                            txt("\n-'Viemos matalo, prepare-se', disse o Guerreiro.", 0.08)
                            txt("-'HA HA HA HA', diz Mascariane.", 0.08)
                            txt("-'Pois bém, jovens. Podem vir!!'", 0.08)
                            txt("Uma batalha está prestes a começar.", 0.08)
                            # Batalha Final:
                            # Nome: Mascariane
                            # Atb: [1500, 70]
                            print()
                            txt("Após a morte de Mascariane o mundo pode finalmente respirar, estão livres da opressão da igreja.", 0.08)
                            txt("Vocês 3 se separaram e nunca mais se viram novamente.", 0.08)
                            txt("O ovo? Quem sabe aonde está?... A paz agora está reinando sobre nós.", 0.08)
                            txt("Sua família agora pode voltar com suas culturas, evoluírem, voltar a ser o que eram no passado.", 0.08)

                        elif escolhas[6] == 2:
                            txt("-'Infelizmente você fez a escolha errada. Guardas!!'", 0.08)
                            txt("-'Desculpe Jovem, mas ninguém além de nós pode saber sobre.'", 0.08)
                            txt("Você é levado para uma prisão, mas no caminho um dos guardas a ajuda a escapar.", 0.08)
                            txt("Mas vocês tem que se livrar dos guardas atrás de vocês!", 0.08)
                            txt("Uma batalha está iniciando.", 0.08)
                            time.sleep(0.4)
                            # Batalha:
                            # Nome: Guardas reais
                            # ATB: [600, 45]
                            txt("Você conseguiu derrota-los, mas o guarda que te ajudou não. Então você foge para a floresta.", 0.04)
                            txt("Ao fugir para a floresta você vê uma carroça coberta.", 0.08)
                            txt("Ela está repleta de garrafas com água.", 0.08)
                            txt("Alguém está vindo busca-la.", 0.08)
                            txt("Em direção norte você nota estar em um território familiar.", 0.08)
                            txt("Ao chegar descobre ser a Catedral. Voltando a estaca 0", 0.08)
                            txt("", 0.08)
                            txt("Indo falar com Mascariane sobre o ovo ele te recompensa. Oferece a salvação de sua família se\n"
                                "você conseguir recuperar o ovo.", 0.08)
                            escolhas.append(ver(input("Escolhas:\n"
                                                      "[1].Aceitar.\n"
                                                      "[2].Aceitar.\n"
                                                      "Isso não é mais uma brincadeira!\n"
                                                      "Sua escolha: "), ["1", "2"]))
                            if 1 == escolhas[7] == 2:
                                txt("\nVocê vai até o rei de Vinicta, mas agora está preparado para uma guerra! Está pronto!", 0.08)
                                txt("O rei Vinicta se mostra surpreso, mas não recua perante a guerra eminente.", 0.08)
                                txt("Estão prestes a começar..", 0.08)
                                time.sleep(0.4)
                                # Batalha Final:
                                # Nome: Vinicta
                                # Atb: [1200, 60]
                                txt("Derrotando Vinicta, Mascariane honrra sua palavra.", 0.08)
                                txt("Os elfos estão oficialmente livres das mãos da catedral. Podem voltar a ser o que quiserem ser!", 0.08)
                                time.sleep(0.08)
                                txt("Muito tempo se passou e Mascariane conseguiu dominar vários reinos, mas não chegou mais perto dos Elfos", 0.08)
                                txt("Tudo está bem, pelo menos por enquanto.", 0.08)

                elif escolhas[3] == 2:
                    print("Voltar aqui!")

            elif escolhas[2] == 2:
                txt("\nAo saír da catedral um mudo aponta para Vinicta.", 0.08)
                txt("Indo para lá, você se depara com restos de corpos, pilhas. Todos em volta de algo com um ninho.", 0.08)
                txt("Algo que se parece com um ovo estavalá, mas estava repleto de lobos.", 0.08)
                txt("Você precisa matar os lobos tocar no ovo.", 0.08)
                # Batalha:
                # Nome: Lobos
                # Atb: [500, 50]
                txt("Chegando no ovo, ao toca-lo percebe que é falso.", 0.08)
                txt("Era uma emboscada!!", 0.08)
                time.sleep(0.4)
                txt("Você foi capturado e levado ao rei Vinicta", 0.08)
                txt("-'Quem é você? Está atrás do ovo novamente?'", 0.08)
                txt("Você nega! Então ele pergunta o porque de você está alí.", 0.08)
                txt("Ao explicar que está tentando achar o ovo para devolver a Mascariane ele fica furioso.", 0.08)
                txt("-'Não podemos devolver a mascariane!! Você como qualquer outro deveria saber disso.", 0.08)
                txt("Eles está tentando extraír a essência pura que este ovo carrega, e com isso se tornar imparável,\n"
                    "nenhum reino conseguirá detelo se conseguir.", 0.08)
                txt("Você deve se juntar a nós na jornada de proteger o ovo das mãos de Mascariane'", 0.08)
                escolhas.append(ver(input("Escolhas:\n"
                                          "[1].Proteger o ovo.\n"
                                          "[2].Não proteger, mas cuidar dele.\n"
                                          "Sua escolha: "), ["1", "2"]))
                time.sleep(0.4)
                if escolhas[3] == 1:
                    txt("\n-'Não será nada fácil, Mascariane virá com seu exército, mas faremos o possível para que não passem!'", 0.08)
                    txt("-'Esteja preparado quando a hora chegar!'", 0.08)
                    time.sleep(0.6)
                    txt("Anos depois..", 0.1)
                    txt("O Exército de Mascariane se aproxima, eles vem para Matar.", 0.08)
                    txt("Por sorte Vinicta também tem magos poderosos, treinou-os escondidos da igreja.", 0.08)
                    txt("Conseguem segurar o exército, mas não conseguem segurar Mascariane, ele conseguiu entrar.",
                        0.08)
                    txt("Indo em direção ao OVO", 0.08)
                    txt("Até que vocês dois se encaram frente a frente.", 0.08)
                    txt("-'Você traíu sua família e a catedral, sua sentença é a morte!!!'", 0.08)
                    # Batalha:
                    # Nome: Mascariane
                    # Atb: [1000, 60]
                    txt("Ao matar mascariane, seu exército recuou, e logo foi dominado por Vinicta, porém, o rei de Vinicta\n"
                        "decidiu deixar no poder o antigo herdeiro por direito. O Filho de Mambla que ainda estava vivo,\n"
                        "mas com a supervisão do rei Vinicta.", 0.08)
                    txt("Ele revigorou o reino em pouco tempo, mostrou-se ser competente para o cargo.", 0.08)
                    txt("Após a morte de Mascariane, o a população pode viver agora sem medo! Sem ter a mão dele pairando\n"
                        "sobre suas cabeças.", 0.08)
                    txt("Além de recuperar a erança que é o ovo, os Elfos voltaram a desenvolver ovos usando um ritual antigo.", 0.08)
                    time.sleep(0.4)
                    txt("2 anos se passaram..", 0.08)
                    txt("O mundo parece estar evoluindo, algumas pessoas preserváram a menságem da igreja de ajudar os menos afortunados.", 0.08)
                    txt("Com o tempo várias igrejas pequenas foram sendo fundadas, mas todas sendo supervisionadas pelo rei do reino que\n"
                        "cada uma estivesse.", 0.08)

                elif escolhas[3] == 2:
                    time.sleep(0.6)
                    txt("\nAo tocar no ovo, você tem uma visão de tortura, talvez fosse o passado do ovo. A tortura constante e agonizante.\n", 0.08)
                    txt("Mais de 100 anos de tortura são mostrado a você em 5 minutos.", 0.08)
                    txt("Anos depois...", 0.08)
                    txt("Anos depois..", 0.1)
                    txt("O Exército de Mascariane se aproxima, eles vem para Matar.", 0.08)
                    txt("Por sorte Vinicta também tem magos poderosos, treinou-os escondidos da igreja.", 0.08)
                    txt("Conseguem segurar o exército, mas não conseguem segurar Mascariane, ele conseguiu entrar.", 0.08)
                    txt("Indo em direção ao OVO", 0.08)
                    txt("Até que vocês dois se encaram frente a frente.", 0.08)
                    txt("-'Você traíu sua família e a catedral, sua sentença é a morte!!!'", 0.08)
                    # Batalha Final:
                    # Nome: Mascariane
                    # Atb: [1000, 60]

                    txt("\nAo matar mascariane, seu exército recuou, e logo foi dominado por Vinicta, porém, o rei de Vinicta\n"
                        "decidiu deixar no poder o antigo herdeiro por direito. O Filho de Mambla que ainda estava vivo,\n"
                        "mas com a supervisão do rei Vinicta.", 0.08)
                    txt("Ele revigorou o reino em pouco tempo, mostrou-se ser competente para o cargo.", 0.08)
                    txt("Após a morte de Mascariane, o a população pode viver agora sem medo! Sem ter a mão dele pairando\n"
                        "sobre suas cabeças.", 0.08)
                    txt("Além de recuperar a erança que é o ovo, os Elfos voltaram a desenvolver ovos usando um ritual antigo.", 0.08)
                    time.sleep(0.4)
                    txt("2 anos se passaram..", 0.08)
                    txt("O mundo parece estar evoluindo, algumas pessoas preserváram a menságem da igreja de ajudar os menos afortunados.", 0.08)
                    txt("Com o tempo várias igrejas pequenas foram sendo fundadas, mas todas sendo supervisionadas pelo rei do reino que\n"
                        "cada uma estivesse.", 0.08)


        elif escolhas[1] == 2:
            txt("-'Então você estava de butuca?", 0.08)
            txt("Não basta o desserviço que sua família faz ao reino.", 0.08)
            txt("Você ouviu informações que levam a morte, Já foi decidido.'", 0.08)
            txt("[Desmaio]", 0.08)
            time.sleep(0.5)
            txt("Na masmorra você sofre constante abusos, assedios e torturas. Tudo para servir de"
                "experimento para novas magias.", 0.08)
            txt("Até que um mago escondido nas sombras o salva de sua tortura", 0.08)
            txt("Ele recrutou mais uma pessoa, um guerreiro.", 0.08)
            txt("Dizem estar atras da cabeça de Mascariane.", 0.08)
            txt("-'Ele está no castelo, vamos o atacar enquanto não está repleto de padres feiticeiros.', disse o mago.",
                0.08)
            txt("Entrando na igreja pelo telhado, vocês se deparam com lobos escuros como a noite.", 0.08)
            txt("Uma batalha está prestes a começas.", 0.08)
            # Batalha:
            # Nome: Lobos da noite
            # Atb: [600, 60]
            dinheiro += 100
            txt("\nLogo após derrotar o lobo Mascariane aparece batendo palmas.", 0.08)
            txt("-'Muito bem, muito bem, eu não esperava pro isso.'", 0.08)
            txt("Ele se prepara para o combate.", 0.08)
            # batalha final:
            # Nome: Mascariane
            # Atb: [1400, 60]
            dinheiro += 100
            txt("Ao matar Mascariane o reino foi reconquistado, e agora governado pelo herdeiro do antigo reino Mambla,\n"
                "o guerreiro da equipe.", 0.08)
            txt("O mundo finalmente está em paz, não são mais manipulados pela mão de mascariane.", 0.08)
            txt("Os magos que restaram simplesmente perderam seu poder após a morte de Mascariane. O tornando fracos e\n"
                "inofencívos.", 0.08)
            txt("Anos se passaram e a família dos Elfos finalmente conseguiram reestabelecer sua cultura, a cultivação\n"
                "de ervas, mana e desenvolvimento de ovos de criaturas místicas.", 0.08)
            txt(f"O novo rei ajuda os Elfos com tudo o que precisam. Diz estar em dívida por {nome_do_jogador} ter ajudado\n"
                "a derrotar mascariane", 0.08)
            txt("FIM!", 0.21)


elif class_e_atributos[0] == "Mago":
    print("A terminar")

txt("Equipe:\n"
    "Jefferson Mangueira Izaquiel;\n"
    "Josias Carneiro;\n"
    "Lorena Vitória.", 0.2)

txt(f"Todas sequências de escolhas que você fez: {escolhas}.", 0.22)

print("Muito obrigado por jogar!!")
