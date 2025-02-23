from tkinter import *
from PIL import Image, ImageTk
from lib import *
from Classes.classItem import Item
from Classes.classJogo import Jogo


usuarioLogado = lerArquivo("Arquivos/Informações/usuarioLogado")[0]

# Lendo o arquivo que contém os itens do catálogo
global listaItens

listaItens = [
    Jogo("Forza Horizon 5", "2021", "Jogo", "Xbox/PC", "Playground Games", 100,
         "Forza Horizon 5 leva os jogadores a uma experiência imersiva no México, com gráficos incríveis, eventos dinâmicos e carros personalizáveis. Aventure-se em paisagens diversificadas e participe de competições eletrizantes."),

    Item("Esquadrão Suicida", "2016", "Filme", "Jogo", 101,
         "Quando uma agência secreta do governo recruta supervilões encarcerados para formar uma força-tarefa especial, a missão suicida coloca o destino do mundo em suas mãos. Ação intensa e humor negro garantidos!"),

    Jogo("The Witcher 3", "2015", "Jogo", "Multiplataforma", "CD Projekt Red", 102,
         "The Witcher 3 é um RPG aclamado que coloca o jogador na pele de Geralt, um caçador de monstros. Explore um mundo vasto e cheio de escolhas que afetam a história, com combates intensos e personagens memoráveis."),

    Item("Interstellar", "2014", "Filme", "Jogo", 103,
         "Em um futuro onde a Terra está morrendo, um grupo de astronautas embarca em uma missão intergaláctica para encontrar um novo planeta habitável. Uma história emocionante sobre tempo, amor e destino."),

    Jogo("Red Dead Redemption 2", "2018", "Jogo", "Multiplataforma", "Rockstar Games", 104,
         "Em uma narrativa épica, acompanhe Arthur Morgan e a gangue Van der Linde enquanto lutam para sobreviver em um mundo em mudança. Com um vasto mundo aberto e detalhes impressionantes, este jogo é uma obra-prima."),

    Jogo("Cyberpunk 2077", "2020", "Jogo", "Multiplataforma", "CD Projekt Red", 105,
         "Cyberpunk 2077 apresenta um mundo futurista vibrante, onde o jogador assume o papel de V, um mercenário em busca de imortalidade. Personalize habilidades, hackeie sistemas e explore uma cidade cheia de perigos e oportunidades."),

    Item("Oppenheimer", "2023", "Filme", "Jogo", 106,
         "Uma visão intensa e profunda sobre J. Robert Oppenheimer, o físico por trás da criação da bomba atômica. O filme explora suas conquistas científicas e os dilemas morais de sua invenção."),

    Jogo("The Last of Us Part II", "2020", "Jogo", "PlayStation", "Naughty Dog", 107,
         "Após eventos trágicos, Ellie embarca em uma jornada brutal de vingança. Em um mundo pós-apocalíptico infestado por infectados e humanos perigosos, cada decisão pode mudar o rumo da história."),

    Item("Duna", "2021", "Filme", "Jogo", 108,
         "Duna conta a história de Paul Atreides, um jovem nobre que precisa sobreviver em um planeta desértico e lidar com forças políticas poderosas. Uma jornada épica de coragem, traição e destino."),

    Jogo("God of War Ragnarok", "2022", "Jogo", "PlayStation", "Santa Monica Studio", 109,
         "A saga nórdica continua com Kratos e Atreus enfrentando deuses e monstros enquanto tentam impedir o Ragnarok. Com batalhas épicas e narrativa envolvente, este jogo traz uma conclusão épica à jornada."),

    Item("Avatar: O Caminho da Água", "2022", "Filme", "Jogo", 110,
         "Nesta continuação, Jake e Neytiri lideram seu povo em meio a novos desafios e descobertas. Com efeitos visuais impressionantes, o filme explora o ecossistema subaquático de Pandora."),

    Jogo("Horizon Forbidden West", "2022", "Jogo", "PlayStation", "Guerrilla Games", 111,
         "Aventure-se em um mundo pós-apocalíptico repleto de criaturas mecânicas. Aloy deve descobrir os segredos do Oeste Proibido e impedir uma nova ameaça à humanidade."),

    Item("John Wick 4", "2023", "Filme", "Jogo", 112,
         "John Wick enfrenta desafios cada vez mais intensos enquanto tenta escapar de sua vida de assassino. Com cenas de ação eletrizantes e um enredo cheio de reviravoltas, este filme mantém a adrenalina no máximo."),

    Jogo("Spider-Man 2", "2023", "Jogo", "PlayStation", "Insomniac Games", 113,
         "A sequência do aclamado jogo do Homem-Aranha traz Peter e Miles enfrentando vilões icônicos como Venom. Com combate aprimorado e uma cidade ainda mais interativa, este jogo é um dos melhores da franquia."),

    Item("Guardiões da Galáxia Vol. 3", "2023", "Filme", "Jogo", 114,
         "O último capítulo da saga dos Guardiões revela segredos dos personagens enquanto enfrentam uma nova ameaça galáctica. Com humor, emoção e ação, este filme fecha a trilogia com chave de ouro.")
]


adicionarAoArquivo(listaItens,"itensCatalogo")
listaItens = lerArquivo("Arquivos/Informações/itensCatalogo")

# Interface do projeto
janela = Tk()
janela.geometry("940x600")
janela.title(f"Locadora Caribe - {usuarioLogado.username}")
janela["bg"] = "#1b1b33"
janela.resizable(False, False)
janela.attributes("-toolwindow",False)
janela.iconbitmap("Arquivos/Imagens/logoProjetoIco.ico")

global itemSelecionado
itemSelecionado = ""

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(x=10,y=50,width=395,height=540)

if itemSelecionado == "":
    displayTexto = Label(display, text="Seja bem-vindo à \nLocadora Caribe!!", 
                         font=("Arial", 20, "bold"), background="#3c3d61", 
                         foreground="white")
    displayTexto.pack(pady=20, anchor="center")

    logo = PhotoImage(file="Arquivos/Imagens/logoProjeto.png")
    displayLogo = Label(display,image=logo,background="#3c3d61")
    displayLogo.pack(anchor="center")

    displayTextoMenor = Label(display, 
        text="A Locadora Caribe é um projeto desenvolvido por Caio Enzo Bessa de Oliveira e José Fernandes Figueirêdo Filho, sob a orientação do professor Ciro Daniel Gurgel de Moura, no Instituto Federal do Rio Grande do Norte (IFRN). Criado para simular a experiência de uma locadora moderna, permitindo o aluguel de jogos e filmes por meio de uma interface intuitiva e prática.\n\nSelecione um item para ver suas informações.",
        font=("Arial", 12), background="#3c3d61", foreground="white", 
        wraplength=370, justify="center") 
    displayTextoMenor.pack(pady=5,padx=10,side="bottom",) 

janela.after(500, listarItens(listaItens, janela,display,itemSelecionado))
janela.mainloop()
