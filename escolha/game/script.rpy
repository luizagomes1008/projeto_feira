# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Diana")

image dmente = Transform("images/menteD.png", fit ="cover")
image quarto_fundo = Transform(
    "images/quarto.png",
    xysize=(config.screen_width, config.screen_height)
)
image mesaquarto = Transform(
    "images/mesaquarto.png",
    xysize=(config.screen_width, config.screen_height)
)

image m ="/images/segurandocelular.jpg"
define h = Character("Helena")
image Hpadrao = "/images/Hpadrao.jpeg"
image Hrindo = "/images/Hrindo.jpeg"


define a = Character("Andreia", color="#66ccff")
define e = Character("Elias", color="#ff9933", what_italic=True)
define g = Character("Gerente")
default dinheiro = 80
default rede = 0
default confianca = 0



# The game starts here.

label start:    
    scene dmente

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    pause 2.0
    d "Meu nome é Diana. Tenho 26 anos."
   

    d "Tenho uma vida como qualquer outra pessoa teria nessa situação..."
    d "Mas algumas escolhas podem mudar completamente o nosso caminho."
    pause 2.0
    d "Há dois anos que trabalho nesse emprego... É o que me sustenta."
    d "É de onde eu tiro o pão de cada dia, o copo d'água."
    d "É também muito cansativo... Mas não posso reclamar."
    pause 3.0
    d "sinto que a qualquer momento o alarme vai-" #ai aqui o despertador iterrompe ela, e ela acorda, precisa adicionar o audio
    scene quarto_fundo 
    pause 2.0
    d"que dor de cabeça"
    d"preciso me arrumar para o trabalho, ou se não vou me atrasar"
    pause 1.0
    d"da ultima vez que isso aconteceu não foi bom..."
    pause 2.0 # aqui adiciona um barulho de notificação
    d"quem será?..."
    scene mesaquarto
    d"hm... cobrança do alugel, não posso me atrasar com isso..."
    d "Nem venceu ainda e já tá me cobrando!"
    show m
    pause 1.0
#no trabalho
    g "Diana, movimento caiu. Hoje é seu último dia. Passa no caixa."
#no caixa
    d "R$80. Só isso. E o aluguel dia 15..."
#surge elias
    e "Ô Diana! Dia 5! R$650 do aluguel."
    d "Elias, fui mandada embora hoje. Me dá até dia 15? Por favor?"
    e "Dia 15 então. Mas vai pra R$700 com juros. Dia 15 eu volto."

#outro capitulo
#escolhas parte da manhã

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

#parte da tarde
    #diana no cll vê cobranca ("Diana, lembrando... dia 15, R$700.")
    d"Como se eu tivesse dinheiro pra isso... Mas se eu me atrasar, o Elias vai me cobrar mais ainda..."
    menu:
        "Pagar mesmo que parcialmente"

        "Pedir ajuda pra Andreia parcelar":
            a "Deixa que eu falo com ele, filha. Você me paga depois me ajudando com a Lili."

        "Descansar e organizar as ideias"
#capitulo 3
    a "Diana, amanhã vamos fazer 30 bolos de pote pra escola. Cada uma faz 10 e divide. Vem? Minha filha Lili vai amar ter você lá."

    h "Amiga! Consegui me inscrever no curso de Atendimento do SENAC Delas. Sabe que pra mim, mulher trans, é difícil arrumar trampo formal, mas esse curso tem parceria de emprego. Tem bolsa de R$300. Bora juntas? A gente se ajuda na prova."

    menu:
        "Aceitar convite da Andreia - Empreender em coletivo":
            d "Vou sim! Vai ser bom pra mim e pra Lili."
            #$confianca += 1
            #$rede += 1


        "Aceitar convite da Helena - Curso com bolsa":
            d "Vou sim! Vai ser bom pra mim e pra Helena."
            #$confianca += 1
            #$rede += 1

        "Recusar os convites":
            d "Não vou. Preciso me organizar primeiro."
            #$confianca -= 1
    return

#variações, cap 4

label andreia:
    a "Diana, cliente quer 50 bolos pra sábado, mas não temos batedeira grande."
    menu:
        "Pedir emprestado na associação (+2 rede, +R$300)":
            $rede += 2
            $dinheiro += 300

        "Fazer na mão virando a noite (+2 confiança, +R$300)":
            $confianca += 2
            $dinheiro += 300

        "Recusar e fazer só 30 (+1 confiança, +R$150)":
            $confianca += 1
            $dinheiro += 150

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
