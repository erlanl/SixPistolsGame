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

        # colocando todas as paredes inquebráveis em um grupo
        self.grupo = pygame.sprite.RenderUpdates()
        self.grupo_quebravel = pygame.sprite.RenderUpdates()

        #cercas
        self.cercas_continuas = pygame.image.load('imagens/cercas_continuas.png').convert_alpha()
        self.cercas_continuas_cima = pygame.image.load('imagens/cercas_continuas_cima.png').convert_alpha()
        self.fim_cercas_continuas_direita_baixo = pygame.image.load('imagens/fim_cercas_continuas_direita_baixo.png')
        self.fim_cercas_continuas_direita_cima = pygame.image.load('imagens/fim_cercas_continuas_direita_cima.png')
        self.cerca_quina_superior_esquerda = pygame.image.load('imagens/cerca_quina_superior_esquerda.png').convert_alpha()
        self.cerca_quina_superior_direita = pygame.image.load('imagens/cerca_quina_superior_direita.png').convert_alpha()
        self.cerca_quina_inferior_esquerda = pygame.image.load('imagens/cerca_quina_inferior_esquerda.png').convert_alpha()
        self.cerca_quina_inferior_direita = pygame.image.load('imagens/cerca_quina_inferior_direita.png').convert_alpha()

        #parede invisivel
        self.parede_invisivel = pygame.image.load('imagens/parede_invisivel.png').convert_alpha()

        #elementos centrais
        self.barril = pygame.image.load('imagens/barril.png').convert_alpha()
        self.obstaculo_2x1 = pygame.image.load('imagens/obstaculo2x1_agua.png').convert_alpha()
        self.obstaculo_1x1 = pygame.image.load('imagens/obstaculo1x1.png').convert_alpha()
       
        #casas
        self.casa_comum_lado_direito = pygame.image.load('imagens/casa_2_lado_direito.png').convert_alpha()
        self.casa_comum_lado_esquerdo = pygame.image.load('imagens/casa_2_lado_esquerdo.png').convert_alpha()

        self.casa_3x1_lado_direito = pygame.image.load('imagens/casa_3x1_lado_direito.png').convert_alpha()
        self.casa_3x1_lado_esquerdo = pygame.image.load('imagens/casa3x1_lado_esquerdo.png')


        self.casa_3_lado_esquerdo = pygame.image.load('imagens/casa_3_lado_esquerdo.png').convert_alpha()     
        
        #casas com nome
        self.bar = pygame.image.load('imagens/bar.png')
        self.salao = pygame.image.load('imagens/salao.png')
        self.banco = pygame.image.load('imagens/banco.png').convert_alpha()
        
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
                x,y = self.conversorPixel(coluna, linha_auxiliar)  
                
                #cercas
                if caractere == '#':
                    self.grupo.add(Parede(self.parede_lados, (x,y)))
                if caractere == '=':
                    self.grupo.add(Parede(self.cercas_continuas, (x,y)))
                if caractere == '*':
                    self.grupo.add(Parede(self.cercas_continuas_cima, (x,y)))
                if caractere == '(':
                    self.grupo.add(Parede(self.fim_cercas_continuas_direita_baixo, (x,y)))
                if caractere == ')':
                    self.grupo.add(Parede(self.fim_cercas_continuas_direita_cima, (x,y)))
                if caractere == '!':
                    self.grupo.add(Parede(self.cerca_quina_superior_esquerda, (x,y)))
                if caractere == '@':
                    self.grupo.add(Parede(self.cerca_quina_superior_direita, (x,y)))
                if caractere == '$':
                    self.grupo.add(Parede(self.cerca_quina_inferior_esquerda, (x,y)))
                if caractere == '%':
                    self.grupo.add(Parede(self.cerca_quina_inferior_direita, (x,y)))

                #obstaculos
                if caractere == '-':
                    self.grupo.add(Parede(self.barril, (x,y)))
                if caractere == '|':
                    self.grupo_quebravel.add(Parede(self.barril, (x,y)))
                if caractere == 'o':
                    self.grupo.add(Parede(self.obstaculo_2x1, (x,y)))
                if caractere == '0':
                    self.grupo.add(Parede(self.obstaculo_1x1, (x,y)))
                #parede invisivel
                if caractere == 'i':
                    self.grupo.add(Parede(self.parede_invisivel, (x,y)))
                

                #casas
                if caractere == '2':
                    self.grupo.add(Parede(self.casa_comum_lado_direito, (x,y)))
                if caractere == '8':
                    self.grupo.add(Parede(self.casa_comum_lado_esquerdo, (x,y)))


                if caractere == '3':
                    self.grupo.add(Parede(self.casa_3x1_lado_direito, (x,y)))
                if caractere == '1':
                    self.grupo.add(Parede(self.casa_3x1_lado_esquerdo, (x,y)))


                if caractere == '7':
                    self.grupo.add(Parede(self.casa_3_lado_esquerdo, (x,y)))
                
                
                #casas com nomes
                if caractere == '4':
                    self.grupo.add(Parede(self.banco, (x,y)))
                if caractere == 's':
                    self.grupo.add(Parede(self.salao, (x,y)))
                if caractere == 'b':
                    self.grupo.add(Parede(self.bar, (x,y)))


    def atualizar_tela(self, screen):
        # screen.fill((255,255,255))
        self.grupo.update()
        self.grupo.draw(screen)
        self.grupo_quebravel.update()
        self.grupo_quebravel.draw(screen)

    # nosso mapa tem 600x640 e o arquivo tem 15 colunas e 16 filas
    # Assim, cada desenho dos sprites é 40x40 pixels (40x15 = 600, 40x16 = 640)
    def conversorPixel(self, linha, coluna):
        return (linha * 40, coluna * 40)