import pygame.display
import pygame as pg

#essa classe pontuacao
#é uma classe que mostra na tela números
#que no jogo foi usada para mostrar a quantidade de municao
class pontuacao:
    def __init__(self,win,x,y,cor,fonte):
        #ele comeca como 0 no padrão
        self.texto = '00'
        self.x = x
        self.y = y
        self.cor = cor
        self.fonte = fonte

        self.win = win

    def set_valor(self,valor):
        #se você quiser botar qualquer valor no display
        if valor < 10:
            valor = '0'+ str(valor)
        self.texto = str(valor)

    def soma(self,valor):
        #essa é a funcao para somar uma quantidade
        #ao valor já existente
        valor = valor + int(self.texto)
        if valor < 10:
            valor = '0'+ str(valor)
        self.texto = str(valor)
    def draw(self):
        #criando a surface
        numeros = self.fonte.render(self.texto,True,self.cor)
        #desenhando
        self.win.blit(numeros,(self.x,self.y,10,10))

#essa é parecida com a funcao de pontuacao
#mas é usada para mostrar texto na tela
#então não se pode somar
#apenas mudar o texto
#se precisar
class texto:
    def __init__(self, win,texto ,x, y, cor, fonte):
        self.texto = texto
        self.x = x
        self.y = y
        self.cor = cor
        self.fonte = fonte
        self.win = win
    def mudar(self,frase):
        #se você quiser mudar o texto
        #mostrado
        self.texto = frase
    def draw(self):
        #faz a surface
        frase = self.fonte.render(self.texto,True,self.cor)
        #desenha na tela
        self.win.blit(frase,(self.x,self.y,10,10))

class Vida:
    """
    Classe de sprite de vida
    """
    def __init__(self, win,x,y, img_vida, nome, vida):
        self.x = x
        self.y = y
        self.win = win
        self.nome = nome
        self.vida_per = vida
        self.img_vida = pygame.image.load(img_vida)
        self.vidas = [self.img_vida,self.img_vida,self.img_vida]
        self.erro = False

    def vida_funcao(self, vida_atual):
        """
        Método de verificar a vida do player
        """
        if vida_atual == 50: # Em determinada vida o coração fica ao meio
            self.vidas[2] = pygame.image.load('imagens/coracao_vida_partido.png')
        elif vida_atual == 40: # Perdendo um coração todo
            try:
                self.vidas.pop(2)
            except IndexError:
                self.erro = True
        elif vida_atual == 30:
            self.vidas[1] = pygame.image.load('imagens/coracao_vida_partido.png')
        elif vida_atual == 20:
            try:
                self.vidas.pop(1)
            except IndexError:
                self.erro = True   
        elif vida_atual == 10:
            self.vidas[0] = pygame.image.load('imagens/coracao_vida_partido.png')
        elif vida_atual <= 0:
            try:
                self.vidas.pop(0)
            except IndexError:
                self.erro = True

        
    def draw(self):
        """
        Método de desenhar os corações
        """
        if self.nome == 'player1': # Se for o player 1 desenha o cowboy
            imagem = pygame.image.load('imagens/head_cowboy.png')
            inicialx= self.x - 30
        elif self.nome == 'player2': # Se for o player 2 desenha a cowgirl
            imagem = pygame.image.load('imagens/head_cowgirl.png')
            inicialx= self.x - 40
        
        
        self.win.blit(imagem,(inicialx,self.y+20,20,20))

        for i in range(len(self.vidas)): # Desenhar vários corações
            if i == 0: # Posições de cada coração
                if self.nome == 'player1':
                    inicialx = inicialx + 40
                elif self.nome == 'player2':
                    inicialx = inicialx + 80
                self.win.blit(self.vidas[i], (inicialx,self.y,10,10))
            else:
                self.win.blit(self.vidas[i], (inicialx+ (i * 30),self.y,10,10))
