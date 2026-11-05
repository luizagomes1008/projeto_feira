# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image barhelenasorrindo = Transform("images/barHsorrindo.jpg", fit = "cover")
image barhelena = Transform("images/barHpadrao.jpg", fit = "cover")
image barhelenanervosa = Transform("images/barHrindo.jpg")
image barhelenapiscando = Transform("images/barHpiscando.jpg",  fit = "cover")
image barhelenapedindo = Transform("images/barHpedido.jpg", fit = "cover")
image barhelenasorrindol = Transform("images/barlanchesHsorrindo.jpg",  fit = "cover")
image barhelenal = Transform("images/barlanchesHpadrao.jpg", fit = "cover")
image barhelenanervosal = Transform("images/barlanchesHrindo.jpg", fit = "cover")
image barhelenapiscandol = Transform("images/barlanchesHpiscando.jpg", fit = "cover")

image farmaciacurr = Transform("images/farmacia.png", fit = "cover")
image lojaroupa = Transform("images/lojaroupa.png", fit = "cover")
image lojacell = Transform("images/lojacell.png", fit = "cover")
image mercado = Transform("images/supermercado.png", fit = "cover")
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
image kitnetporta = Transform("images/kitnetporta.png", fit = "cover")
image cras = Transform("images/cras.png", fit = "cover")
image bolo = Transform("images/bolos.png", fit = "cover")


define audio.tema_principal = "musicas/musicareflexiva.mp3"
define audio.musica_animada = "musicas/lofi.mp3"
define audio.musica_triste = "musicas/musicatriste.mp3"


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
image h hirritadau ="images/Personagens/HirritadaUniforme.png"
image h halternativau ="images/Personagens/HalternativaUniforme.png"
image h holhofechadou ="images/Personagens/HolhofechadoUniforme.png"
image h hreceiou ="images/Personagens/HreceioUnifome.png"
image h hrindou ="images/Personagens/HrindoUniforme.png"
transform h_saindo:
    xalign 0.5
    yalign 1.0
    zoom 1.7
    linear 1.5:
        xalign -1.5

define d = Character("Diana")
image dpadrao = "/images/Dpadrao.png" 

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
image e ealternativo = "/images/personagens/ealternativo.png"
image e ediscusao = "/images/personagens/ediscucao.png"
image e efalando = "/images/personagens/efalando.png"
image e eviradadeolho = "/images/personagens/eviradadeolho.png"
transform e_saindo:
    xalign 0.5
    yalign 1.0
    zoom 1.5
    linear 1.5:
        xalign 0.5
    


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
default dinheiro = 100
default rede = 0
default confianca = 0
default conversadiana = False
default empregoDia2 = False
default aluguelPago = False
default andreiaAjudaAluguel = False
default cursoSENAC = False
default vagaEncontrada = False
default trabalhoColetivo = False


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

    play music tema_principal fadein 2.0
   

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
    pause 1.3
    scene banheirouniforme with Dissolve(1)
    d"preciso lavar esse uniforme o quanto antes"
    d"estou pronta"
    stop music fadeout 2.0
    pause 2
    #saindo de casa
   # scene dmente with fade
    #pause 1.5
    
    play music musica_animada fadein 2.0
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
    a"bom trabalho querida, se cuida!"
    stop music fadeout 2.0
    scene dmente with fade
    pause 2
    scene onibusmanha with  Dissolve(1) 
    pause 5
    scene dmente with fade
    pause 2
#no trabalho
    scene lanchonete1 with Dissolve(1)
    play music tema_principal fadein 1.0
    pause 1
    d"Cheguei"
    show h hirritadau at h_chegando
    h "Diana! Por que não responde as mensagens que te mando?!"
    d"Bom dia pra você também Helena"
    show h holhofechadou
    h"Hm, bom dia"
    d"Para de ser chata amiga!"
    show h hirritadau
    pause 1
    show h hrindou
    h"Chata é você!"
    pause 1
    show h hreceiou
    h"Enfim, o patrão mandou você ficar depois do curso, quer conversar contigo..."
    d"Eu sei, ele me mandou mensagem hoje de manhã..."
    d"Talvez eu consiga o meu tão sonhado aumento"
    show h halternativau
    h"É verdade! Vamos nos manter positivas!"
    show h hrindou
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
    stop music fadeout 1.0
    scene lanchoneten
    d"terminei meu turno, estou tão cansada..."
    g"diana!"
    show g gpadrao at g_chegando
    d"ah! oi Julio"
    d"você queria conversar comigo, não é?"
    show g golhofechado 
    g"sim... bom..."
    pause 1.5
    play music musica_triste fadein 1.0
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
    d "R$100. Só isso... E o aluguel dia 5... Preciso pagar a outra metade "
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
    stop music fadeout 2.0
    scene dmente with Dissolve(1) 


#dia 2


    pause 2.5 #celular despertando
    scene quarto_fundo with Dissolve(1) 
    pause 1
    d"*bocejo*"
    d"Quem está me ligando a essa hora da manhã?!"
    show celhelena at celular_menor
    play music musica_triste fadein 1.0
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
        "Quero. Eu preciso desabafar.":
            $confianca += 2
            d "Eu tô com medo, Helena."
            show h hpadraobocaaberta
            d "Eu não sei se vou conseguir pagar o aluguel."
            h "Você não precisa resolver tudo hoje."
            h"um passo de cada vez, lembra?"

        "Não quero falar disso agora. ":
            d "Eu só quero esquecer isso por enquanto."
            h "Tudo bem..."
            $confianca -= 2

        "Não é tão grave assim.":
            d "Eu vou dar um jeito."
            h "Eu sei que vai. Mas você não precisa fingir que tá tudo bem comigo."
    show h hrindo 
    stop music fadeout 1.0
    play music musica_animada fadein 1.0
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
    # scene cafedamanha with Dissolve(1) 
    scene barhelena with fade
    #cena dela com a helena feliz na sua frente
    h"Fazia bastante tempo que não comemos aqui não é?"
    d"é verdade... Está diferente"
    h"costumávamos tomar o capuccino daqui depois das aulas, lembra?"
    d"com certeza, era tão gostoso"
    scene barhelenasorrindo
    #cena helena feliz alternativa
    h"bom, então já sei o que pedir para nós"
    h"o que acha de uma porção de pão de queijo para acompanhar?"
    d"parece realmente muito bom..."
    scene barhelenapiscando
    #cena helena piscadela
    h"ok, vou pedir!"
    scene barhelenapedindo
    #cena dela sozinha
    d"Estava com saudades de sair com Helena"
    d"Ela me faz muito bem..."
    scene dmente with fade
    pause 1
    scene barhelenal with fade 
    #cena delas com a comida na mesa
    h"prontinho, isso parece estar muito bom!"
    d"realmente, me lembra os tempos da escola."
    h "Você lembra quando a gente se conheceu?"
    d "Infelizmente."
    scene barhelenanervosal
    h "Nossa, vai começar..."
    d "Você derrubou café em mim."
    h "Foi sem querer!"
    d "Você falou que eu que estava no caminho."
    scene barhelenasorrindo
    h "E estava mesmo."
    d "Helena!"
    scene dmente with fade
    pause 1
    scene barhelena with fade
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
    show a apreocupada
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
            scene dmente with Dissolve(1)
            scene farmaciacurr with fade
            pause 1.5
            scene dmente with fade
            scene lojaroupa with fade
            pause 1.5
            scene dmente with fade
            scene mercado with fade
            pause 1.5
            scene dmente with fade
            scene lojacell with fade
            pause 1.5
            scene dmente with fade
            scene onibusnoite with Dissolve(1)
            h "O dia foi cheio hoje hein!"
            d "realmente, estou morrendo de sono"
            pause 1 
            scene dmente with Dissolve(1)
            scene kitnetn with Dissolve (1)
            show h hpadrao at h_chegando
            pause 1
            d "obrigada por me ajudar hoje Helena, de verdade"
            show h hrindo at h_centro
            h"você sabe que pode sempre contar comigo nao é Diana?"
            d"com seu apoio tudo fica mais leve"
            show h halternatica at h_centro
            h "nesse ritmo você vai encontrar uma vaga rapidinho!"
            d"que assim seja!"
            show h hrindo at h_centro
            h"boa noite Diana, dorme bem"
            d"boa noite miga, obrigada mais uma vez"
            show h hpadraobocaaberta at h_saindo
            pause 1
            scene dmente with Dissolve(1)
            scene dmente 
            pause 1
            scene dmente with Dissolve(1)
            scene quarton with fade
            pause 1
            d"amanhã as coisas vão melhorar, sinto isso"
            scene dmente with Dissolve(1)
            pause 1
        
     
        "Prefiro descansar um pouco":
            d "Acho que preciso de um tempo para colocar a cabeça no lugar."
            h "E tudo bem."
            d "Eu só queria esquecer tudo por algum tempo."
            show h holhofechado
            h "Então hoje você vai descansar. Amanhã a gente pensa no resto."
            d"obrigada por me apoiar Helena"
            show h hpadraobocaaberta
            h"você pode sempre contar comigo!"
            show h hrindo
            h"que tal passarmos a tarde maratonando nossa série favorita?"
            d "isso me parece ótimo"
            pause 1
            scene dmente with Dissolve(1)
            scene dmente
            pause 2
            scene dmente with Dissolve(1)
            scene salan with Dissolve(1)
            show h hpadraobocaaberta at h_centro with fade
            h"já está tarde, é melhor eu ir"
            d"ta bom amiga, se cuida"
            h"amanhã pensaremos melhor!"
            d"obrigada por passar esse tempo comigo"
            show h hrindo
            h"eu que agradeço miga!"
            show h hpadraobocaaberta
            h"bom, já vou indo, boa noite Diana!"
            d"Boa noite helena! Dorme bem"
            show h hpadrao at h_saindo
            scene dmente with Dissolve(1)
            scene quarton with Dissolve(1)
            pause 1
            d"amanhã as coisas vão melhorar, sinto isso"
            scene dmente with Dissolve(1)
            scene dmente with Dissolve(1)
            pause 1



        "Não sei o que quero fazer":
            $ confianca -= 1
            d "Sinceramente? Eu não faço ideia."
            h "Você não precisa ter todas as respostas agora."
            d "Tenho medo de escolher errado."
            show h hpadraobocaaberta 
            h "Às vezes, não escolher nada por enquanto também é uma escolha."
            d "Você sempre sabe o que falar, né?"
            show h halternatica
            h "Nem sempre. Só finjo que sei."
            d "Boba."
            h "Sua boba."
            show h hrindo
            h"que tal passarmos a tarde maratonando nossa série favorita?"
            d "isso me parece ótimo"
            pause 1
            scene dmente with Dissolve(1) #aqui por algum motivo o cenario se repete :/
            pause 2
            scene salan with Dissolve(1)
            show h hpadraobocaaberta at h_centro with fade
            h"já está tarde, é melhor eu ir"
            d"ta bom amiga, se cuida"
            h"amanhã pensaremos melhor!"
            d"obrigada por passar esse tempo comigo"
            show h hrindo
            h"eu que agradeço miga!"
            show h hpadraobocaaberta
            h"bom, já vou indo, boa noite Diana!"
            d"Boa noite helena! Dorme bem"
            show h hpadrao at h_saindo
            scene dmente with Dissolve(1)
            scene quarton with Dissolve(1)
            pause 1
            d"amanhã as coisas vão melhorar, sinto isso"
            scene dmente with Dissolve(1)
            scene dmente with Dissolve(1)
            pause 1


#Dia 3
    pause 2.5 #celular despertando
    scene quarto_fundo with Dissolve(1) 
    pause 1
    d"*bocejo*"
    scene banheiro
    scene cozinha
    scene salam
    d "Tá... vamos ver as contas"
    d "Tenho [dinheiro] e preciso pagar R$350 do aluguel e comprar mais comida..."
    d "Não vai ser o suficiente... \n Dia 15 já já está aí... "
    d "Tenho que procurar uma forma de ganhar dinheiro... {p} Mas qual?"
    if empregoDia2 == True:
        d "Ontem já entreguei alguns currículos, enquanto não respondem, vou procurar outras opções."
    else:
        d "Posso atualizar o meu currículo e tentar umas vagas de emprego CLT."
    d "Acho que a Helena conhece alguns lugares para eu fazer um bico..."
    #surge elias
    e "Ô Diana! "
    d"ah não, o aluguel..."
    scene kitnetporta with fade
    show e epadrao at h_centro
    pause 1
    d "Elias, fui mandada embora hoje. Me dá até dia 15? Por favor?"
    show e ediscusao
    e "Já se passaram dois dias Diana, nao tolelarei mais."
    show e epadrao
    d"por favor seu Elias, me dê ao menos 5 dias"
    show e ealternativo
    e"3 dias Diana, nada mais!"
    show e epadrao at h_saindo
    d"ah não..."
    scene salam with fade
    pause 1
    if confianca < 1:
        d "Eu nem sei se consigo pedir ajuda para alguém..."
        d "Mas talvez seja melhor tentar do que ficar parada."
    else:
        d "Preciso pensar nas possibilidades que ainda tenho."
    menu:
        d "Opito por qual desses caminhos?"

        
        "entregar currículos" if empregoDia2 == False:
                $ confianca += 1
                d "Vou atualizar meu currículo e entregar em algumas empresas."
                d "Vou perguntar para a Helena sobre lugares para  mandar meu currículo"
                d "hoje mesmo"
                show celhelena at celular_menor
                d "Helena, você sabe aonde eu posso levar meu currículo?"
                h "Ah sim! vou te passar os endereços"
                d "Obrigada, Helena, De verdade."
                h "Conte comigo sempre amiga!"
                hide celhelena
                scene dmente with Dissolve(1) 
                pause 1
                d "Já atualizei meu currículo... Não é dos melhores mas preciso de emprego logo"
                scene onibusmanha with Dissolve(1) 
                pause 1
                d "Mas estoou confiante! Passando em 5 lugares tenho mais chances"
                $confianca += 2
                pause 3
                scene dmente with Dissolve(1)
                scene farmaciacurr with fade
                pause 1.5
                scene dmente with fade
                scene lojaroupa with fade
                pause 1.5
                scene dmente with fade
                scene mercado with fade
                pause 1.5
                scene dmente with fade
                scene lojacell with fade
                pause 1.5
                scene dmente with fade
                scene onibusnoite with Dissolve(1)
                d "Consegui ir em varios lugares."
                d "Mas agora estou morrendo de sono"
                pause 1 
                scene dmente with Dissolve(1)
                scene kitnetn with Dissolve (1)
                pause 1
                show celhelena at celular_menor
                d "Obrigada por me ajudar hoje Helena, não sabia nem por onde começar"
                h"Você sabe que pode sempre contar comigo nao é Diana?"
                d"Você sempre me ajuda e tudo fica mais fácil"
                h "Nesse ritmo você vai encontrar uma vaga rapidinho!"
                d "Espero que sim!"
                h"boa noite Diana, dorme bem"
                d"boa noite miga, obrigada mais uma vez"
                hide celhelena
                pause 1
                scene dmente with Dissolve(1)
                scene dmente 
                pause 1
                scene dmente with Dissolve(1)
                scene quarton with fade
                pause 1
                d"amanhã as coisas vão melhorar, sinto isso"
                scene dmente with Dissolve(1)
                pause 1


        "Procurar um bico":
            d "Bom, acho que por agora é melhor fazer algo simples e rápido..."
            d "Vou convorsar com a Helena"
            d "Talvez ela saiba de alguém que precise de ajuda com algo, como fazer uma faxina"
            show celhelena at celular_menor
            h "Eu conheço uma faxineira, talvez você possa de oferecer para ajudar ela e receber parte do dinheiro"
            h "Oque você acha?"
            d "É melhor que nada... preciso de dinheiro rápido"
            hide celhelena
            pause 1
            scene banheirouniforme with fade
            d "de pouco em pouco vou me erguer"
            scene onibusmanha with Dissolve(1) 
            pause 1
            scene dmente with Dissolve(1)
            d "Passei o dia todo ajudando a faxineira..."
            $dinheiro += 80
            $confianca -= 1
            scene quarton with fade
            pause 1
            d "Fiquei muito cansada, não sei se trabalhar com isso é pra mim..."
            d "Pelo menos consegui 80 reais"
            d "por agora tenho [dinheiro] reais"
            d "Amanhã vejo oque faço..."
            scene dmente with Dissolve(1)
            pause 1


        "Conversar com Andreia":
            $ conversadiana = True
            d "Talvez eu devesse conversar com a Andreia..."
            d "Ela conhece bastante gente por aqui."
            d "Não custa tentar, né?"
            scene dmente with Dissolve(1)
            pause 1
            scene kitnet with Dissolve(1)
            show a apreocupada at a_entrando_direita
            a "Diana? Precisa de alguma coisa? Você parece preocupada."
            d "Andreia... eu tô precisando de dinheiro."
            d "Fui mandada embora e não sei muito bem por onde começar."
            show a aalternativa
            a "Ah, minha filha... sinto muito."
            show a apadrao
            a "Mas olha, talvez eu consiga te ajudar com algumas coisas."
            d "Sério? Como?"
            a "Você já ouviu falar dos cursos gratuitos que oferecem por aqui?"
            a "Tem algumas iniciativas para mulheres que estão procurando emprego."
            d "Não sabia disso..."
            show a afeliz
            a "Também conheço umas mulheres que fazem doces para vender."
            a "Às vezes aparece bastante encomenda. Poderia ser uma renda extra."
            d "Eu não tinha pensado nisso..."

            a " tem o CRAS também. Lá você pode se informar sobre os programas de assistência e outras oportunidades."

            d "Parece que existem mais possibilidades do que eu imaginava."
            show a apadrao
            a "Claro que existem, Diana. Você não precisa enfrentar tudo sozinha."

            d "Obrigada, Andreia. De verdade."
            hide a
            scene dmente with Dissolve(1)
            pause 1

            d "Depois de conversar com Andreia, comecei a pensar em tudo que ela me contou."
            d "Talvez eu não estivesse tão sem opções quanto imaginava."

            scene onibusmanha with Dissolve(1)
            pause 2

            scene kitnetn with Dissolve(1)
            pause 1

            d "O restante do dia passou enquanto eu tentava organizar minhas ideias."
            d "Anotei os endereços dos cursos e os contatos que Andreia me passou."
            scene black with fade
            pause 1.5
            scene quarton with fade
            d "Já estava ficando tarde. Amanhã seria um novo dia."
            scene dmente with Dissolve (1)
            pause 1

# DIA 4

    pause 2.5
    scene quarto_fundo with Dissolve(1)
    pause 1

    d "Mais um dia..."

    scene banheirouniforme with fade
    pause 1

    scene salam with fade
    pause 1

    d "Preciso pensar no que fazer hoje."
    d "Não posso continuar dependendo apenas dos poucos reais que tenho."
    show celhelena at celular_menor
    h "Bom dia, amiga! Como você está?"
    d "Bom dia, Helena. Estou tentando pensar no que fazer hoje."
    h "Olha, lembrei de uma coisa que pode te ajudar."
    h "Você já ouviu falar do CRAS? Acho que Andreia já mecionou, lá você pode conseguir informações sobre programas de assistência e oportunidades."
    h "Também existem cursos profissionalizantes gratuitos por aqui."
    d "Nossa, eu nem sabia que tinha tudo isso, pode me ajudar bastante."
    h "Pois é! Acho que vale a pena dar uma olhada."
    d "Obrigada por lembrar de mim, Helena."
    hide celhelena
    if conversadiana == True:
        d "Além disso, Andreia tinha comentado sobre algumas mulheres que trabalham com produção de doces."
        d "Talvez eu consiga uma oportunidade com elas."
    else:
        d "Preciso encontrar alguma maneira de conseguir uma renda extra."
        d "Talvez seja uma boa ideia organizar meu currículo e procurar outras oportunidades."

    menu:
        d "O que devo fazer hoje?"
        "Buscar ajuda do CRAS e conhecer cursos profissionalizantes":
            d "Acho que começar buscando informações pode ser uma boa ideia."
            d "Vou tentar descobrir quais programas e cursos estão disponíveis."
            scene dmente with Dissolve(1)
            pause 1

            scene onibusmanha with Dissolve(1)
            pause 2

            d "Espero encontrar alguma oportunidade por lá."
            scene cras with fade 
            pause 1.5
            scene dmente with Dissolve(1)
            pause 1

            d "Consegui algumas informações sobre os programas de assistência."
            d "Também descobri algumas possibilidades de cursos gratuitos."

            $ rede += 2
            $ confianca += 1

            scene onibusnoite with Dissolve(1)
            pause 2

            scene quarton with fade
            d "Pelo menos hoje consegui descobrir que existem pessoas e lugares dispostos a ajudar."
            d "Talvez eu esteja começando a encontrar um caminho."

        "Ajudar Andreia na produção de doces" if conversadiana == True:
            d "Andreia comentou sobre algumas confeiteiras que precisam de ajuda."
            d "Pode ser uma boa oportunidade para conseguir uma renda."

            scene dmente with Dissolve(1)
            pause 1

            scene onibusmanha with Dissolve(1)
            pause 2

            d "Tomara que dê tudo certo."

            scene dmente with Dissolve(1)
            pause 1
            scene bolo with fade
            pause 1.5
            scene onibusnoite with Dissolve(1)
            d "As mulheres foram muito receptivas comigo."
            d "Passei boa parte do dia ajudando na preparação dos doces."
            d "Foi cansativo, mas gostei de trabalhar em equipe."
            pause 1.5
            scene kitnetn with Dissolve(1)

            $ rede += 1
            $ confianca += 1
            $ dinheiro += 150

            scene quarton with fade
            d "Foi um dia produtivo."
            d"as amigas da Andreia me anteciparam 150 reais, estou muito feliz"
            d"tenho [dinheiro] reais"
            d "Quem sabe isso não se transforma em uma oportunidade maior?"

        "Organizar meu currículo e procurar novas vagas":
            d "Acho que preciso continuar tentando encontrar um emprego."
            d "Vou conversar com Helena e pedir algumas indicações."

            show celhelena at celular_menor

            d "Helena, você conhece algum lugar que esteja contratando?"
            h "Posso procurar algumas oportunidades e te mandar."
            h "Não desiste, amiga. Uma hora vai aparecer alguma coisa."
            d "Espero que sim."

            hide celhelena

            scene dmente with Dissolve(1)
            pause 1

            d "Passei boa parte do dia pesquisando vagas e atualizando meu currículo."
            d "Ainda não consegui nada, mas pelo menos estou tentando."

            scene onibusnoite with Dissolve(1)
            pause 2

            scene quarton with fade
            d "Amanhã vou continuar procurando."

        "Tentar conciliar a produção de doces e os cursos" if conversadiana == True and confianca > 2:
            d "Talvez eu não precise escolher apenas uma possibilidade."
            d "Posso ajudar na produção de doces e também procurar me qualificar."
            scene dmente with Dissolve(1)
            pause 1
            scene onibusmanha with Dissolve(1)
            pause 2
            d "Vou começar ajudando com os doces."
            scene dmente with Dissolve(1)
            pause 1
            scene bolo with fade
            pause 1
            d "Depois, vou aproveitar para buscar informações sobre os cursos disponíveis."
            pause 1.5
            scene onibusmanha with Dissolve(1)
            pause 2
            scene cras with fade
            pause 1.5
            scene onibusnoite with Dissolve(1)
            d "Foi bastante coisa para um único dia..."
            d "Mas sinto que estou começando a construir novas possibilidades."
            pause 1.5
            scene dmente with Dissolve(1)
            scene kitnetn with fade
            pause 1
            $ rede += 2
            $ confianca += 2
            scene quarton with fade
            d "Estou cansada, mas feliz por não ter desistido."

# ============================================================
# DIA 5 - NOVAS POSSIBILIDADES
# ============================================================

label dia5:

    play music tema_principal fadein 2.0

    scene dmente with Dissolve(1.5)

    pause 2.0

    d "O despertador tocou cedo naquela manhã."
    d "Por alguns segundos, esqueci que não precisava mais ir trabalhar."

    pause 1.0

    d "É estranho... Passei tanto tempo reclamando da rotina."
    d "Agora, sinto falta até dela."

    scene banheiro with fade

    d "Preciso parar de pensar no que perdi."
    d "Ainda tenho algumas possibilidades."

    scene mesaquarto with Dissolve(1.0)

    pause 1.0

    d "Vamos ver..."

    # --------------------------------------------------------
    # CELULAR - HELENA
    # --------------------------------------------------------

    show celhelena at celular_menor

    h "Diana, bom dia!"
    h "Você lembra que te falei do curso do SENAC Delas?"

    d "Lembro. Você conseguiu mais informações?"

    h "Consegui! As inscrições estão abertas."
    h "E existe uma bolsa de apoio de R$300 para algumas participantes."

    d "R$300? Isso ajudaria bastante..."

    h "Além disso, o curso tem parceria com empresas."
    h "Não é garantia de emprego, mas pode abrir algumas portas."

    d "Eu tenho medo de começar algo e não conseguir terminar."

    h "Você não precisa decidir tudo de uma vez."
    h "Só queria que soubesse que essa oportunidade existe."

    hide celhelena

    pause 1.0

    d "Um curso... um trabalho... ou continuar tentando conseguir dinheiro rápido."

    d "Eu preciso escolher com cuidado."

    menu:

        "O que Diana decide fazer hoje?"

        "Participar da produção de doces com Andreia":

            d "Acho que consigo trabalhar com as mulheres da associação."
            d "Pelo menos já conheço um pouco desse ambiente."

            scene onibusmanha with Dissolve(1.0)

            pause 2.0

            scene bolo with fade

            pause 1.0

            d "Hoje precisamos preparar as encomendas para a escola."

            "Diana se juntou às outras mulheres."
            "Enquanto trabalhavam, conversavam sobre suas vidas, dificuldades e planos."

            d "É curioso..."
            d "Cada uma de nós tem uma história diferente."

            d "Mas parece que, quando estamos juntas, as coisas ficam um pouco menos difíceis."

            pause 1.5

            scene kitnetn with Dissolve(1.0)

            $ dinheiro += 100
            $ rede += 2
            $ confianca += 1
            $ trabalhoColetivo = True

            d "Recebi R$100 pelo trabalho de hoje."
            d "Não é muito, mas foi conquistado com meu próprio esforço."

            d "E, pela primeira vez em alguns dias, não me senti tão perdida."

        "Inscrever-se no curso do SENAC Delas":

            d "Talvez seja hora de tentar algo diferente."
            d "Não quero apenas sobreviver. Quero ter outras oportunidades."

            scene onibusmanha with Dissolve(1.0)

            pause 2.0

            scene cras with fade

            pause 1.0

            "Diana foi buscar informações sobre a inscrição e os programas de apoio."

            "Após receber as orientações, Diana conseguiu realizar sua inscrição."

            scene dmente with Dissolve(1.0)
            scene onibusmanha with fade

            d "Pronto. Agora é esperar pelas próximas etapas."

            show celhelena at celular_menor

            h "E aí? Conseguiu?"

            d "Consegui me inscrever!"

            h "Eu sabia que você ia tentar."

            d "Ainda estou nervosa."

            h "Nós podemos estudar juntas quando as aulas começarem."

            d "Obrigada, Helena."

            hide celhelena

            $ cursoSENAC = True
            $ rede += 2
            $ confianca += 2

            scene salam with fade

            d "Hoje não consegui dinheiro..."
            d "Mas talvez tenha conseguido algo que valha ainda mais no futuro."

        "Continuar procurando emprego":

            d "Eu preciso de uma renda fixa."
            d "Não posso depender apenas de trabalhos temporários."

            scene onibusmanha with Dissolve(1.0)

            pause 2.0

            scene farmaciacurr with fade

            pause 1.0

            d "Mais um currículo entregue."

            scene dmente with fade

            scene lojaroupa with fade

            pause 1.0

            d "Espero que alguém entre em contato."

            scene dmente with fade

            scene mercado with fade

            pause 1.0

            d "É cansativo procurar emprego sem saber se alguém vai responder."

            scene dmente with fade

            scene lojacell with fade

            pause 1.0

            d "Mas não posso desistir."

            scene onibusnoite with Dissolve(1.0)

            pause 2.0

            scene kitnetn with fade

            d "Passei o dia inteiro procurando vagas."

            pause 1.0

            "Ao chegar em casa, Diana recebeu uma mensagem."

            show celmensagem at celular_maior

            pause 1.0

            d "Uma entrevista..."

            d "Não é um emprego ainda, mas é uma oportunidade."

            hide celmensagem

            $ vagaEncontrada = True
            $ confianca += 2

            d "Amanhã preciso me preparar."


    scene mesaquarto with fade

    pause 1.0

    d "Antes de pensar no amanhã, preciso resolver o aluguel."

    d "R$350..."

    d "Quanto dinheiro eu tenho agora?"

    d "Tenho R$[dinheiro]."

    pause 1.0

    if dinheiro >= 350:

        d "Eu finalmente tenho o suficiente."

        menu:

            "O que Diana faz?"

            "Pagar o aluguel":

                d "Não quero adiar isso mais uma vez."

                $ dinheiro -= 350
                $ aluguelPago = True

                scene kitnetporta with fade

                show e epadrao at h_centro

                e "Diana?"

                d "Seu Elias. Eu consegui o dinheiro do aluguel."

                show e eviradadeolho

                e "Certo. Pelo menos resolveu essa pendência."

                d "Obrigada por ter me dado mais alguns dias."

                show e epadrao at h_saindo

                pause 1.0

                hide e

                scene salam with fade

                d "Pronto."

                d "Uma preocupação a menos."
                scene dmente with Dissolve(1)
                scene mesaquarto with fade
                d"já nao preciso me preocupar pelo resto do mês com o aluguel"
                d"mas isso também não significa que tenho que ficar parada, vou procurar vagas de emprego pela internet"
                d"pelo resto do dia!"

                $ confianca += 2

            "Guardar o dinheiro para outras necessidades":

                d "Eu preciso pensar na comida e nas outras contas também."

                d "Talvez eu consiga pagar depois."

                $ aluguelPago = False

                d "Mas isso significa que ainda tenho uma dívida."
                scene dmente with Dissolve(1)
                scene mesaquarto with fade
                d"bom, tenho dinheiro para o resto do mês, mas preciso pensar no aluguel"
                d"vou procurar vagas de emprego pela internet"
                d"pelo resto do dia!"

    else:

        d "Ainda não consegui juntar o suficiente."

        $ valorFaltante = 350 - dinheiro

        d "Faltam R$[valorFaltante]."

        pause 1.0

        d "Eu poderia tentar pedir ajuda..."

        scene kitnet with fade

        show a apreocupada at a_entrando_direita

        a "Diana? Você parece preocupada."

        d "Andreia, eu ainda não consegui pagar o aluguel."

        show a aalternativa

        a "Quanto está faltando?"

        d "R$[valorFaltante]."

        show a apreocupada

        a "Eu posso te ajudar com o que falta."

        d "Mas Andreia, você já tem tantas coisas para cuidar..."

        show a apadrao

        a "Diana, eu não estou oferecendo porque acho que você não consegue."

        a "Estou oferecendo porque sei que essa situação é difícil."

        a "E porque, quando a gente pode ajudar alguém, não precisa esperar essa pessoa chegar ao limite."

        menu:

            "Diana aceita a ajuda de Andreia?"

            "Aceitar":

                d "Eu aceito. Obrigada, Andreia."

                show a afeliz

                a "Não precisa agradecer tanto."

                d "Eu vou me organizar para não ficar nessa situação novamente."

                a "Eu sei que vai."

                $ dinheiro += valorFaltante
                $ dinheiro -= 350
                $ aluguelPago = True
                $ andreiaAjudaAluguel = True
                $ rede += 2
                $ confianca += 1

                d "Consegui pagar o aluguel."

                d "Não foi sozinha... mas consegui."
                scene dmente with Dissolve(1)
                scene mesaquarto with fade
                d"já nao preciso me preocupar pelo resto do mês com o aluguel"
                d"mas isso também não significa que tenho que ficar parada, vou procurar vagas de emprego pela internet"
                d"pelo resto do dia!"

            "Recusar":

                d "Eu agradeço muito, mas quero tentar conseguir o restante."

                show a apreocupada

                a "Tudo bem, Diana."

                a "Só não quero que você pense que precisa enfrentar tudo sozinha."

                $ aluguelPago = False
                $ confianca += 1
                scene dmente with Dissolve(1)
                scene mesaquarto with fade
                d"ainda tenho a dívida do aluguel, mas nao vou me aborrecer facilmente"
                d"vou procurar vagas de emprego pela internet"
                d"pelo resto do dia!"
            

        hide a

    scene quarton with fade

    pause 1.0

    d "O dia foi longo."

    if aluguelPago == True:

        d "Pelo menos o aluguel está resolvido."

    else:

        d "Ainda tenho uma pendência para resolver."

    if cursoSENAC == True:

        d "Também consegui me inscrever no curso."
        d "Talvez essa seja uma oportunidade de mudar minha vida."

    if vagaEncontrada == True:

        d "A entrevista de emprego será amanhã."
        d "Preciso me preparar."

    if trabalhoColetivo == True:

        d "Gostei de trabalhar com as mulheres da associação."
        d "Talvez eu possa continuar ajudando."

    pause 1.5

    d "Não sei exatamente como será o futuro."

    d "Mas hoje consegui dar mais um passo."

    stop music fadeout 2.0

    scene dmente with Dissolve(1.0)

    pause 2.0

    jump dia6


label dia6:

    play music tema_principal fadein 2.0

    scene quarto_fundo with Dissolve(1.5)

    pause 1.0

    d "Sexto dia."

    d "Parece que faz muito mais tempo desde que fui demitida."

    d "Tanta coisa aconteceu em tão pouco tempo."

    scene banheiro with fade

    pause 1.0

    d "Eu não sei se tudo vai dar certo."

    d "Mas acho que finalmente entendi uma coisa."

    d "Recomeçar não significa voltar ao ponto de partida."

    d "Significa continuar, mesmo depois de tudo mudar."

    scene salam with fade

    if vagaEncontrada == True:

        d "Hoje é o dia da entrevista."

        pause 1.0
        scene banheirodianaemprego #aqui colocar o bg dela normal no espelho
        scene onibusmanha with Dissolve(1.0)

        pause 2.0

        scene farmaciacurr with fade

        pause 1.0

        d "Eu consegui chegar."

        d "Estou nervosa, mas vou tentar."
        scene dmente with fade

        "A entrevista foi breve."
        "Diana respondeu às perguntas e explicou sua experiência na lanchonete."

        pause 1.0
        scene onibusmanha with Dissolve(1)

        d "Agora só preciso esperar."

        $ confianca += 1

    elif cursoSENAC == True:

        d "Hoje preciso organizar os documentos para o curso."

        pause 1.0

        scene onibusmanha with Dissolve(1.0)

        pause 2.0

        scene cras with fade

        pause 1.0

        d "Consegui confirmar as informações da inscrição."

        d "Ainda tenho muito o que aprender."

        d "Mas estou disposta a tentar."

        $ confianca += 1

    elif trabalhoColetivo == True:

        d "Andreia comentou que a associação recebeu novas encomendas."

        d "Talvez eu possa ajudar novamente."

        scene onibusmanha with Dissolve(1.0)

        pause 2.0

        scene bolo with fade

        pause 1.0

        d "As mulheres já estão trabalhando."

        d "É bom ver que esse projeto está crescendo."

        "Diana ajudou a organizar as encomendas e a produção."

        $ dinheiro += 80
        $ rede += 1
        $ confianca += 1
        scene onibusnoite with Dissolve (1)
        pause 2.5
        scene kitnetn with fade
        pause 1

        d "Consegui mais R$80."

        d "Aos poucos, estou construindo alguma estabilidade."

    scene cozinha with fade
    d"vou preparar algo para comer"
    "toc toc"
    h"diana sou eu, abre aqui"
    scene kitnetporta
    show h hpadrao at h_centro with dissolve
    d"oi amiga, que surpresa"
    show h hrindo
    h"trouxe lanche! Vamos para a cozinha"
    d"vamos!"
    show h h_saindo
    pause 1
    scene cozinha with fade
    show h hpadrao at h_centro with Dissolve

    h "Diana, como foi seu dia?"

    d "Foi bom. Acho que estou começando a encontrar um caminho."
    show h halternatica

    h "Fico feliz em ouvir isso."

    d "Eu ainda tenho medo de não conseguir."
    show h hpadraobocaaberta
    h "Acho que todo mundo sente isso em algum momento."

    h "Mas você não precisa ter tudo resolvido agora."

    d "Obrigada, Helena."
    show h halternatica
    h "E quando eu começar o curso, você vai estudar comigo, hein?"

    d "Se eu conseguir entrar, com certeza."
    show h hrindo

    h "Você consegue."
    hide h with fade

    scene dmente with Dissolve(1)

    pause 2


    scene kitnet with fade

    pause 1.0

    d "Quando tudo aconteceu, eu achei que tinha perdido tudo."
    scene lanchonete with fade
    d "Meu emprego."
    scene kitnetporta with fade
    d "Minha segurança."
    scene banheirodianaemprego with fade
    d "Minha rotina."
    scene dmente with fade
    pause 1.0

    d "Mas também encontrei pessoas que me ajudaram."
    show h halternatica at h_vai_esquerda with dissolve
    show a afeliz at a_entrando_direita with dissolve
    d "Helena, Andreia..."
    d "E todas aquelas mulheres que me mostraram que eu não precisava enfrentar tudo sozinha."
    hide a 
    hide h

    pause 1.5

    d "Ainda tenho muito pela frente."
    
    d "Talvez eu consiga um novo emprego."
    d "Talvez eu termine um curso."
    d "Talvez eu encontre uma forma de viver do meu próprio trabalho."
    show d dpadrao at h_centro with dissolve
    pause 1.5

    d "Eu não sei."

    d "Mas, pela primeira vez, não sinto que meu futuro está completamente fechado."
    hide d

    scene dmente with Dissolve(2.0)

    pause 2.0

    jump fim

label fim:

    scene dmente with fade

    pause 1.0

    if aluguelPago == True and confianca >= 3 and rede >= 3:

        d "Consegui pagar o aluguel e construir uma rede de apoio."

        d "Ainda não tenho todas as respostas."

        d "Mas agora sei que posso recomeçar."

        "FINAL: UM NOVO COMEÇO"

    elif aluguelPago == True:

        d "Consegui pagar o aluguel."

        d "Ainda preciso encontrar estabilidade e novas oportunidades."

        d "Mas pelo menos consegui resolver uma das minhas maiores preocupações."

        "FINAL: UM PASSO DE CADA VEZ"

    elif cursoSENAC == True and rede >= 3:

        d "Ainda não consegui resolver todas as minhas dificuldades."

        d "Mas consegui me inscrever em um curso e encontrei pessoas dispostas a me apoiar."

        d "Talvez essa seja a oportunidade que eu precisava."

        "FINAL: NOVAS OPORTUNIDADES"

    elif trabalhoColetivo == True and rede >= 3:

        d "Ainda tenho dificuldades financeiras."

        d "Mas encontrei uma forma de trabalhar e construir algo junto de outras mulheres."

        d "Talvez juntas possamos ir mais longe."

        "FINAL: FORÇA COLETIVA"

    else:

        d "Ainda não consegui resolver tudo."

        d "O aluguel continua sendo uma preocupação."

        d "Mas não quero desistir."

        d "Amanhã será mais um dia para tentar."

        "FINAL: CONTINUAR TENTANDO"

    pause 2.0

    scene black with fade

    pause 1.5
    #aqui a gente coloca um fundo especial, uma foto delas, sla
    "Nenhuma mulher nasce vulnerável."
    "A vulnerabilidade também é resultado da falta de oportunidades."
    "Quando existe apoio, acesso e respeito, novas histórias podem começar."

    pause 2.0

    return
