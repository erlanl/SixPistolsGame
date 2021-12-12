import pygame
import pygame as pg
from pygame.locals import *
import mapa
import random
from interface import pontuacao
from interface import texto
import pygame.font
import os


class Balas:
    # lista de todas as balas do jogo
    lista_balas = []

    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 10
        self.altura = 10
        self.cor = 'YELLOW'
        self.rect = pygame.Rect(x, y, 10, 10);

        # coloca a bala na lista
        Balas.lista_balas.append(self)

    def draw(self):
        self.rect.center = [self.x, self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def remover(self):
        Balas.lista_balas.remove(self)


class Tiro:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 5
        self.altura = 5
        self.cor = 'BLUE'
        self.rect = pygame.Rect(x, y, 5, 5);

    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def tiro(self):
        if (self.balas < 6):
            if self.cool_down == 0:
                bala = Tiro(self.win, self.x, self.y)
                self.tiros.append(bala)
                self.cool_down = 1
                self.balas += 1
            print(self.balas)

    def movimento_tiro(self, vel):
        vel = self.vel
        self.cooldown()
        for bala in self.tiros:
            bala.movimento(vel, self.tecla_tiro)

    def draw(self):
        self.rect.center = [self.x, self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def colisao_plataforma(self,lista_plataforma:list):
        for plataforma in lista_plataforma:
            if (self.rect.colliderect(plataforma.rect)):
                return True
        return False

    def movimento(self, vel, direcao,lista_plataforma:list):
        if direcao == pg.K_RCTRL:
            self.y += vel
            return self.colisao_plataforma(lista_plataforma)
        elif direcao == pg.K_f:
            self.y -= vel
            return self.colisao_plataforma(lista_plataforma)

    def fora_tela(self, altura):
        return not (self.y <= altura and self.y >= 0)


class Player:
    COOLDOWN = 30  # Metade de um segundo pois o jogo é 60 fps

    def __init__(self, win, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita, tecla_tiro):

        self.win = win
        self.x = x
        self.y = y

        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita
        self.tecla_tiro = tecla_tiro
        self.vel = 10
        self.quantidade_balas = 0
        self.rect = pg.Rect(x, y, 30, 30)
        self.velocidade = 10
        self.cor = 'WHITE'

        self.tiros = []
        self.cool_down = 0

        self.balas = 0

    # Funcao que vai verificar se o player colidiu com uma plataforma
    def colisao(self, lista_plataforma):

        # Loop para verificar se o player esta colidindo com uma plataforma
        for i in range(len(lista_plataforma)):

            # Caso o retangulo do player esteja colidindo com o retangulo da plataforma
            if (self.rect.colliderect(lista_plataforma[i])):
                # Retornamos True e a posicao da plataforma na lista_plataforma
                return True, i

        # Caso contrario, retornamos False e um valor escolhido aleatoriamente
        return False, 0


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

        if keys[self.tecla_esquerda]:
            self.rect.x -= self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para esquerda e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique a direita da plataforma
                self.rect.x = lista_plataformas[indice].x + lista_plataformas[indice].width

        if keys[self.tecla_direita]:
            self.rect.x += self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para direita e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique a esquerda da plataforma
                self.rect.x = lista_plataformas[indice].x - self.rect.width

        if keys[self.tecla_cima]:
            self.rect.y -= self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para frente e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique abaixo da plataforma
                self.rect.y = lista_plataformas[indice].y + lista_plataformas[indice].height

        if keys[self.tecla_baixo]:
            self.rect.y += self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para tras e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique em cima da plataforma
                self.rect.y = lista_plataformas[indice].y - self.rect.height

        if keys[self.tecla_tiro]:
            self.tiro()

        self.movimento_tiro(self.vel, lista_plataformas)

    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def tiro(self):
        if (self.quantidade_balas > 0):
            if self.cool_down == 0:
                bala = Tiro(self.win, self.rect.center[0], self.rect.center[1])
                self.tiros.append(bala)
                self.cool_down = 1
                self.quantidade_balas -= 1
                print(self.quantidade_balas)

    def movimento_tiro(self, vel, lista_plataforma:list):
        vel = self.vel
        self.cooldown()
        for bala in self.tiros:
            if (bala.movimento(vel, self.tecla_tiro,lista_plataforma)):
                self.tiros.remove(bala)


    def draw(self):
        # self.rect.center=[self.x,self.y]
        pg.draw.rect(self.win, self.cor, self.rect)
        for bala in self.tiros:
            bala.draw()


def spawnarObjeto(screen, classe, evitaveis: list = [], borda: int = 0, quantidade: int = 1):
    # cria uma copia pra evitar a modificação da lista original
    evitaveis = evitaveis.copy()

    for i in range(quantidade):
        contagem_loops = 0
        lugar_valido = False
        # fecha o loop se achar um lugar valido ou tentar mais de 50 vezes
        while not lugar_valido and contagem_loops < 50:
            contagem_loops += 1
            # pega o tamanho da tela
            tamanho_tela_x, tamanho_tela_y = pygame.display.get_surface().get_size()

            # gera coordenadas aleatorias
            objeto_x = random.uniform(0, tamanho_tela_x)
            objeto_y = random.uniform(0, tamanho_tela_y)

            # cria o objeto
            objeto = classe(screen, objeto_x, objeto_y)
            # infla o retangulo pra simular a borda
            objeto.rect.inflate_ip(borda, borda)

            # checa se o objeto colide com algum evitavel
            lugar_valido = True
            for evitavel in evitaveis:
                if objeto.rect.colliderect(evitavel.rect):
                    lugar_valido = False
                    objeto.remover()
                    break
            # desinfla o retangulo
            objeto.rect.inflate_ip(-borda, -borda)
        # adiciona ao evitaveis para impedir que alguem spawne sobre ele
        evitaveis.append(objeto)


def main():
    spawn_cooldown = 0
    screen = pg.display.set_mode((600, 640))
    nivel = mapa.Mapa('mapa.txt')

    quantidade_plataform = []

    clock = pg.time.Clock()

    player1 = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_f)
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_RCTRL)

    # as fontes estão na pasta Assets, pode escolher qualquer fonte com tipo de arquivo .ttf
    # escolhendo a fonte pra usar, o segundo argumento é o tamanho
    fonte_pontuacao = pg.font.Font(os.path.join('Assets/alarm clock.ttf'), 40)
    fonte_texto = pg.font.Font(os.path.join('Assets/SEASRN__.ttf'), 20)
    # os argumentos são a janela, a posicao x, posicao y, cor e a fonte
    pontuacao1 = pontuacao(screen, 10, 40, (255, 255, 255), fonte_pontuacao)
    pontuacao2 = pontuacao(screen, (screen.get_width() - 50), 40, (255, 255, 255), fonte_pontuacao)
    # os argumentos sao a janela, o texto, posicao x , posicao y, cor e a fonte
    id1 = texto(screen, 'Jogador 1', 10, 10, (255, 255, 255), fonte_texto)
    id2 = texto(screen, 'Jogador 2', (screen.get_width() - 135), 10, (255, 255, 255), fonte_texto)

    evitar_lista = []
    for objeto in nivel.grupo:
        quantidade_plataform.append(objeto.rect)
        evitar_lista.append(objeto)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # Chamando a funcao movimento do player, dentro dessa funcao movimento sera chamada a funcao colisao do player
        player1.movimento(quantidade_plataform, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
        player2.movimento(quantidade_plataform, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)


        screen.fill((40, 40, 40))
        player1.draw()
        player2.draw()
        nivel.atualizar_tela(screen)
        pontuacao1.draw()
        pontuacao2.draw()
        id1.draw()
        id2.draw()

        spawn_cooldown += 1
        if spawn_cooldown >= 90:
            spawn_cooldown = 0
            spawnarObjeto(screen, Balas, evitar_lista + Balas.lista_balas, 20)

        # desenha todas as balas da lista
        for bala in Balas.lista_balas:
            bala.draw()

        # para cada bala na lista checa a colisão
        for bala in Balas.lista_balas:
            if bala.rect.colliderect(player1.rect):
                player1.quantidade_balas += 1
                bala.remover()
                pontuacao1.set_valor(player1.quantidade_balas)
                print(f"player1 tem {player1.quantidade_balas} balas")

            if bala.rect.colliderect(player2.rect):
                player2.quantidade_balas += 1
                bala.remover()
                pontuacao2.set_valor(player2.quantidade_balas)
                print(f"player2 tem {player2.quantidade_balas} balas")

        pg.display.flip()
        clock.tick(30)

        pygame.display.update()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()
