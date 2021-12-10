import pygame
import pygame as pg
import random
import copy

#x_random = random.uniform(0, 640)
#y_random = random.uniform(0, 480)

class Balas:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 10
        self.altura = 10
        self.cor = 'RED'

    def draw(self):
        pg.draw.rect(self.win, self.cor, (self.x, self.y, self.largura, self.altura))


class Player:
    def __init__(self, win, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita):
        self.win = win
        self.x = x
        self.y = y

        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita
        
        self.square = pygame.Rect(300, 230, 20, 20)
        self.largura = 20
        self.altura = 20
        self.vel = 10
        self.cor = 'WHITE'

    
    def control(self):
        keys = pg.key.get_pressed()

        if keys[self.tecla_esquerda]:
            self.x -= self.vel
        if keys[self.tecla_direita]:
            self.x += self.vel
        if keys[self.tecla_cima]:
            self.y -= self.vel
        if keys[self.tecla_baixo]:
            self.y += self.vel
        
    def draw(self):
        pg.draw.rect(self.win, self.cor, (self.x, self.y, self.largura, self.altura))



def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    player = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
    bala = Balas(screen, 100, 80)

    players = [player, player2]

    #posição do jogador no plano (x, y)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        
        player.control()
        player2.control()

        screen.fill((40, 40, 40))
        player.draw()
        player2.draw()
        bala.draw()

        pg.display.flip()
        clock.tick(30)

        
        #if player.collidrect(bala):
        #    print('oi')
        #if player2.colliderect(player):
        #    print('oi')

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()


#ATENÇÃO: o eixo y é invertido