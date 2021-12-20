import pygame
from abc import ABC, abstractmethod
from pygame import mixer

pygame.mixer.init()
som_coleta= mixer.Sound("sons/coletar.wav")
som_coleta.set_volume(0.03)
#classe que todos os coletáveis herdam
class Coletaveis:
    # lista de todos os coletaveis
    lista_coletaveis = []
    cor="WHITE"
    som_coleta=None
    

    def __init__(self, win, x, y):
        
        self.win = win
        self.x = x
        self.y = y

        self.largura = 10
        self.altura = 10
        self.rect = pygame.Rect(x, y, 10, 10);

        # coloca o coletavel na lista
        Coletaveis.lista_coletaveis.append(self)

    def draw(self,screen):
        if self.atributo == "VELOCIDADE_JOGADOR":
            self.imagem = pygame.image.load('imagens/buff_rapidez.png')
            screen.blit(self.imagem, self.rect)
        if self.atributo == "VELOCIDADE_TIRO":
            self.imagem = pygame.image.load('imagens/buff_velo_tiro.png')
            screen.blit(self.imagem, self.rect)
        if self.atributo == "DIMINUIR_COOLDOWN":
            self.imagem = pygame.image.load('imagens/buff_reduz_cooldown.png')
            screen.blit(self.imagem, self.rect)
        if self.atributo == "BALA":
            self.imagem = pygame.image.load('imagens/bullet.png')
            screen.blit(self.imagem, self.rect)

    def remover(self):
        if self in Coletaveis.lista_coletaveis:
            Coletaveis.lista_coletaveis.remove(self)

    @abstractmethod
    def colisao_jogador(self):
        pass

#balsa coletáveis
class Balas(Coletaveis):
    atributo="BALA"

    def colisao_jogador(self, jogador):
        som_coleta.play()
        jogador.quantidade_balas+=1
        self.remover()
        print(f"jogador tem {jogador.quantidade_balas} balas")

#power up que aumenta velocidade do jogador
class Velocidade(Coletaveis):
    atributo="VELOCIDADE_JOGADOR"

    def colisao_jogador(self, jogador):
        som_coleta.play()
        if jogador.velocidade<10:
            jogador.velocidade+=1
        self.remover()
        print(f"velocidade do jogador aumentada para {jogador.velocidade}")

#pwoer up que aumenta a velocidade dos tiros
class Velocidade_Tiro(Coletaveis):
    atributo="VELOCIDADE_TIRO"

    def colisao_jogador(self, jogador):
        som_coleta.play()
        if jogador.vel<15:
            jogador.vel+=1
        self.remover()

        print(f"velocidade da bala aumentada para {jogador.vel}")

#power up que diminui o delay dos tiros
class Cadencia(Coletaveis):
    atributo="DIMINUIR_COOLDOWN"

    def colisao_jogador(self, jogador):
        som_coleta.play()
        if jogador.COOLDOWN>15:
            jogador.COOLDOWN-=3
        self.remover()
        print(f"cooldown reduzido para {jogador.COOLDOWN}")

