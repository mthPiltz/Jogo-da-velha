import pygame
from pygame.locals import * 
from sys import exit


def desenha(quadrado_marcado, quadrados, posicao_no_tabuleiro, jogador, tela):
    if quadrado_marcado != 10:
            posicao_x, posicao_y = define_posicoes(quadrados, quadrado_marcado)

    if posicao_no_tabuleiro == True:
        if jogador == True:
            img = pygame.image.load("x.png").convert_alpha()
            imgR = pygame.transform.scale(img, (83, 83))
            tela.blit(imgR, (posicao_x + 35, posicao_y + 15))
        else:
            imgc = pygame.image.load("circulo.png").convert_alpha()
            imgcR = pygame.transform.scale(imgc, (83, 83))
            tela.blit(imgcR, (posicao_x + 35, posicao_y + 15))
    else:
        print("Clique em uma posição no tabuleiro")


def procura_quadrado(quadrados, posicao_mouse):
    posicao_no_tabuleiro = False
    for i in range(len(quadrados)):
        quadrado_testadoo = quadrados[i]
        x_menor = quadrado_testadoo[0]
        x_maior = quadrado_testadoo[2]
        y_menor = quadrado_testadoo[1]
        y_maior = quadrado_testadoo[3]
        if x_menor <= posicao_mouse[0] and x_maior >= posicao_mouse[0] and y_menor <= posicao_mouse[1] and y_maior >= posicao_mouse[1]:
            quadrado_marcado = i
            posicao_no_tabuleiro = True
            return quadrado_marcado, posicao_no_tabuleiro
        quadrado_marcado = 10
    return quadrado_marcado, posicao_no_tabuleiro


def define_posicoes(quadrados, quadrado_marcado):
    aux_x = quadrados[quadrado_marcado]
    posicao_x = aux_x[0]
    aux_y = quadrados[quadrado_marcado]
    posicao_y = aux_y[1]

    return posicao_x, posicao_y


def alterna_jogador(jogador):
    if jogador == True:
        jogador = False
    else:
        jogador = True

    return jogador


def marca_posicoes(tabuleiro, jogador, quadrado_marcado):
    if quadrado_marcado == 10:
        return tabuleiro

    if jogador == False:
        tabuleiro[quadrado_marcado] = "X"
    else:
        tabuleiro[quadrado_marcado] = "O"
    return tabuleiro


def verifica_vencedor(tabuleiro):
    if tabuleiro[0] == tabuleiro[1] and tabuleiro[0] == tabuleiro[2]:
        vencedor = True
        print("AÈEEEEE")
        return vencedor
    if tabuleiro[3] == tabuleiro[4] and tabuleiro[3] == tabuleiro[5]:
        vencedor = True
        return vencedor
    if tabuleiro[6] == tabuleiro[7] and tabuleiro[6] == tabuleiro[8]:
        vencedor = True
        return vencedor
    if tabuleiro[0] == tabuleiro[3] and tabuleiro[0] == tabuleiro[6]:
        vencedor = True
        return vencedor
    if tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7]:
        vencedor = True
        return vencedor
    if tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8]:
        vencedor = True
        return vencedor
    if tabuleiro[0] == tabuleiro[4] and tabuleiro[0] == tabuleiro[8]:
        vencedor = True
        return vencedor
    if tabuleiro[2] == tabuleiro[4] and tabuleiro[2] == tabuleiro[6]:
        vencedor = True
        return vencedor
    if tabuleiro[0] == tabuleiro[1] and tabuleiro[0] == tabuleiro[2]:
        vencedor = True
        return vencedor



def verifica_posicao(tabuleiro, quadrado_marcado):
    print(quadrado_marcado)
    ocupada = False
    if quadrado_marcado == 10:
        return
    if tabuleiro[quadrado_marcado] == "X" or tabuleiro[quadrado_marcado] == "O":
        print("aaaaaaaaaaaaaaaa")
        ocupada = True
    return ocupada


def mensagem_principal(jogador, tela):
    arial = pygame.font.SysFont("arial", 70)
    if jogador == True:
        teste = arial.render("Vez do Jogador X", True, (255, 0, 0), 0)
        tela.blit(teste, (20,20))
    else:
        teste = arial.render("Vez do Jogador O", True, (255, 0, 0), 0)
        tela.blit(teste, (20,20))

def main():
    pygame.init()
    #---------- configurações da tela
    tela = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Jogo da velha")
    pygame.draw.line(tela, (142, 0, 0), (166,135), (166, 480), 5)
    pygame.draw.line(tela, (142, 0, 0), (333,135), (333, 480), 5)
    pygame.draw.line(tela, (142, 0, 0), (20,240), (480,240), 5)
    pygame.draw.line(tela, (142, 0, 0), (20,365), (480,365), 5)


    #----------------------------------
    tabuleiro = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    jogador = True
    contador = 0

    #Definindo os "botões" do jogo
    posicao1 = Rect((20, 135), (166, 240))
    posicao2 = Rect((166, 135), (333, 240))
    posicao3 = Rect((333, 135), (480, 240))
    posicao4 = Rect((20, 240), (166, 365))
    posicao5 = Rect((166, 240), (333, 365))
    posicao6 = Rect((333, 240), (480, 365))
    posicao7 = Rect((20, 365), (166, 480))
    posicao8 = Rect((166, 365), (333, 480))
    posicao9 = Rect((333, 365), (480, 480))

    quadrados = [posicao1, posicao2, posicao3, posicao4, posicao5, posicao6, posicao7, posicao8, posicao9]

    while True:
        pygame.display.flip()
        mensagem_principal(jogador, tela)
        vencedor = False
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()

            if e.type == MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                quadrado_marcado, posicao_no_tabuleiro = procura_quadrado(quadrados, posicao_mouse)
                ocupada = verifica_posicao(tabuleiro, quadrado_marcado)
                if ocupada == False:
                    desenha(quadrado_marcado, quadrados, posicao_no_tabuleiro, jogador, tela)
                    jogador = alterna_jogador(jogador)
                    tabuleiro = marca_posicoes(tabuleiro, jogador, quadrado_marcado)
                    vencedor = verifica_vencedor(tabuleiro)
                    contador += 1

                print(tabuleiro)

        if vencedor == True:
            print("Vitoria") 
            main()
        elif contador == 9:
            print("Empate")
            main()


main()