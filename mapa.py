import pygame


class Parede(pygame.sprite.Sprite):
    def __init__(self, imagem, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        pass


class Mapa:
    def __init__(self, arquivo): 

        #colocando todas as paredes inquebráveis em um grupo      
        self.grupo = pygame.sprite.RenderUpdates()
        self.grupo_quebravel = pygame.sprite.RenderUpdates()

        self.parede_lados = pygame.image.load('casas_lado.png').convert_alpha()
        self.parede_hemisferios = pygame.image.load('casas_hemisferio.png').convert_alpha()
        
        
        #acessando o arquivo que contem o mapa em forma de texto
        arquivo = open(arquivo)
        self.textoMapa = arquivo.readlines()
        arquivo.close()
        
        #Acessando o mapa.txt linha por linha para substituir cada caractere por uma imagem
        linha_auxiliar = -1
        for linha in self.textoMapa:
            linha_auxiliar += 1
            coluna = -1
            for caractere in linha:
                coluna += 1
                
                #Convertendo os valores para pixel para saber a posição real na tela
                x,y = self.conversorPixel(linha_auxiliar, coluna)  
                
                if caractere == '#':
                    self.grupo.add(Parede(self.parede_lados, (x,y)))
                if caractere == '=':
                    self.grupo.add(Parede(self.parede_hemisferios, (x,y)))
                if caractere == '|':
                    self.grupo_quebravel.add(Parede(self.parede_lados, (x,y)))
    

    def atualizar_tela(self, screen):
        #screen.fill((255,255,255))
        self.grupo.update()
        self.grupo.draw(screen)
        self.grupo_quebravel.update()
        self.grupo_quebravel.draw(screen)

    #nosso mapa tem 600x650 e o arquivo tem 15 colunas e 16 filas
    #Assim, cada desenho dos sprites é 40x40 pixels (40x15 = 600, 40x16 = 640)
    def conversorPixel(self, linha, coluna):
        return (linha*40, coluna*40)