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
        self.texto = valor

    def soma(self,valor):
        valor = valor + int(self.texto)
        if valor < 10:
            valor = '0'+ str(valor)
        self.texto = valor
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