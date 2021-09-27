import random
from random import randint #Módulo para sortear números randomicos
from time import sleep #Módulo para mostrar o print depois de alguns segundos
'''
Nome: Victor Hugo Rabello Teixeira
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
'''


def iniciar_game():#Começar o jogo!
    print('-=' * 27)
    print('\033[1;32m _____               _     _      ____  _')
    print('|__  /___  _ __ ___ | |__ (_) ___|  _ \(_) ___ ___')
    print("  / // _ \| '_ ` _ \| '_ \| |/ _ \ | | | |/ __/ _ \ ")
    print(' / /_ (_) | | | | | | |_) | |  __/ |_| | | (__  __/')
    print('/____\___/|_| |_| |_|_.__/|_|\___|____/|_|\___\___|\033[m')
    print('-=' * 27)

    # Chama a função para armazenar os jogadores
    jogador_game()


# Função de regras
def regras_inicio():
    regras = input("\nVocê já conhece as regras ? [S/N]").upper()[0]#Pega a primeira letra do que é escrito e deixa em maiusculo
    sleep(0.3)
    while regras != 'S':#Estrutura de repitição, caso a resposta seja diferente de sim
        if regras=="N":
            print("\nAcesse o link: \033[1;4;34mbityli.com/uOjrr\033[m")
            sleep(1)
            regras = input("\nVocê já conhece as regras ? [S/N]").upper()[0]
            sleep(1)
        else:#Else faz parte da condição do if, diferente do else do While logo abaixo!
            print("\nNão é uma resposta válida, digite '\033[1;32mSIM\033[m' ou '\033[1;31mNÂO\033[m'")
            sleep(1)
            regras = input("\nVocê já conhece as regras ? [S/N]").upper()[0]
            sleep(1)
    else:# se a resposta for sim, ele continua daqui
            print("\nótimo, podemos começar a jogar!\n")
            sleep(1)


# Função para sortear dados
def rolarDado():
    global mesa
    # Crio a variavel mesa para armazenar os passos que irão continuar no jogo
    mesa = []
    global copo
    # Variavel criada apra armazenar os valores dos dados
    copo = ['Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Amarelo', 'Amarelo', 'Amarelo', 'Amarelo','Vermelho', 'Vermelho', 'Vermelho', ]
    # Faz um loop num range de 3 para sortear os dados 3 vezes
    for i in range(0, 3):
            # Variavel dado armazena o valor aleatorio que vem do copo
            dado = random.choice(copo)
            if dado == 'Verde':
                # Variavel faceDado armazena os dados que irão vir da função rolarFace
                faceDado = rolarFace(1)
                if faceDado == 'C':
                    faceDado = 'Cérebro'
                if faceDado == 'T':
                    faceDado = 'Tiro'
                if faceDado == 'P':
                    faceDado = 'Passos'
                print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;32mVerde\033[m / \033[1mFace -->\033[m \033[1;32m{faceDado}\033[m')
                calcular(faceDado)
                if faceDado == 'Passos':
                    mesa.append('PVerde')
                sleep(0.6)
            elif dado == 'Amarelo':
                # função com prametro para chamar as cores
                faceDado = rolarFace(2)
                if faceDado == 'C':
                    faceDado = 'Cérebro'
                if faceDado == 'T':
                    faceDado = 'Tiro'
                if faceDado == 'P':
                    faceDado = 'Passos'
                print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;33mAmarelo\033[m / \033[1mFace -->\033[m \033[1;33m{faceDado}\033[m')
                calcular(faceDado)
                if faceDado == 'Passos':
                    mesa.append('PAmarelo')
                sleep(0.6)
            elif dado == 'Vermelho':
                faceDado = rolarFace(3)
                if faceDado == 'C':
                    faceDado = 'Cérebro'
                if faceDado == 'T':
                    faceDado = 'Tiro'
                if faceDado == 'P':
                    faceDado = 'Passos'
                print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;31mVermelho\033[m / \033[1mFace -->\033[m \033[1;31m{faceDado}\033[m')
                # função calcula os pontos dos jogadores
                calcular(faceDado)
                if faceDado == 'Passos':
                    #caso venha Passos é armazenado na mesa
                    mesa.append('PVermelho')
                sleep(0.6)


# Função para Armazenar os pontos com os parametros para identificar nome e valores
def armazena(id,value):
    global pontos
    global vida
    global passos
    global jogadores_nome
    global nomes
    global galera
    jogadores_nome = {}
    jogadores_nome[id] = 0
    # verifica se a resposta foi Não e soma os pontos de todas os turnos
    if value == 1:
        jogadores_nome.update(galera)
        jogadores_nome[id] = jogadores_nome[id] + pontos
    # Verifica que a resposta foi Sim e armazena os dados da rodada
    if value == 2:
        jogadores_nome[id] = pontos
        jogadores_nome.update(galera)
    # Verifica se levou tiro e não armazena dados
    if value == 3:
        jogadores_nome.update(galera)
        jogadores_nome[id] = jogadores_nome[id]


# Função para calcular os pontos
def calcular(faceDado):
    if faceDado == 'Cérebro':
        global pontos
        pontos = pontos + 1
    elif faceDado == 'Tiro':
        global vida
        vida = vida - 1


# Funcão para validar se existe passos na rodada anterior
def ValidacaoPassos():
    global MesaPassos
    # Variavel para armazenar os dados dos passos
    MesaPassos = []
    # Verifica o tamanho da variavel mesa e passa para a função rolarDadoPassos
    if len(mesa) == 1:
        rolarDadoPassos(2)
    elif len(mesa) == 2:
        rolarDadoPassos(1)
    # Loop de 0 a tamnho da variavel mesa para rolar dados
    for i in range(0, len(mesa)):
        if 'PVerde' in mesa:
            mesa.remove('PVerde')
            faceDado = rolarFace(1)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;32mVerde\033[m / \033[1mFace -->\033[m \033[1;32m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                MesaPassos.append('PVerde')
            sleep(0.6)
        elif 'PAmarelo' in mesa:
            mesa.remove('PAmarelo')
            faceDado = rolarFace(2)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;33mAmarelo\033[m / \033[1mFace -->\033[m \033[1;33m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                MesaPassos.append('PAmarelo')
            sleep(0.6)
        elif 'PVermelho' in mesa:
            mesa.remove('PVermelho')
            faceDado = rolarFace(3)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;31mVermelho\033[m / \033[1mFace -->\033[m \033[1;31m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                MesaPassos.append('PVermelho')
            sleep(0.6)


# Funcão para validar se existe passos que veio armazenado da função validarPassos
def ValidacaoPassos1():
    global MesaPassos
    if len(MesaPassos) == 1:
        rolarDadoPassos1(2)
    elif len(MesaPassos) == 2:
        rolarDadoPassos1(1)
    for i in range(0, len(MesaPassos)):
        if 'PVerde' in MesaPassos:
            MesaPassos.remove('PVerde')
            faceDado = rolarFace(1)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;32mVerde\033[m / \033[1mFace -->\033[m \033[1;32m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                mesa.append('PVerde')
            sleep(0.6)
        elif 'PAmarelo' in MesaPassos:
            MesaPassos.remove('PAmarelo')
            faceDado = rolarFace(2)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;33mAmarelo\033[m / \033[1mFace -->\033[m \033[1;33m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                mesa.append('PAmarelo')
            sleep(0.6)
        elif 'PVermelho' in MesaPassos:
            MesaPassos.remove('PVermelho')
            faceDado = rolarFace(3)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;31mVermelho\033[m / \033[1mFace -->\033[m \033[1;31m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                mesa.append('PVermelho')
            sleep(0.6)


# Função para aleatorizar os dados do ValidacaoPassos
def rolarDadoPassos(valor):
    global copo
    global MesaPassos
    for i in range(0,valor):
        dado = random.choice(copo)
        if dado == 'Verde':
            faceDado = rolarFace(1)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;32mVerde\033[m / \033[1mFace -->\033[m \033[1;32m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                MesaPassos.append('PVerde')
            sleep(0.6)
        elif dado == 'Amarelo':
            faceDado = rolarFace(2)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;33mAmarelo\033[m / \033[1mFace -->\033[m \033[1;33m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                MesaPassos.append('PAmarelo')
            sleep(0.6)
        elif dado == 'Vermelho':
            faceDado = rolarFace(3)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;31mVermelho\033[m / \033[1mFace -->\033[m \033[1;31m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                MesaPassos.append('PVermelho')
            sleep(0.6)


# Função para aleatorizar os dados do ValidacaoPassos1
def rolarDadoPassos1(valor):
    global copo
    global MesaPassos
    for i in range(0,valor):
        dado = random.choice(copo)
        if dado == 'Verde':
            faceDado = rolarFace(1)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;32mVerde\033[m / \033[1mFace -->\033[m \033[1;32m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                mesa.append('PVerde')
            sleep(0.6)
        elif dado == 'Amarelo':
            faceDado = rolarFace(2)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;33mAmarelo\033[m / \033[1mFace -->\033[m \033[1;33m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                mesa.append('PAmarelo')
            sleep(0.6)
        elif dado == 'Vermelho':
            faceDado = rolarFace(3)
            if faceDado == 'C':
                faceDado = 'Cérebro'
            if faceDado == 'T':
                faceDado = 'Tiro'
            if faceDado == 'P':
                faceDado = 'Passos'
            print(f'Dado {i + 1}: \033[1mCor -->\033[m \033[1;31mVermelho\033[m / \033[1mFace -->\033[m \033[1;31m{faceDado}\033[m')
            calcular(faceDado)
            if faceDado == 'Passos':
                mesa.append('PVermelho')
            sleep(0.6)


# Função para aleatorizar a face do dado
def rolarFace(face):
    dado_verde = 'CPCTPC'
    dado_amarelo = 'TPCTPC'
    dado_vermelho = 'TPTCPT'
    if face == 1:
        faceVerde = random.choice(dado_verde)
        return faceVerde
    elif face == 2:
        faceAmarela = random.choice(dado_amarelo)
        return faceAmarela
    elif face == 3:
        faceVermelha = random.choice(dado_vermelho)
        return faceVermelha


# Função para iniciar o jogo e acabar o jogo
def AcabaJogo():
    global jogadores
    global galera
    galera = {}
    global nomes
    global jogadores_nome
    global vida
    global pontos
    global passos
    global mesa
    global MesaPassos
    # Cria variavel para para iniciar os pontos e vida
    vida = 3
    pontos = 0

    fimDeJogo = False

    while not fimDeJogo:

        # Percorre os jogadores
        for jogador in jogadores:
            if 13 in galera.values():
                print(f'\n\033[1mVocê ganhou')
                fimDeJogo = True
                break
            elif 14 in galera.values():
                print(f'\n\033[1mVocê ganhou')
                fimDeJogo = True
                break
            elif 15 in galera.values():
                print(f'\n\033[1mVocê ganhou')
                fimDeJogo = True
                break
            elif 16 in galera.values():
                print(f'\n\033[1mVocê ganhou')
                fimDeJogo = True
                break
            elif 17 in galera.values():
                print(f'\n\033[1mVocê ganhou')
                fimDeJogo = True
                break
            # Se foi decretado fim de jogo
            if fimDeJogo:
                break
            # Inicia variável de controle do turno
            continuarTurno = 's'

            vida = 3
            pontos = 0
            passos = 0

            # Repetição dos turnos do jogador atual
            while (continuarTurno.lower() == 's'):
                # Valida se jogador alcançou os pontos para vitoria!
                print(f'\033[1;4;31mTURNO DO JOGADOR {jogador} \033[m\n')
                sleep(0.6)
                print(f'\033[1mJogue os dados\033[m \033[1;31m{jogador}\033[m:')
                rolarDado()
                # Valida se jogador levou mais de 3 tiros no jogo
                if vida <= 0:
                    sleep(0.2)
                    # Chama a função para não armazenar os pontos
                    armazena(jogador,3)
                    input('\nVOCÊ \033[31mMORREU!\033[m PRESSIONE ENTER!\n')
                    break
                print(f'\n\033[1;35mCérebros Comidos: {pontos} ---- Vida restante: {vida}\033[m')
                print(f'Pontos Totais: {galera}')
                # Pergunta se jogador deseja continuar o turno ou anotar seus pontos
                continuarTurno = input("\nAVISO: Você deseja continuar jogando dados? [S/N]\n").upper()[0]
                if continuarTurno == 'S':
                    while mesa:
                        if mesa:
                            print(f'\033[1;4;31mTURNO DO JOGADOR {jogador} \033[m\n')
                            sleep(0.6)
                            print(f'\033[1mJogue os dados\033[m \033[1;31m{jogador}\033[m:')
                            ValidacaoPassos()
                            print(f'\n\033[1;35mCérebros Comidos: {pontos} ---- Vida restante: {vida}\033[m')
                            print(f'Pontos Totais: {galera}')
                            if vida <= 0:
                                sleep(0.2)
                                # Chama a função para não armazenar os pontos
                                armazena(jogador, 3)
                                input('\nVOCÊ \033[31mMORREU!\033[m PRESSIONE ENTER!\n')
                                continuarTurno = 'n'
                                break
                            armazena(jogador, 2)
                            continuarTurno = input("\nAVISO: Você deseja continuar jogando dados? [S/N]\n").upper()[0]
                            if continuarTurno == 'S':
                                if MesaPassos:
                                    print(f'\033[1;4;31mTURNO DO JOGADOR {jogador} \033[m\n')
                                    sleep(0.6)
                                    print(f'\033[1mJogue os dados\033[m \033[1;31m{jogador}\033[m:')
                                    ValidacaoPassos1()
                                    print(f'\n\033[1;35mCérebros Comidos: {pontos} ---- Vida restante: {vida}\033[m')
                                    print(f'Pontos Totais: {galera}')
                                    if vida <= 0:
                                        sleep(0.2)
                                        # Chama a função para não armazenar os pontos
                                        armazena(jogador, 3)
                                        input('\nVOCÊ \033[31mMORREU!\033[m PRESSIONE ENTER!\n')
                                        continuarTurno = 'n'
                                        break
                                    armazena(jogador, 2)
                                    continuarTurno = input("\nAVISO: Você deseja continuar jogando dados? [S/N]\n").upper()[0]
                                    if continuarTurno == 'N':
                                        mesa = []
                if continuarTurno == 'N':
                    print(galera)
                    armazena(jogador,1)
            galera.update(jogadores_nome.copy())


# Função para armazenar os nomes e quantidade de jogadores
def jogador_game():
    global jogadores
    jogadores = []
    jogador_quant = int(input("Digite a quatidade de players: "))  # Pega a quantidade de jogadores para começar a jogar
    while jogador_quant <= 1:
        sleep(0.3)
        print("\n\033[1;31mPara jogar é necessário 2 jogadores ou mais!!\033[m\n")
        sleep(2)
        jogador_game()
        break
    else:
        print("\n\033[1mVAMOS COMEÇAR!\033[m\n")
        sleep(0.5)
    for i in range(0, jogador_quant):  # faz uma contagem de 0 ate quantidade de jogadores colocada no input acima
        nome = input(f"Digite o nome do \033[1mJogador {i + 1}:\033[m ")  # i +1 para começar a contagem a partir de 1 em diante
        jogadores.append(nome)

    regras_inicio()


iniciar_game()
AcabaJogo()
print(f'\n\033[1;33mPontuação Final:{galera}\033[m')

#███████▀▀▀░░░░░░░▀▀▀███████
#████▀░░░░░░░░░░░░░░░░░▀████
#██│░░░░░░░░░░░░░░░░░░░│███
#██▌│░░░░░░░░░░░░░░░░░░░│▐██
#██░└┐░░░░░░░░░░░░░░░░░┌┘░██
#██░░└┐░░░░░░░░░░░░░░░┌┘░░██
#█░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
#██▌░│██████▌░░░▐██████│░▐██
#███░│▐███▀▀░░▄░░▀▀███▌│░███
#██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
#██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
#████▄─┘██▌░░░░░░░▐██└─▄████
#█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
#████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
#█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
#███████▄░░░░░░░░░░░▄███████
#██████████▄▄▄▄▄▄▄██████████