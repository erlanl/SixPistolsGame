import pygame
import pygame as pg
from pygame.locals import *
import mapa
import random
from interface import pontuacao
from interface import texto
import pygame.font
import os
from coletaveis import *

class Tiro:
    def __init__(self, win , x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 5
        self.altura = 5
        self.cor = 'BLUE'
        self.rect=pygame.Rect(x,y,5,5);
    
    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1


    def draw(self):
        self.rect.center=[self.x,self.y]
        pg.draw.rect(self.win, self.cor, self.rect)
    
    def colisao(self, obj, colidor):
        return obj.rect.colliderect(colidor)

    def colisao_plataforma(self,lista_plataforma:list, lista_quebravel:list, nivelQuebravel):
        for objeto in lista_quebravel:
            if (self.rect.colliderect(objeto[0].rect)):
                objeto[1] -= 1
                if (objeto[1] <= 0):
                    lista_quebravel.pop(lista_quebravel.index(objeto))
                    lista_plataforma.pop(lista_plataforma.index(objeto[0].rect))
                    nivelQuebravel.remove(objeto[0])
                return True

        for plataforma in lista_plataforma:
            if (self.rect.colliderect(plataforma)):
                return True

        return False

    def movimento(self, vel, direcao):
        if direcao == pg.K_RCTRL:
            self.y += vel
        elif direcao == pg.K_f:
            self.y -= vel

    def fora_tela(self, altura):
        return not (self.y <= altura and self.y >= 0)


class Player:
    COOLDOWN = 30 # Metade de um segundo pois o jogo é 60 fps

    def __init__(self, win, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita, tecla_tiro, obj,px,py,fonte, imagem):

        self.win = win
        self.x = x
        self.y = y
        self.imagem = pygame.image.load(imagem)

        self.pontos = pontuacao(win, px, py, (255, 255, 255), fonte)
        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita
        self.tecla_tiro = tecla_tiro
        self.vel = 10
        self.quantidade_balas=0
        # O player inicia como um quadrado em vez de pegarmos uma caracteristica por vez e montarmos o quadrado depois
        self.quadrado = pg.Rect(x, y, 30, 30)
        self.rect=self.quadrado
        # Da linha 19 a 20, eh codigo base
        self.velocidade = 10
        self.cor = 'WHITE'

        self.tiros = []
        self.cool_down = 0
        self.vida = 100

        self.inimigo = obj
        self.balas = 0

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

    def movimento(self, lista_plataformas, lista_quebravel, nivelQuebravel, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita):

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

        if keys[self.tecla_tiro]:
            self.tiro()

        self.movimento_tiro(self.vel, self.inimigo, lista_plataformas, lista_quebravel, nivelQuebravel)

    # Linha 93 ate 94 codigo basico
    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def tiro(self):
        if (self.quantidade_balas > 0):
            if self.cool_down == 0:
                bala = Tiro(self.win, self.rect.center[0],self.rect.center[1])
                self.tiros.append(bala)
                self.cool_down = 1
                self.quantidade_balas -= 1
                self.pontos.soma(-1)
                print(self.quantidade_balas)
            
    def Ponto_soma(self, valor):
        self.pontos.soma(valor)

    def movimento_tiro(self, vel, obj, lista_plataforma:list, list_quebravel:list, nivelQuebravel):
        vel = self.vel
        self.cooldown()
        for bala in self.tiros:
            bala.movimento(vel, self.tecla_tiro)
            if bala.colisao(bala, obj):
                self.tiros.remove(bala)
                self.vida -= 10
                print(self.vida)
                if self.vida <= 0:
                    self.inimigo.cor = 'RED'
                    print('morreu')
            elif (bala.colisao_plataforma(lista_plataforma, list_quebravel, nivelQuebravel)):
                self.tiros.remove(bala)

    def draw(self, screen):
        screen.blit(self.imagem, self.rect)
        for bala in self.tiros:
            bala.draw()
        self.pontos.draw()

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

def spawnarColetaveis(screen,evitar:list=[]):
    #so permite que 8 coletaveis existam no maximo
    if len(Coletaveis.lista_coletaveis)>=8:
        return None

    #pesos para probabilidade de spawnar
    pesos=[70,10,10,10]
    classes=[Balas,Velocidade,Velocidade_Tiro,Cadencia]

    escolhido=None

    soma_pesos=sum(pesos)
    rand=random.uniform(1,soma_pesos)

    soma_parcial=0
    #escolhe uma classe aleatoria com base nos pesos
    for i in range(len(pesos)):
        if pesos[i]+soma_parcial>rand:
            escolhido=classes[i]
            break
        soma_parcial+=pesos[i]
    
    spawnarObjeto(screen,escolhido,evitar,20)

def main():
    spawn_cooldown = 0
    screen = pg.display.set_mode((600, 640))
    nivel = mapa.Mapa('mapa.txt')
    tela_fundo = pygame.image.load('background.png')

    quantidade_plataform = []
    quantidade_plataformQuebravel = []

    clock = pg.time.Clock()

    fonte_pontuacao = pg.font.Font(os.path.join('Assets/alarm clock.ttf'), 40)
    fonte_texto = pg.font.Font(os.path.join('Assets/SEASRN__.ttf'), 20)

    player1 = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_f, None,(screen.get_width()-90),530,fonte_pontuacao,'cowboy_joaquim2.png' )
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_RCTRL, None,40,70,fonte_pontuacao, 'cowgirl_leila.png')
    player1.inimigo=player2
    player2.inimigo=player1

    # os argumentos sao a janela, o texto, posicao x , posicao y, cor e a fonte
    id1 = texto(screen, 'Jogador 1', (screen.get_width() - 175), 570, (255, 255, 255), fonte_texto)
    id2 = texto(screen, 'Jogador 2', 40, 40, (255, 255, 255), fonte_texto)




    evitar_lista=[player1, player2]
    for objeto in nivel.grupo:
        quantidade_plataform.append(objeto.rect)
        evitar_lista.append(objeto)
    for obj in nivel.grupo_quebravel:
        quantidade_plataformQuebravel.append([obj,5])
        quantidade_plataform.append(obj.rect)
        evitar_lista.append(obj)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT or (player1.vida <= 0 or player2.vida <= 0):
                done = True

        # Chamando a funcao movimento do player, dentro dessa funcao movimento sera chamada a funcao colisao do player
        player1.movimento(quantidade_plataform, quantidade_plataformQuebravel, nivel.grupo_quebravel, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
        player2.movimento(quantidade_plataform, quantidade_plataformQuebravel, nivel.grupo_quebravel, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)


        screen.blit(tela_fundo, (0,0))

        nivel.atualizar_tela(screen)

        id1.draw()
        id2.draw()

        spawn_cooldown+=1
        if spawn_cooldown >= 60:
            spawn_cooldown=0
            spawnarColetaveis(screen, evitar_lista+Coletaveis.lista_coletaveis)
            
        # desenha todas as balas da lista e checa colisão com os jogadores
        for coletavel in Coletaveis.lista_coletaveis:
            coletavel.draw(screen)
    
            if coletavel.rect.colliderect(player1.rect):
                coletavel.colisao_jogador(player1)
                player1.pontos.set_valor(player1.quantidade_balas)
                

            if coletavel.rect.colliderect(player2.rect):
                coletavel.colisao_jogador(player2)
                player2.pontos.set_valor(player2.quantidade_balas)

        player1.draw(screen)
        player2.draw(screen)

        pg.display.flip()
        clock.tick(30)

        pygame.display.update()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()
