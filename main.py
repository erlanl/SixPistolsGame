import pygame as pg

import os

import pygame.font

from classes import Balas
from classes import Player
from interface import pontuacao
from interface import texto


def main():
    screen = pg.display.set_mode((1280, 720))
    pg.display.set_caption('Projeto IP')
    clock = pg.time.Clock()


    player1 = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
    #as fontes estão na pasta Assets, pode escolher qualquer fonte com tipo de arquivo .ttf
    #escolhendo a fonte pra usar, o segundo argumento é o tamanho
    fonte_pontuacao = pg.font.Font(os.path.join('Assets/alarm clock.ttf'),40)
    fonte_texto = pg.font.Font(os.path.join('Assets/SEASRN__.ttf'),20)
    #os argumentos são a janela, a posicao x, posicao y, cor e a fonte
    pontuacao1 = pontuacao(screen,10,40,(255,255,255),fonte_pontuacao)
    pontuacao2 = pontuacao(screen, (screen.get_width()-50), 40, (255, 255, 255), fonte_pontuacao)
    #os argumentos sao a janela, o texto, posicao x , posicao y, cor e a fonte
    id1 = texto(screen,'Jogador 1', 10,10,(255,255,255),fonte_texto)
    id2 = texto(screen, 'Jogador 2', (screen.get_width()-135), 10, (255, 255, 255), fonte_texto)
    Balas(screen, 100, 80)
    Balas(screen, 200, 80)
    Balas(screen, 200, 180)
    Balas(screen, 100, 180)

    # posição do jogador no plano (x, y)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        player1.control()
        player2.control()

        screen.fill((40, 40, 40))

        player1.draw()
        player2.draw()
        pontuacao1.draw()
        pontuacao2.draw()
        id1.draw()
        id2.draw()
        # desenha todas as balas da lista
        for bala in Balas.lista_balas:
            bala.draw()

        pg.display.flip()
        clock.tick(30)

        # para cada bala na lista checa a colisão
        for bala in Balas.lista_balas:
            if bala.rect.colliderect(player1):
                player1.quantidade_balas += 1
                pontuacao1.soma(1)
                bala.remover()
                print(f"player1 tem {player1.quantidade_balas} balas")

            if bala.rect.colliderect(player2):
                player2.quantidade_balas += 1
                pontuacao2.soma(1)
                bala.remover()
                print(f"player2 tem {player2.quantidade_balas} balas")


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()