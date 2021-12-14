import pygame
from abc import ABC, abstractmethod

class Coletaveis:
    # lista de todos os coeltaveis
    lista_coletaveis = []
    cor="WHITE"
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 10
        self.altura = 10
        self.rect = pygame.Rect(x, y, 10, 10);

        # coloca o coletavel na lista
        Coletaveis.lista_coletaveis.append(self)

    def draw(self):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(self.win, self.cor, self.rect)

    def remover(self):
        Coletaveis.lista_coletaveis.remove(self)

    @abstractmethod
    def colisao_jogador(self):
        pass

class Balas(Coletaveis):
    cor="YELLOW"

    def colisao_jogador(self, jogador):
        jogador.quantidade_balas+=1
        self.remover()

class Velocidade(Coletaveis):
    cor="PURPLE"

    def colisao_jogador(self, jogador):
        if jogador.velocidade<15:
            jogador.velocidade+=1
        self.remover()

class Velocidade_Tiro(Coletaveis):
    cor="CYAN"

    def colisao_jogador(self, jogador):
        if jogador.vel<15:
            jogador.vel+=1
        self.remover()

class Cadencia(Coletaveis):
    cor="BLACK"

    def colisao_jogador(self, jogador):
        if jogador.COOLDOWN>15:
            jogador.COOLDOWN-=3
        self.remover()
    

