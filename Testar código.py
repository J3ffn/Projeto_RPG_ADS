# Lembrete!
# Os prints que tem "Voltar aqui!" são os que ainda estão para ser feito!
# Quando tiver "# Combate:" é pq vai puxar a função de combate!
# Adicionar um ítem de erança na parte de algum final. Fazer atribuição aos atributos.
import time, random

# Função texto
def txt(texto, tempo):
    for i in range(1):
        for c in texto:
            print(c, end='')
            time.sleep(tempo if "-" not in texto else 0)
        print()

dinheiro = 0
escolhas = []
class_e_atributos = [0]
personagens = [
    ["Guerreiro", [100, 0, 90]],
    ["Elfo", [110, 90, 100]],
    ["Mago", [90, 100, 110]],
]
print(f"""
{'-' * 60}
{'Bem-vindo(a) ao [Nome do jogo]'.center(60)}

{'Selecione uma classe para começar a jornada.':^60}
{"[1]":^20} {"[2]":^20} {"[3]":^20}
{personagens[0][0]:^20} {personagens[1][0]:^20} {personagens[2][0]:^20}
{'-' * 60}""")

class_e_atributos[0] = int(input("Sua escolha: "))

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
    escolhas.append(int(input("""Reinos:
        [1]. Minic
        [2]. Blugg
Sua escolha: """)))
# Adicionar verificação de erro.

    if escolhas[0] == 1:
        txt("\nÀ caminho de Minic, você encontra saqueadores. Eles ainda não\n"
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
                txt("\nSeguindo em frente um bando de lobos o esperava, era"
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
                escolhas.append(int(input("\n[1].Falar com barman.\n"
                                        "[2].Falar com bêbados.\n"
                                        "Sua escolha: ")))
                # Adicionar verificação depois.

                if escolhas[2] == 1:
                    time.sleep(0.15)
                    txt('"\nEu poderia contar a eles que você está por aqui.."\n', 0.08)
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
                    txt("\nBêbados geralmente não sabem guardar segredo!", 0.1)
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
                        txt("\nO barman está te espeando a um tempo.", 0.13)
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
                                txt("\nUm bêbado falou tentou falar de algo atrás\n"
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
                                        "intençõs agora com o YETI.", 0.16)

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
            txt("\nPelos desenhos parece que eles já sabiam disso.", 0.1)
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
                txt("\nVocê vai ao reino de Minic para falar com Julius.", 0.12)
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
    # txt(elfa_historia, 0.06)
    escolhas.append(int(input("Escolhas:\n"
                              "[1].Falar com a mãe sobre o ovo perdido.\n"
                              "[2].Ir atrás de mais informações.\n"
                              "Escolha: ")))

    if escolhas[0] == 1:
        print("Voltar aqui!")

    elif escolhas[0] == 2:
        txt(f"\nSaindo de Trozar, {nome_do_jogador} parte em busca de sua aventura!\n", 0.1)
        txt(f"Para descobrir mais sobre o que foi roubado, será necessário conversar com os guardas,\n"
             "por sorte um deles já foi da família, mas continua sendo da família.\n", 0.07)
        txt("Porém, Mascariane talvez mascariane te remunere se conseguir recupera-lo para ele", 0.08)
        time.sleep(0.4)
        escolhas.append(int(input("Escolhas:\n"
                                  "[1].Falar com antigo familiar\n"
                                  "[2].Falar com Mascariane.\n"
                                  "Escolha: ")))
        if escolhas[1] == 1:
            txt("\nDentro da capital, só existe um local para ele estar.\n"
                "O bar S, o único bar liberal da catedral, bar esse não conhecido por Mascariane.", 0.06)
            time.sleep(0.3)
            txt("Lá está ele!! Tomando uma breja gelada daquelas.", 0.04)
            txt("Bébado ele diz:" 
                "-'Minha garota. O que lhe traz aqui?'")
            escolhas.append(int(input("Escolhas:\n"
                                      "[1].Perguntar sobre ítem roubado.\n"
                                      "[2].Falar sobre família."
                                      "Escolha: \n")))
            time.sleep(0.2)
            if escolhas[2] == 1:
                txt("\n-Ítem? Que ítem? Aaaa, você está falando, Burp!.., do ovo", 0.07)
                txt("OVO??", 0.1)
                txt("[Ele apénas sorri e se deita.]", 0.1)
                time.sleep(0.3)
                txt("-'Eu não deveria ter te contado isso, mas agora já era.'", 0.06)
                txt("'O ovo é uma erança de sua família, tempos atrás eu cudava dele, até que..'")
                time.sleep(0.2)
                txt("ATÉ QUE O QUE?!", 0.2)
                txt("'Até que o chefia chegou de ameaçou matar a todos se não entregassem sua última\n"
                "erança, que era o OVO, ainda não sabemos o que o ovo vai gerar, mas é algo diferente'\n", 0.08)
                txt("'Não posso mais falar nada sobre, senão serei morto.'", 0.08)
                time.sleep(0.2)
                txt("O barman está te chamando!", 0.08)
                escolhas.append("Escolhas:\n"
                                "[1].Falar com Barman.\n"
                                "[2].Ir embora.\n"
                                "Escolha: ")
                time.sleep(0.3)
                if escolhas[3] == 1:
                    txt("\n-Shhhhh..", 0.2)
                    txt("-'Você está em búsca do que foi roubado? Eu ouvi dizer que eles foram para\n"
                        "o reino Vinicta'", 0.09)
                    txt("Por que você está me ajudando?", 0.09)
                    txt("-'Digamos que eu tenho uma dívida com os Elfos. [Mostra uma perna de pau]'", 0.06)
                    escolhas.append("Escolhas:\n"
                                    "[1].Confiar e ir para Vinicta\n"
                                    "[2].Perguntar sobre a história da perna\n"
                                    "Escolha: ")
                    if escolhas[4] == 1:
                        txt("\n-'Antes de ir, tome isso!'\n"
                        "-'O colar da sua avó, ela me pediu para entregar à você, mas nunca a ví antes deste dia.\n"
                        "Eu não sei se é mágico ou é apénas um colar normal, mas ele agora é seu!!'\n", 0.1)
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
                    escolhas.append(int(input("Escolhas:\n"
                                              "[1].Buscar pelo ítem.\n"
                                              "[2].Falar com o rei sobre.\n"
                                              "Escolha: ")))
                    if escolhas[5] == 1:
                        escolhas.append(int(input("\nEscolhas:\n"
                                                  "[1].Pedir informações a alguém.\n"
                                                  "[2].Ir para bares coletar informações.\n"
                                                  "Escolha: ")))
                        time.sleep(0.3)
                        if escolhas[6] == 1:
                            txt("\nNinguém parece querer te ajudar quanto a isso!", 0.08)
                            txt("Além de estarem começando a desconfiar de você.", 0.08)
                            txt("Perto de um lago tem um velho que todos dizem ser maluco", 0.08)
                            escolhas.append(int(input("Escolhas:\n"
                                                      "[1].Falar com o velho.\n"
                                                      "[2].Ignorar.\n"
                                                      "Escolha: ")))
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
                                escolhas.append(int(input("Escolhas:\n"
                                                          "[1].Treinar para rivalizar com Mascariane.\n"
                                                          "[2].Ir direto a Mascariane.\n"
                                                          "Escolha: ")))
                                time.sleep(0.08)
                                while escolhas[-1] == 2:
                                    txt("\nPéssima escolha! Você morreu na primeira tentativa.", 0.08)
                                    escolhas.pop
                                    escolhas.append(int(input("Escolhas:\n"
                                                              "[1].Treinar para rivalizar com Mascariane.\n"
                                                              "[2].Ir direto a Mascariane.\n"
                                                              "Escolha: ")))

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
                                    print()
                                    txt("Governe bem, seja melhor do que mascariane foi!", 0.08)
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
                                      f"{'-'* 40}")

                                time.sleep(0.6)
                                txt("Enfurecido, você vai direto mara a Catedral", 0.08)
                                time.sleep(0.1)
                                txt("Um guerreiro estava lá, mas conversando o guerreiro revela que também está atráz de Mascariane, só que para matalo.", 0.08)
                                txt("Sem exitar você se junta a ele na jornada até que uma mulher grávida fala sobre experimentos dentro de uma masmorra.", 0.08)
                                escolhas.append("Escolhas:\n"
                                                "[1].Ir para Masmorra\n"
                                                "[2].Continuar com Guerreiro.\n"
                                                "Sua Escolha: ")
                                time.sleep(0.3)
                                if escolhas[8] == 1:
                                    txt("\nEra uma pessagem atrás da igreja, bem escondida!")
                                    txt("Entrando lá, várias pessoas estavam enjauladas, várias multiladas, órgãos estavam jogados sobre uma mesa.\n"
                                    "Aparentemante não havia ninguém alí, mas descendo mais 4 magos são avistados, e..", 0.08)
                                    txt("Lá está! O ovo, dentro de algo com.. água?!")
                                    escolhas.append("Escolhas:\n"
                                                    "[1].Lutar de frente."
                                                    "[2].Esperar todos irem embora.")
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
                                        escolhas.append(int(input("Escolhas:\n"
                                                                  "[1].Subir em cima dele.\n"
                                                                  "[2].Não subir em cima.\n"
                                                                  "Escolhas: ")))
                                        if escolhas[10] == 1:
                                            txt("\nApós isso ele quebra a parece ao seu lado.", 0.08)
                                            txt("Lá estão Mascariane e o Guerreiro se matando, com a quebra da parede foi uma obrigação intervir no combate, se aliando ao lado do guerreiro.", 0.08)

                                        elif escolhas[10] == 2:
                                            txt("Do nada ele quebra a parede!", 0.08)
                                            txt("Lá estão Mascariane e o Guerreiro se matando, com a quebra da parede foi uma obrigação intervir no combate, se aliando ao lado do guerreiro.", 0.08)

                                        # Batalha final
                                        # Nome: Mascariane
                                        # Atributos: [2000, 90]
                                        dinheiro += 100
                                        txt("Após a morte de mascariane, Vinicta agora está em paz, podendo seguir com sua cultura local e não ficando mais dependente de Mascariane", 0.08)
                                        txt(f"Após matar Mascariane, {nome_do_jogador}", 0.08)
                                        txt("Se mudou com sua família para algum reino ao norte para poder cuidar do YETI, que consequentemente é a sua cultura.", 0.08)
                                        txt("Nunca mais voltando para o Vinicta ou a antiga Catedral que agora é Mambla")

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
                                    txt("Batalha Final iniciando...")
                                    # Batalha Final 2 (Final msm):
                                    # Nome: Mascariane
                                    # Atb: [2000, 60, 100]
                                    txt("Após a batalha você percebe que o YETI na verdade era a criatura dentro do ovo, tocando nela consegue ter visões\n"
                                    "das torturas praticadas por Mascariane com o OVO para tentar conseguir a exência pura dele.", 0.08)
                                    txt("Após um enterro dígno, o YETI agora poderá descansar em paz.\n", 0.08)
                                    time.sleep(0.4)
                                    txt("Sua família agora está solta das mãos de Mascariane. Está livre para terem sua cultura local novamente!", 0.08)
                                    txt("Soube que o Guerreiro virou o rei da Catedral, até mudou o nome dela para Mambla. Tudo parece muito bem!", 0.08)
                                    txt("Algumas pessoas preferiram cultivar a idéia inicial da igreja, a idéia da bondade, causando assim a criação de várias\n"
                                    "igrajas, mas agora supervisionadas pelo Guerreiro.")

                        elif escolhas[6] == 2:
                            txt("\nIndo a um bar de esquina você escuta sobre um ovo, e se aproxima para ouvir..", 0.08)
                            txt("-'Aquele ovo estava uma delícia'", 0.08)
                            txt("Não tinha nada a ver com o que procura!", 0.08)
                            txt("Ao sair do bar, um algúem estava sendo decaptado, mas antes de morrer ele disse: ", 0.08)
                            txt("-'O OVO, NÃO O DEIXEM PEGAR, NA PONTE OS AGUARD..'", 0.08)
                            txt("O que será que ele quis dizer?", 0.08)
                            txt("Passando por uma rua, ladrões tentam roubar o seu dinheiro a força.", 0.08)
                            txt("Uma batalha estaria começando...")
                            # Batalha:
                            # Nome: Bandidos
                            # ATB: [350, 40, 80]
                            txt("Derrotando eles um portal se abre, mostrando a entrada da Catedral.", 0.08)
                            escolhas.append("Escolhas:\n"
                                            "[1].Entrar no Portal."
                                            "[2].Não entrar.")
                            if escolhas[7] == 1:
                                txt("Olhando para trás, alguém estava te observando, logo após ve-lo o portal se fecha", 0.08)

                            elif escolhas[7] == 2:
                                txt("Alguém lhe empurra e te faz passar pelo portal.", 0.08)
                                txt("Em seguida o portal se fechou.", 0.08)

                            txt("Guardas estavam te esperando!!")
                            time.sleep(0.3)
                            txt("-'Você foi recrutado para o experimento de algo horroso.', disse o Padre.", 0.08)
                            txt("Descendo uma masmorra, percebe que está sendo levada para um experimento.", 0.08)
                            txt("Eles te deixam sozinho com o OVO, talvez por acha que você virará alimento.", 0.08)
                            txt("Mas pelo contrário, no momento em que se sentou ao lado dele ele rachou, como se estivesse chocando", 0.08)
                            txt("E estava. Assim que os guardas saíram ele chocou, mostrou ser um YETI, só que imaginou você como a mamãe.", 0.08)
                            
                    elif escolhas[5] == 2:
                        print("Voltar aqui!")

                elif escolhas[3] == 2:
                    print("Voltar aqui!")
                    
            elif escolhas[2] == 2:
                print("Voltar aqui!")

        elif escolhas[1] == 2:
            print("Voltar aqui")

elif class_e_atributos[0] == "Mago":
    print("A ser construída")

txt("Equipe:\n"
"Jefferson Mangueira Izaquiel;\n" 
"Josias Carneiro;\n"
"Lorena Vitória.", 0.2)

txt(f"Todas sequências de escolhas que você fez: {escolhas}.", 0.22)

print("Muito obrigado por jogar!!")
