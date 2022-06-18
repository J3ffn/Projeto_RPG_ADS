# by Jefferson.
####################
import time
import random

####################

print("Atenção, pedimos que utilize apenas números para jogar o jogo, obrigado!")
# time.sleep(5)


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
            time.sleep(0.023)
        print()


##################################
# # # Lore dos personagens.
# - Guerreiro.
guerreiro_historia = """    Em um reino conhecido como Mambla, era acolhido um bebê recém-nascido que estava 
boiando numa cesta no rio por uma das filhas do rei Alexandre, na cesta estava escrito apenas 
seu nome, Samuel, por sorte, a família real era conhecida por sua bondade com o seu povo, 
Samuel estava em boas mãos. Ao completar 15 anos já era reconhecido pelo rei pela sua bravura 
e qualidade em lutas com espadas. No seu aniversário de 16 anos é comunicado ao rei que o 
papa da igreja central faria uma visita ao reino no mesmo dia, logo foram se programar para a 
chegada do papa, porém, ao longe se avista um homem que usava uma capa preta com um
capuz cobrindo seu rosto, parecia estar falando algo, quando do nada uma rocha era invocada, 
cobria todo o céu do reino e estava bem em cima do castelo, parecia estar de noite, mas também 
uma carta era entregue ao rei, dizendo: "Entregue o ovo, ou será amassado.", Soando frio o rei 
convoca seus melhores homens para levar sua família até um local seguro, mas não era possível 
sair, pois o mago havia criado uma espécie de barreira, mas existia uma falha,  porém, nela só 
podiam passar pessoas baixas, e o único que conseguiu passar por ela foi Samuel, tendo que 
deixar sua família e amigos para trás. Seu pai tentaria combater o mago ao invés de fazer o que 
foi pedido na carta, pois dizia ser perigoso entregá-lo a igreja. Percebendo a aproximação de 
tropas no portão, o misterioso mago solta a rocha em cima do reino, destruindo tudo, mas por 
causa dos destroços ele acaba se ferindo e rasgando sua capa, revelando assim sua marca da 
igreja, ele não ligava de ter a marca exposta, pois deduzia que todos estavam mortos, porém, 
do outro lado estava Samuel, se engasgando com as próprias lágrimas, mas atento a marca. 
Depois disso, Samuel jura vingança à igreja. E assim sua ambição escolhida, e sua história 
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

###
personagens = ["Guerreiro", "Arqueiro", "Mago"]
escolha = []
lista = [0, 0, 0]  # [HP, Força, Mana]

# Início.
print(f"""
    Bem-vindo(a) ao [Nome do jogo]

    Selecione uma classe para começar a jornada.

    1.{personagens[0]}, 2.{personagens[1]}, 3.{personagens[2]}
    """)
escolha.append(int(input("Escolha: ")))
if escolha[0] == 1:
    escolha.append(lista[0])
    txt(guerreiro_historia)

if escolha[0] == 2:
    escolha.append(lista[1])
    txt(elfa_historia)

if escolha[0] == 3:
    escolha.append(lista[2])
    txt(mago_historia)
