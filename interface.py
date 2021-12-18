import pygame.display
import pygame as pg


class pontuacao:
    def __init__(self,win,x,y,cor,fonte):
        self.texto = '00'
        self.x = x
        self.y = y
        self.cor = cor
        self.fonte = fonte

        self.win = win

    def set_valor(self,valor):
        if valor < 10:
            valor = '0'+ str(valor)
        self.texto = str(valor)

    def soma(self,valor):
        valor = valor + int(self.texto)
        if valor < 10:
            valor = '0'+ str(valor)
        self.texto = str(valor)
    def draw(self):
        numeros = self.fonte.render(self.texto,True,self.cor)
        self.win.blit(numeros,(self.x,self.y,10,10))

class texto:
    def __init__(self, win,texto ,x, y, cor, fonte):
        self.texto = texto
        self.x = x
        self.y = y
        self.cor = cor
        self.fonte = fonte
        self.win = win
    def mudar(self,frase):
        self.texto = frase
    def draw(self):
        frase = self.fonte.render(self.texto,True,self.cor)
        self.win.blit(frase,(self.x,self.y,10,10))

class Vida:
    def __init__(self, win,x,y, img_vida, nome, vida):
        self.x = x
        self.y = y
        self.win = win
        self.nome = nome
        self.vida_per = vida
        self.img_vida = pygame.image.load(img_vida)
        self.vidas = [self.img_vida,self.img_vida,self.img_vida,self.img_vida,self.img_vida]
        self.erro = False

    def vida_funcao(self, vida_atual):
        if vida_atual == 90:
            self.vidas[4] = pygame.image.load('coracao_vida_partido.png')
        elif vida_atual == 80:
            try:
                self.vidas.pop(4)
            except IndexError:
                self.erro = True
        elif vida_atual == 70:
            self.vidas[3] = pygame.image.load('coracao_vida_partido.png')
        elif vida_atual == 60:
            try:
                self.vidas.pop(3)
            except IndexError:
                self.erro = True   
        elif vida_atual == 50:
            self.vidas[2] = pygame.image.load('coracao_vida_partido.png')
        elif vida_atual == 40:
            try:
                self.vidas.pop(2)
            except IndexError:
                self.erro = True
        elif vida_atual == 30:
            self.vidas[1] = pygame.image.load('coracao_vida_partido.png')
        elif vida_atual == 20:
            try:
                self.vidas.pop(1)
            except IndexError:
                self.erro = True
        elif vida_atual == 10:
            self.vidas[0] = pygame.image.load('coracao_vida_partido.png')
        elif vida_atual <= 0:
            try:
                self.vidas.pop(0)
            except IndexError:
                self.erro = True

        
    def draw(self):
        if self.nome == 'player1':
            imagem = pygame.image.load('player1.png')
        elif self.nome == 'player2':
            imagem = pygame.image.load('player2.png')
        
        self.win.blit(imagem,(self.x - 40,self.y,20,20))

        for i in range(len(self.vidas)):
            self.win.blit(self.vidas[i], (self.x+ (i * 30),self.y,10,10))