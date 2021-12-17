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

        self.parede_lados = pygame.image.load('imagens/40x40.png').convert_alpha()
        self.parede_obstaculo = pygame.image.load('imagens/3.png').convert_alpha()
        self.cercas_continuas = pygame.image.load('imagens/cercas_continuas.png').convert_alpha()
        self.cercas_continuas_cima = pygame.image.load('imagens/cercas_continuas_cima.png').convert_alpha()
        self.fim_cercas_continuas_direita_baixo = pygame.image.load('imagens/fim_cercas_continuas_direita_baixo.png')
        self.fim_cercas_continuas_direita_cima = pygame.image.load('imagens/fim_cercas_continuas_direita_cima.png')
        self.cerca_quina_superior_esquerda = pygame.image.load(
            'imagens/cerca_quina_superior_esquerda.png').convert_alpha()
        self.cerca_quina_superior_direita = pygame.image.load(
            'imagens/cerca_quina_superior_direita.png').convert_alpha()
        self.cerca_quina_inferior_esquerda = pygame.image.load(
            'imagens/cerca_quina_inferior_esquerda.png').convert_alpha()
        self.cerca_quina_inferior_direita = pygame.image.load(
            'imagens/cerca_quina_inferior_direita.png').convert_alpha()
        self.parede_invisivel = pygame.image.load('imagens/parede_invisivel.png').convert_alpha()
        self.casas_3 = pygame.image.load('imagens/40x40(3x).png').convert_alpha()

        # acessando o arquivo que contem o mapa em forma de texto
        arquivo = open(arquivo)
        self.textoMapa = arquivo.readlines()
        arquivo.close()

        # Acessando o mapa.txt linha por linha para substituir cada caractere por uma imagem
        linha_auxiliar = -1
        for linha in self.textoMapa:
            linha_auxiliar += 1
            coluna = -1
            for caractere in linha:
                coluna += 1

                # Convertendo os valores para pixel para saber a posição real na tela
                x, y = self.conversorPixel(coluna, linha_auxiliar)

                if caractere == '#':
                    self.grupo.add(Parede(self.parede_lados, (x, y)))
                if caractere == '=':
                    self.grupo.add(Parede(self.cercas_continuas, (x, y)))
                if caractere == '*':
                    self.grupo.add(Parede(self.cercas_continuas_cima, (x, y)))
                if caractere == '(':
                    self.grupo.add(Parede(self.fim_cercas_continuas_direita_baixo, (x, y)))
                if caractere == ')':
                    self.grupo.add(Parede(self.fim_cercas_continuas_direita_cima, (x, y)))
                if caractere == '-':
                    self.grupo.add(Parede(self.parede_obstaculo, (x, y)))
                if caractere == '|':
                    self.grupo_quebravel.add(Parede(self.parede_obstaculo, (x, y)))
                if caractere == '!':
                    self.grupo.add(Parede(self.cerca_quina_superior_esquerda, (x, y)))
                if caractere == '@':
                    self.grupo.add(Parede(self.cerca_quina_superior_direita, (x, y)))
                if caractere == '$':
                    self.grupo.add(Parede(self.cerca_quina_inferior_esquerda, (x, y)))
                if caractere == '%':
                    self.grupo.add(Parede(self.cerca_quina_inferior_direita, (x, y)))
                if caractere == 'i':
                    self.grupo.add(Parede(self.parede_invisivel, (x, y)))
                if caractere == '3':
                    self.grupo.add(Parede(self.casas_3, (x, y)))

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