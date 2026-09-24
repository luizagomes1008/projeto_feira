# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
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
define h = Character("Helena")
image h hpadrao = "/images/personagens/hpadrao.png" 
image h hreceio ="images/personagens/hreceio.png"
image h hpadraobocaaberta ="images/personagens/hpadraobocaabera.png"
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
    linear 1.5 zoom 1.7
image a afeliz = "/images/personagens/afeliz.png" 
image a apadrao = "/images/personagens/apadrao.png"
image a apreocupada = "/images/personagens/apreocupada.png"
image a aalternativa = "/images/personagens/aalternativa.png"

define e = Character("Elias", color="#ff9933", what_italic=True)
image e epadrao = "images/personagens/epadrao.png"
define g = Character("Gerente Julio")
transform g_chegando:
    xalign 1.2
    yalign 1.0
    zoom 1.7
    linear 1:
        xalign 0.5
transform g_saindo:
    xalign 0.5
    yalign 1.0
    zoom 1.7
    linear 1.5:
        xalign -1.2
default dinheiro = 80
default rede = 0
default confianca = 0



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
    d "Mesmo que não seja muito..."
    pause 3.0
    d "Sinto que a qualquer momento o alarme vai-" #ai aqui o despertador iterrompe ela, e ela acorda, precisa adicionar o audio
    scene quarto_fundo with Dissolve(1.5) #with fade
    pause 2.0
    d"Que dor de cabeça"
    d"Preciso me arrumar para o trabalho, ou se não vou me atrasar"
    pause 1.0
    d"Da ultima vez que isso aconteceu não foi bom..."
    pause 2.0 # aqui adiciona um barulho de notificação
    d"Quem será?..."
    scene mesaquarto 
    
    d"Quem será agora?" #no celular vai ter uma mensagem do patrão dizendo que precisa conversar com ela
  #  d"hm... cobrança do alugel, não posso me atrasar com isso..."
   # d "Nem venceu ainda e já tá me cobrando!
    show celbloq at celular_maior
    pause 1.0
    show celmensagem at celular_maior
    pause 1.0
    d"Espero que tudo esteja bem..."
    pause 0.5
    scene dmente with fade
    pause 2
    scene banheiro  with fade
    d"Preciso lavar esse uniforme o quanto antes"
    pause 1.0
    show dpadrao #aqui eu vou desenhar ela se vendo no espelho com o uniforme, oq acham?
    d"Estou pronta"
    pause 5
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
    d"Ah, oi Andreia, estou bem! E sua filha, está tudo bem?"
    show a apreocupada
    a "Ala pegou uma gripe chata, tenho que passar na farmacia..."
    d"Coitadinha, já já ela se recupera"
    show a aalternativa
    a"Ah vc sabe como ela é, vai se recuperar rapido"
    pause 1.5
    show a apreocupada
    a"Devo estar te atrasando né?! Não me dei conta..."
    d"Relaxa andreia, estou no horário, mas é melhor indo"
    show a afeliz
    a"Bom trabalho querida, se cuida!"
    scene dmente with fade
    pause 2
    scene onibusmanha with  Dissolve(1) 
    pause 5
    scene dmente with fade
    pause 2
#no trabalho
    scene lanchonete1 with Dissolve(1)
    pause 1
    d"Cheguei"
    show h hirritada at h_chegando
    h "Diana!  por que não responde as mensagens que te mando?!"
    d"Bom dia pra você também Helena"
    show h holhofechado 
    h"Hm, bom dia"
    d"Para de ser chata amiga!"
    show h hirritada
    pause 1
    show h hrindo
    h"Chata é você!"
    pause 1
    show h hreceio
    h"Enfim, o patrão mandou você ficar depois do curso, quer conversar contigo..."
    d"Eu sei, ele me mandou mensagem hoje de manhã..."
    d"Talvez eu consiga o meu tão sonhado aumento"
    show h halternatica
    h"É verdade! Vamos nos manter positivas!"
    show h hpadraobocaaberta
    h"É melhor eu ir atender o caixa, logo logo isso aqui vai encher de gente"
    d"É mesmo, você tem razão, vou para a área de serviço..."
    scene dmente with fade
    pause 1
    scene banheirolanchonete with fade
    d"Eu espero realmente que seja apenas o aumento..."
    d"É melhor começar meu turno logo"
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
    d"Terminei meu turno, estou tão cansada..."
    g"Diana!"
    show e epadrao at g_chegando
    d"Ah! oi Julio"
    d"Você queria conversar comigo, não é?"
    g"Sim... bom..."
    pause 1.5
    g "Diana, movimento caiu. Estamos cortando gastos..."
    d"Como assim?..."
    g" Hoje foi seu último dia. Passa no caixa, obrigado."
    d"Julio espera! eu pos-"
    show e epadrao at g_saindo
    d"Ah não..."
    scene dmente with fade
    pause 0.5
#no caixa
    scene caixa with fade
    d "R$80. Só isso... E o aluguel dia 5... "
    d "Eita, já é hoje!"
    pause 1
    d"Eu vou dar um jeito... Já está tarde, melhor voltar para casa..."
    scene dmente with Dissolve(1) 
    scene onibusnoite with fade
    pause 1
    d"Não acredito nisso... Não sei o que vou fazer..."
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
    d"É melhor eu preparar algo para comer..."
    scene cozinha
    pause 0.5
    d"Vejamos..."
    scene geladeira
    pause 1
    d"Hhmmm..."
    d"Pizza serve"
    scene cozinha
    d"É melhor eu economizar mais do que antes"
    d"Estava indo bem naquele emprego... Que pena..."
    pause 1
    d"*bocejo*"
    d"Estou cansada, melhor ir dormir."
    scene quarton
    d"Amanhã eu penso melhor no que fazer, preciso descansar..."
    pause 1
    scene dmente with Dissolve(1) 
    pause 2.5 #celular despertando
    scene quarto_fundo with Dissolve(1) 
    pause 1
    d"*bocejo*"
    d"Quem está me ligando a essa hora da manhã?!"
    show celhelena at celular_menor
    d"Helena... "


#surge elias
    e "Ô Diana! Dia 5! R$650 do aluguel."
    d "Elias, fui mandada embora hoje. Me dá até dia 15? Por favor?"
    e "Dia 15 então. Mas vai pra R$700 com juros. Dia 15 eu volto."

#outro capitulo
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
