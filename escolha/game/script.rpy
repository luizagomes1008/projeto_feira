# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image cafedamanha = Transform("images/salam.png", fit = "cover")
image salam = Transform("images/salam.png", fit = "cover")
image banheirouniforme = Transform("images/banheirodianaemprego.png", fit = "cover")
image geladeira = Transform("images/geladeira.png", fit = "cover")
image quarton = Transform("images/quarton.png", fit ="cover")
image cozinha = Transform("images/cozinha.png", fit ="cover")
image salan = Transform("images/salan.png", fit ="cover")
image kitnetn = Transform("images/kitnetn.png", fit ="cover")
image caixa = Transform("images/caixalanchonete.png", fit ="cover")
image dmente = Transform("images/dmente.png", fit ="cover")
image banheirolanchonete = Transform("images/banehirolanchonete.jpeg", fit ="cover")
image kitnet = Transform("images/kitnet.jpeg", fit ="cover")
image lanchoneten = Transform("images/lanchoneten.png", fit ="cover")
image lanchonete1 = Transform("images/lanchonete1.jpeg", fit ="cover")
image lanchonete = Transform("images/lanchonete.png", fit ="cover")
image lanchonete2 = Transform("images/lanchonete2.png", fit ="cover")
image lanchonete3 = Transform("images/lanchonete3.png", fit ="cover")
image lanchonete4 = Transform("images/lanchonete4.png", fit ="cover")


image onibusnoite:

    Transform("images/onibusnoite1.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusnoite2.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusnoite3.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusnoite4.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusnoite5.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusnoite6.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusnoite7.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15
    
    Transform("images/onibusnoite8.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    repeat

image onibusmanha:

    Transform("images/onibusmanha1.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusmanha2.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusmanha3.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusmanha4.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusmanha5.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusmanha6.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    Transform("images/onibusmanha7.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15
    
    Transform("images/onibusmanha8.png",
        xysize=(config.screen_width, config.screen_height))
    pause 0.15

    repeat

image quarto_fundo = Transform(
    "images/quarto.jpeg",
    xysize=(config.screen_width, config.screen_height)
)
image mesaquarto = Transform(
    "images/mesaquarto.png",
    xysize=(config.screen_width, config.screen_height)
)
image banheiro = Transform(
    "images/banheiro.jpeg",
    xysize=(config.screen_width, config.screen_height)
)
image celmensagem = "images/celularmensagem.png"
transform celular_maior:
    zoom 1.5
    xalign 0.5
    yalign 0.5
transform celular_menor:
    zoom 0.5
    xalign 0.5
    yalign 0.5
image celbloq ="/images/celularbloq.png"


define h = Character("Helena", color="#eb53ed")
image h hpadrao = "/images/personagens/hpadrao.png" 
image h hreceio ="images/personagens/hreceio.png"
image h hpadraobocaaberta ="images/personagens/Hdesconfiada.png"
# Helena começa no centro
transform h_centro:
    zoom 1.7
    xalign 0.5
    yalign 1.0
# Helena vai do centro para a esquerda
transform h_vai_esquerda:
    zoom 1.7
    xalign 0.5
    yalign 1.0
    linear 0.8:
        xalign 0.2
# Helena volta da esquerda para o centro
transform h_volta_centro:
    zoom 1.7
    xalign 0.2
    yalign 1.0

    linear 0.7:
        xalign 0.5
# Andreia entra pela direita e fica na direita
transform a_entrando_direita:
    zoom 1.9
    xalign 1.2
    yalign 1.0

    linear 0.8:
        xalign 0.8
# Andreia sai da direita, atravessando para a esquerda
transform a_saindo_esquerda:
    zoom 1.9
    xalign 0.8
    yalign 1.0

    linear 0.7:
        xalign -1.2

transform h_chegando:
    xalign 1.2
    yalign 1.0
    zoom 1.7
    linear 1.5:
        xalign 0.5
image h hrindo = "/images/personagens/hrindo.png" 
image h  hirritada = "/images/personagens/hirritada.png" 
image h holhofechado = "/images/personagens/holhofechado.png" 
image h halternatica ="images/personagens/halternativa.png"

define d = Character("Diana")
image dpadrao = "/images/Dpadrao.jpeg" 

define a = Character("Andreia", color="#66ccff")
transform andreia_chegando:
    xalign 0.5
    yalign 1.0
    linear 1.5 zoom 1.9
image a afeliz = "/images/personagens/afeliz.png" 
image a apadrao = "/images/personagens/apadrao.png"
image a apreocupada = "/images/personagens/apreocupada.png"
image a aalternativa = "/images/personagens/aalternativa.png"
image a airritada = "/images/personagens/airritada.png"


define e = Character("Elias", color="#ff9933", what_italic=True)
image e epadrao = "images/personagens/epadrao.png"


define g = Character("Gerente Julio", color="#e6df27")
image g golhoaberto = "images/personagens/polhoaberto.png"
image g golhofechado = "images/personagens/polhofechado.png"
image g gpadrao = "images/personagens/ppadrao.png"

transform g_chegando:
    xalign 1.2
    yalign 1.0
    zoom 1.5
    linear 1:
        xalign 0.5
transform g_saindo:
    xalign 0.5
    yalign 1.0
    zoom 1.5
    linear 1.5:
        xalign -1.2
default dinheiro = 80
default rede = 0
default confianca = 0

default empregoDia2 = False


# The game starts here.

label start:    
    #scene star
    scene dmente

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    pause 2.0
    d "Meu nome é Diana. Tenho 26 anos."
   

    d "Tenho uma vida como qualquer outra pessoa teria"
    d "Mas algumas escolhas podem mudar completamente o nosso caminho."
    pause 2.0
    d "desde que terminei o ensino médio minha vida tem sido difícil, até encontrar esse emprego "
    d "É cansativo... Mas não posso reclamar, agora tenho uma renda fixa."
    d "mesmo que não seja muito..."
    pause 3.0
    d "sinto que a qualquer momento o alarme vai-" #ai aqui o despertador iterrompe ela, e ela acorda, precisa adicionar o audio
    scene quarto_fundo with Dissolve(1.5) #with fade
    pause 2.0
    d"que dor de cabeça"
    d"preciso me arrumar para o trabalho, ou se não vou me atrasar"
    pause 1.0
    d"da ultima vez que isso aconteceu não foi bom..."
    pause 2.0 # aqui adiciona um barulho de notificação
    d"quem será?..."
    scene mesaquarto 
    
    d"quem será agora?" #no celular vai ter uma mensagem do patrão dizendo que precisa conversar com ela
  #  d"hm... cobrança do alugel, não posso me atrasar com isso..."
   # d "Nem venceu ainda e já tá me cobrando!
    show celbloq at celular_maior
    pause 1.0
    show celmensagem at celular_maior
    pause 1.0
    d"espero que tudo esteja bem..."
    pause 0.5
    scene dmente with fade
    pause 2
    scene banheiro  with fade
    pause 1.3
    scene banheirouniforme with Dissolve(1)
    d"preciso lavar esse uniforme o quanto antes"
    d"estou pronta"
    pause 2
    #saindo de casa
   # scene dmente with fade
    #pause 1.5
    scene kitnet with  fade
    pause 1
    a "Diana!"
    show a afeliz with moveinleft
    pause 1.5
    d"...???"
    show a afeliz at andreia_chegando
    a"Bom dia querida! como está?"
    d"ah, oi Andreia, estou bem! E sua filha, está tudo bem?"
    show a apreocupada
    a "ela pegou uma gripe chata, tenho que passar na farmacia..."
    d"coitadinha, já já ela se recupera"
    show a aalternativa
    a"ah vc sabe como ela é, vai se recuperar rapido"
    pause 1.5
    show a apreocupada
    a"devo estar te atrasando né?! Não me dei conta..."
    d"relaxa andreia, estou no horário, mas é melhor indo"
    show a afeliz
    a"bom trabalho querida, se cuida!"
    scene dmente with fade
    pause 2
    scene onibusmanha with  Dissolve(1) 
    pause 5
    scene dmente with fade
    pause 2
#no trabalho
    scene lanchonete1 with Dissolve(1)
    pause 1
    d"cheguei"
    show h hirritada at h_chegando
    h "diana!  por que não responde as mensagens que te mando?!"
    d"bom dia pra você também Helena"
    show h holhofechado 
    h"hm, bom dia"
    d"para de ser chata amiga!"
    show h hirritada
    pause 1
    show h hrindo
    h"chata é você!"
    pause 1
    show h hreceio
    h"enfim, o patrão mandou você ficar depois do curso, quer conversar contigo..."
    d"eu sei, ele me mandou mensagem hoje de manhã..."
    d"talvez eu consiga o meu tão sonhado aumento"
    show h halternatica
    h"é verdade! Vamos nos manter positivas!"
    show h hpadraobocaaberta
    h"é melhor eu ir atender o caixa, logo logo isso aqui vai encher de gente"
    d"é mesmo, você tem razão, vou para a área de serviço..."
    scene dmente with fade
    pause 1
    scene banheirolanchonete with fade
    d"eu espero realmente que seja apenas o aumento..."
    d"é melhor começar meu turno logo"
    scene dmente with Dissolve(1) 
    pause 2
    scene lanchonete with Dissolve(1) 
    pause 2

    scene lanchonete2 with Dissolve(1) 
    pause 2
 
    scene lanchonete3 with Dissolve(1) 
    pause 2  
     
    scene lanchonete4 with Dissolve(1) 
    pause 2
    scene dmente with fade
    pause 1
    scene lanchoneten
    d"terminei meu turno, estou tão cansada..."
    g"diana!"
    show g gpadrao at g_chegando
    d"ah! oi Julio"
    d"você queria conversar comigo, não é?"
    show g golhofechado 
    g"sim... bom..."
    pause 1.5
    g "Diana, movimento caiu. Estamos cortando gastos..."
    show g golhoaberto
    d"como assim?..."
    g" Hoje foi seu último dia. Passa no caixa, obrigado."
    d"Julio espera! eu pos-"
    show g gpadrao at g_saindo
    d"ah não..."
    scene dmente with fade
    pause 0.5
#no caixa
    scene caixa with fade
    d "R$80. Só isso... E o aluguel dia 15..."
    pause 1
    d"eu vou dar um jeito... Já está tarde, melhor voltar para casa..."
    scene dmente with Dissolve(1) 
    scene onibusnoite with fade
    pause 1
    d"não acredito nisso... Não sei o que vou fazer..."
    pause 5
    scene dmente with Dissolve(1) 
    scene kitnetn with fade
    d"..."
    scene dmente with fade
    pause 1
    scene salan with fade
    d"Depois de um dia longo finalmente vou descansar." 
    d"Mas como vou descansar sabendo da minha atual situação..."
    pause 0.5
    d"é melhor eu preparar algo para comer..."
    scene cozinha
    pause 0.5
    d"vejamos..."
    scene geladeira
    pause 1
    d"hmmm..."
    d"pizza serve"
    scene cozinha
    d"é melhor eu economizar mais do que antes"
    d"estava indo bem naquele emprego... Que pena..."
    pause 1
    d"*bocejo*"
    d"estou cansada, melhor ir dormir."
    scene quarton
    d"amanhã eu penso melhor no que fazer, preciso descansar..."
    pause 1
    scene dmente with Dissolve(1) 


#dia 2


    pause 2.5 #celular despertando
    scene quarto_fundo with Dissolve(1) 
    pause 1
    d"*bocejo*"
    d"quem está me ligando a essa hora da manhã?!"
    show celhelena at celular_menor
    d"Helena... "
    h "Bom dia, amiga."
    d "Bom dia..."
    h "Você tá bem?"
    d "Tô."
    h "Diana..."
    h "Eu te conheço. Você não tá bem."
    pause 1
    h"O Julio te despediu, não é? Descobri assim que cheguei em casa..."
    d"Sim... Justo quando comecei a me sustentar com aquele emprego e acontece isso..."
    h"Não fica assim Diana, abre aqui, vamos conversar!"
    d"Vou me trocar e já abro, até já..."
    hide celhelena
    pause 1 
    d"melhor ir logo"
    scene banheiro with fade #aqui é ela se vendo no espelho do banheiro
    d"..."
    pause 2 
    scene salam with fade
    d"pode entrar amiga."    
    show h hreceio at h_chegando
    h"Licença..."
    h"Oi Di... como está?"
    d"Estou bem... eu acho?"
    h"Quer conversar sobre? Você sabe que pode contar comigo sempre, não é?"
    d"eu..."
    pause 1
    menu:
        "Quero. Eu preciso desabafar. (+2 confiança)":
            $confianca += 2
            d "Eu tô com medo, Helena."
            show h hpadraobocaaberta
            d "Eu não sei se vou conseguir pagar o aluguel."
            h "Você não precisa resolver tudo hoje."
            h"um passo de cada vez, lembra?"

        "Não quero falar disso agora. (-2 confiança)":
            d "Eu só quero esquecer isso por enquanto."
            h "Tudo bem..."
            $confianca -= 2

        "Não é tão grave assim. (neutro)":
            d "Eu vou dar um jeito."
            h "Eu sei que vai. Mas você não precisa fingir que tá tudo bem comigo."
    show h hrindo 
    h"Você vai se recuperar rápido Diana, sei disso"
    d"Obrigada amiga, eu espero..."
    h"vem, vamos tomar café juntas na padaria do seu Zé!"
    d"não posso mais gastar Helena..."
    show h halternatica
    h"E você não vai gastar, da próxima você que paga hein!"
    h"Vamos!"
    show h hrindo
    d"Ok... Obrigada amiga"

    scene dmente with fade
    pause 2
    scene onibusmanha with  Dissolve(1) 
    pause 4
    scene cafedamanha with Dissolve(1) 
    #cena dela com a helena feliz na sua frente
    h"Fazia bastante tempo que não comemos aqui não é?"
    d"é verdade... Está diferente"
    h"costumávamos tomar o capuccino daqui depois das aulas, lembra?"
    d"com certeza, era tão gostoso"
    #cena helena feliz alternativa
    h"bom, então já sei o que pedir para nós"
    h"o que acha de uma porção de pão de queijo para acompanhar?"
    d"parece realmente muito bom..."
    #cena helena piscadela
    h"ok, vou pedir!"
    #cena dela sozinha
    d"Estava com saudades de sair com Helena"
    d"Ela me faz muito bem..."
    scene dmente with fade
    pause 1
    #cena delas com a comida na mesa
    h"prontinho, isso parece estar muito bom!"
    d"realmente, me lembra os tempos da escola."
    h "Você lembra quando a gente se conheceu?"
    d "Infelizmente."
    h "Nossa, vai começar..."
    d "Você derrubou café em mim."
    h "Foi sem querer!"
    d "Você falou que eu que estava no caminho."
    h "E estava mesmo."
    d "Helena!"
    scene dmente with fade
    pause 1
    #cena delas sem comida na mesa
    d"Estava muito bom."
    h"gostinho de nostalgia..."   
    h"vamos indo, eu te acompanho"
    d"Ok, o ônibus passa daqui 5 minutos"
    h"Bora!"
    scene dmente with fade
    pause 2
    scene onibusmanha with  Dissolve(1) 
    pause 4
    scene kitnet with Dissolve(1)
    show h hpadraobocaaberta at h_centro
    h"chegamos!"
    a"Helena! oiii!!"
    show h hrindo at h_vai_esquerda
    h"Dona Andreia! Oiê!"
    show a afeliz at a_entrando_direita
    h"Como você está? Nunca mais te vi!"
    a"Estou bem, e você Diana?"
    show a apadrao
    a"Uai, pensei que você estaria trabalhando nesse horário"
    show h hreceio
    d"então... Acontece que fui..."
    d"despedida"
    show a apreocupada
    a"Meu Deus! Sinto muito Diana!"
    a"Mas com certeza você vai achar oportunidades melhores"
    d"assim eu espero..."
    pause 1
    show h hpadraobocaaberta
    h "aquela ali não sua filha Dona Andreia?"
    show a apadrao
    a"Ah meu Deus, ela vai cair se continuar assim"
    show a airritada
    a"com licença meninas..."
    show a afeliz at a_saindo_esquerda
    pause 1
    hide a
    show h hpadrao at h_volta_centro
    d"vamos entrar amiga."
    show h hpadraobocaaberta at h_centro
    h"vamos sim"
    scene dmente with fade
    pause 1
    scene salam with fade
    show h hpadrao at h_chegando
    d"foi divertido, obrigada."
    show h hrindo 
    h"Que isso Diana, não precisa agradecer!"
    show h halternatica
    d"Eu te pago assim que possível Helena"
    show h hirritada
    h"Para com isso garota! Relaxa"
    show h halternatica
    h"Só de passar esse tempo contigo já me paga, deixa de besteira"
    show h hrindo
    pause 1
    d"Eu não sei o que fazer amiga..."
    show h hpadraobocaaberta
    h "Você não precisa decidir tudo agora."
    d "Mas eu não posso ficar parada para sempre."
    h "Eu sei. Só acho que você merece respirar um pouco antes."
    d "Respirar..."
    h "É. Você acabou de perder o emprego."
    d "Parece que tudo aconteceu tão rápido..."
    h "Então vamos fazer uma coisa de cada vez."
    d "E por onde eu começo?"
    h "Você pode começar descansando."
    show h hreceio
    d "Ou posso tentar resolver alguma coisa."
    h "O que você está pensando?"
    menu:
        "Quero começar a procurar um emprego":
            $empregoDia2 = True
            $ confianca += 1
            d "Talvez eu já devesse começar a entregar currículos."
            d"hoje mesmo"
            show h hreceio
            h "Se você quiser, eu vou com você."
            d "Você faria isso?"
            show h halternatica
            h "Claro que faria."
            d "Obrigada, Helena. De verdade."
            show h hrindo
            h "conte comigo sempre amiga!"
            scene dmente with Dissolve(1) 
            pause 1
            scene onibusmanha with Dissolve(1) 
            pause 1
            h"Eu sei de alguns lugares ótimos"
            d"obrigada por me ajudar"
            pause 3
        
     
        "Prefiro descansar um pouco":
            d "Acho que preciso de um tempo para colocar a cabeça no lugar."
            h "E tudo bem."
            d "Eu só queria esquecer tudo por algumas hours."
            h "Então hoje você vai descansar. Amanhã a gente pensa no resto."

        "Não sei o que quero fazer":
            d "Sinceramente? Eu não faço ideia."
            h "Você não precisa ter todas as respostas agora."
            d "Tenho medo de escolher errado."
            h "Às vezes, não escolher nada por enquanto também é uma escolha."
            d "Você sempre sabe o que falar, né?"
            h "Nem sempre. Só finjo que sei."
            d "Boba."
            h "Sua boba."





#surge elias
    e "Ô Diana! Dia 5! R$650 do aluguel."
    d "Elias, fui mandada embora hoje. Me dá até dia 15? Por favor?"
    e "Dia 15 então. Mas vai pra R$700 com juros. Dia 15 eu volto."

    scene dmente with Dissolve(1) 



#Dia 3



    pause 2.5 #celular despertando
    scene quarto_fundo with Dissolve(1) 
    pause 1
    d"*bocejo*"
    scene banheiro
    scene cozinha
    scene salam
    d "Tá... vamos ver as contas"
    d "Tenho [dinheiro] e preciso pagar R$700 do aluguel e comprar mais comida..."
    d "Não vai ser o suficiente... \n Dia 15 já já está aí... "
    d "Tenho que procurar uma forma de ganhar dinheiro... {p} Mas qual?"
    if empregoDia2 == True:
        d "Ontem já entreguei alguns currículos, enquanto não respondem, vou procurar outras opções."
    else:
        d "Posso atualizar o meu currículo e tentar umas vagas de emprego CLT."
    d "Acho que a Helena conhece alguns lugares para eu fazer um bico..."
    d "Também tem... {p} Naahhh..."
    d "..."
    d "Tá. Querendo ou não é uma opção..."
    d "Se eu não me engano, minha vizinha me contou sobre o trabalho sexual, poderia ver com ela para conseguir a renda extra que preciso."
    menu:
        d "Opito por qual desses caminhos?"

        
        "entregar currículos" if empregoDia2 == False:
                d "Vou atualizar meu currículo e entregar em algumas empresas."
                $confianca += 1
        "Procurar um bico":
            d "Vou convorsar com a Helena"

        "Se prostituir":
            d "Vou conversar com a vizinha."


# No 3 é obrigatório
# Vou tentar por ele falando com a amiga e a H fala de bico e levar mais currículos
# Aí faz a Diana lembrando da vizinha e q talvez prostituicao seja uma opção
    menu:
        "Trabalho {i}sério{/i}":
            d "Vou procurar um emprego formal, é mais estabilidade."

        "Bico":
            d "Talvez eu devesse procurar um bico."

        "Prostituição":
            d "Talvez eu devesse procurar um trabalho sexual."
    # escolhas parte da manhã
    menu:
        "Levar currículos no centro (-R$12 busão, +2 confiança)":
            $dinheiro -= 12
            $confianca += 2
            d "Gastei do busão, mas entreguei 5 currículos."

        "Fazer faxina pelo zap (+R$50, -1 confiança)":
            $dinheiro += 50
            $confianca -= 1
            d "Fiz faxina o dia todo. R$50, mas tô acabada."

        "Ir no CRAS se informar (+2 rede, +1 confiança)":
            $rede += 2
            $confianca += 1
            d "Tem curso do SENAC Delas com bolsa e tem a associação de mães da Andreia."

    # parte da tarde
    d "Como se eu tivesse dinheiro pra isso... Mas se eu me atrasar, o Elias vai me cobrar mais ainda..."

    menu:
        "Pagar mesmo que parcialmente":
            d "Vou pagar o que eu conseguir agora."

        "Pedir ajuda pra Andreia parcelar":
            a "Deixa que eu falo com ele, filha. Você me paga depois me ajudando com a Lili."

        "Descansar e organizar as ideias":
            d "Preciso respirar e pensar no que vou fazer."

    # capítulo 3
    a "Diana, amanhã vamos fazer 30 bolos de pote pra escola. Cada uma faz 10 e divide. Vem? Minha filha Lili vai amar ter você lá."

    h "Amiga! Consegui me inscrever no curso de Atendimento do SENAC Delas. Sabe que pra mim, mulher trans, é difícil arrumar trampo formal, mas esse curso tem parceria de emprego. Tem bolsa de R$300. Bora juntas? A gente se ajuda na prova."

    menu:
        "Aceitar convite da Andreia - Empreender em coletivo":
            d "Vou sim! Vai ser bom pra mim e pra Lili."
            # $confianca += 1
            # $rede += 1
            jump andreia

        "Aceitar convite da Helena - Curso com bolsa":
            d "Vou sim! Vai ser bom pra mim e pra Helena."
            # $confianca += 1
            # $rede += 1
            jump helena

        "Recusar os convites":
            d "Não vou. Preciso me organizar primeiro."
            # $confianca -= 1

    jump fim


#variações, cap 4

label andreia:
    a "Diana, cliente quer 50 bolos pra sábado, mas não temos batedeira grande."
    menu:
        "Aceitar convite da Andreia - Empreender em coletivo":
            d "Vou sim! Vai ser bom pra mim e pra Lili."
            #$confianca += 1
            #$rede += 1
            jump andreia

        "Aceitar convite da Helena - Curso com bolsa":
            d "Vou sim! Vai ser bom pra mim e pra Helena."
            #$confianca += 1
            #$rede += 1
            jump helena

        "Recusar os convites":
            d "Não vou. Preciso me organizar primeiro."
            #$confianca -= 1

    jump fim



label helena:
    h "Diana, tô nervosa. Se eu não passar, vão dizer que é porque sou trans. Mas se eu passar, mostro que a gente pode ocupar esses lugares."

    menu:
        "Estudar juntas na casa da Andreia":
            a "Lili faz o dever dela, vocês estudam. Eu faço café."

        "Helena fica doente de ansiedade, Diana vai sozinha e depois ensina ela":
            d "Tudo bem, Helena. Vou te ajudar."

        "As duas pedem pra professora fazer prova oral juntas":
            d "Ainda bem que essa prof é boasinha."

    jump fim

label fim:
    if dinheiro >= 700 and confianca >= 3 and rede >= 3:
        d "Consegui pagar o aluguel, fiz os bolos e passei na prova. Agora posso respirar."
    elif dinheiro < 700 and confianca >= 3 and rede >= 3:
        d "Não consegui pagar o aluguel, nem fazer os bolos e nem passar na prova. Mas vou continuar tentando."
    elif dinheiro >= 700 and confianca < 3 and rede >= 3:
        d "Consegui pagar o aluguel, mas não fiz os bolos e nem passei na prova. Mas vou continuar tentando."
    elif dinheiro >= 700 and confianca >= 3 and rede < 3:
        d "Consegui pagar o aluguel e fazer os bolos, mas não passei na prova. Mas vou continuar tentando."
    else:
        d "Não consegui nada. Mas vou continuar tentando."

    #"Nenhuma mulher nasce vulnerável. A vulnerabilidade é falta de oportunidade. Quando existe rede, curso e respeito, a história muda. Conheça projetos reais de Ribeirão Pires que inspiraram essa história."   n entendi se é alguém q fala ou se tem como n ser
    

    # This ends the game.
    return
