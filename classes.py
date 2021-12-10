import pygame
import pygame as pg


class Balas:
    # lista de todas as balas do jogo
    lista_balas = []

    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 10
        self.altura = 10
        self.cor = 'RED'
        self.rect = pygame.Rect(x, y, 10, 10);

        # coloca a bala na lista
        Balas.lista_balas.append(self)

    def draw(self):
        self.rect.center = [self.x, self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def remover(self):
        Balas.lista_balas.remove(self)


class Player:
    def __init__(self, win, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita):
        self.win = win
        self.x = x
        self.y = y

        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita

        self.quantidade_balas = 0
        self.square = pygame.Rect(300, 230, 20, 20)
        self.largura = 20
        self.altura = 20
        self.vel = 10
        self.cor = 'WHITE'
        self.rect = pygame.Rect(x, y, 20, 20);

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
        self.rect.center = [self.x, self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

