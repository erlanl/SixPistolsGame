# As linhas que possuem um comentario dizendo "codigo basico" em cima sao linhas que estao no codigo do main e nao estao relacionadas com a mecanica de colisao

# Linha 3 ate 9 eh codigo basico
import pygame
import pygame as pg
from pygame.locals import *
import mapa


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

        # O player inicia como um quadrado em vez de pegarmos uma caracteristica por vez e montarmos o quadrado depois
        self.quadrado = pg.Rect(x, y, 30, 30)

        # Da linha 19 a 20, eh codigo base
        self.velocidade = 10
        self.cor = 'WHITE'

    # Funcao que vai verificar se o player colidiu com uma plataforma
    def colisao(self, lista_plataforma):

        # Loop para verificar se o player esta colidindo com uma plataforma
        for i in range(len(lista_plataforma)):

            # Caso o retangulo do player esteja colidindo com o retangulo da plataforma
            if (self.quadrado.colliderect(lista_plataforma[i])):
                # Retornamos True e a posicao da plataforma na lista_plataforma
                return True, i

        # Caso contrario, retornamos False e um valor escolhido aleatoriamente
        return False, 0

    # Linha 38 ate 39 eh codigo basico

    def movimento(self, lista_plataformas, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita):

        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita

        keys = pg.key.get_pressed()

        # Variavel que diz se o jogador colidiu com uma plataforma
        colidiu: bool

        # Variavel, dentro da funcao, que ira receber o indice da plataforma que colidiu com o player
        indice: int

        # Linha 48 ate 49 eh codigo base
        if keys[self.tecla_esquerda]:
            self.quadrado.x -= self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para esquerda e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique a direita da plataforma
                self.quadrado.x = lista_plataformas[indice].x + lista_plataformas[indice].width

        if keys[self.tecla_direita]:
            self.quadrado.x += self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para direita e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique a esquerda da plataforma
                self.quadrado.x = lista_plataformas[indice].x - self.quadrado.width

        if keys[self.tecla_cima]:
            self.quadrado.y -= self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para frente e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique abaixo da plataforma
                self.quadrado.y = lista_plataformas[indice].y + lista_plataformas[indice].height

        if keys[self.tecla_baixo]:
            self.quadrado.y += self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para tras e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique em cima da plataforma
                self.quadrado.y = lista_plataformas[indice].y - self.quadrado.height

    # Linha 93 ate 94 codigo basico
    def draw(self):
        pg.draw.rect(self.win, self.cor, self.quadrado)

# Linha 93 ate 96 eh codigo basico
def main():
    screen = pg.display.set_mode((600, 640))
    nivel = mapa.Mapa('mapa.txt')

    quantidade_plataform = []

    clock = pg.time.Clock()

    player1 = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)

    for objeto in nivel.grupo:
        quantidade_plataform.append(objeto.rect)

    # Linha 13 ate linha 108 eh codigo basico
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # Chamando a funcao movimento do player, dentro dessa funcao movimento sera chamada a funcao colisao do player
        player1.movimento(quantidade_plataform, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
        player2.movimento(quantidade_plataform, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)

        # Linha 113 ate 115 eh codigo basico

        screen.fill((40, 40, 40))
        player1.draw()
        player2.draw()
        nivel.atualizar_tela(screen)

        # desenha todas as balas da lista
        for bala in Balas.lista_balas:
            bala.draw()

        # para cada bala na lista checa a colisão
        for bala in Balas.lista_balas:
            if bala.rect.colliderect(player1):
                player1.quantidade_balas += 1
                bala.remover()
                print(f"player1 tem {player1.quantidade_balas} balas")

            if bala.rect.colliderect(player2):
                player2.quantidade_balas += 1
                bala.remover()
                print(f"player2 tem {player2.quantidade_balas} balas")

        # Linha 122 ate 129 eh codigo basico
        pg.display.flip()
        clock.tick(30)

        pygame.display.update()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()
