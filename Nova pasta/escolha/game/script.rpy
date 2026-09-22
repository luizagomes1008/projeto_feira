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
define H = Character("Helena")
image Hpadrao = "/images/Hpadrao.jpeg"
image Hrindo = "/images/Hrindo.jpeg"

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
    d"hm..."
    show m
    pause 1.0




    

    # This ends the game.

    return
