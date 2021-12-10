import pygame as pg
from classes import Balas
from classes import Player


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    player1 = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
    
    Balas(screen, 100, 80)
    Balas(screen, 200, 80)
    Balas(screen, 200, 180)
    Balas(screen, 100, 180)

    #posição do jogador no plano (x, y)
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

        #desenha todas as balas da lista
        for bala in Balas.lista_balas:
            bala.draw()

        pg.display.flip()
        clock.tick(30)

        #para cada bala na lista checa a colisão
        for bala in Balas.lista_balas:
            if bala.rect.colliderect(player1):
                player1.quantidade_balas+=1
                bala.remover()
                print(f"player1 tem {player1.quantidade_balas} balas")

            if bala.rect.colliderect(player2):
                player2.quantidade_balas+=1
                bala.remover()
                print(f"player2 tem {player2.quantidade_balas} balas")


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()