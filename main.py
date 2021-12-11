#As linhas que possuem um comentario dizendo "codigo basico" em cima sao linhas que estao no codigo do main e nao estao relacionadas com a mecanica de colisao

#Linha 3 ate 9 eh codigo basico
import pygame as pg

class Player:
    def __init__(self, win, x, y):
        self.win = win

    #O player inicia como um quadrado em vez de pegarmos uma caracteristica por vez e montarmos o quadrado depois
        self.quadrado = pg.Rect(x,y,30,30)

    #Da linha 19 a 20, eh codigo base
        self.velocidade = 10
        self.cor = 'WHITE'

    #Funcao que vai verificar se o player colidiu com uma plataforma
    def colisao(self,lista_plataforma):

        #Loop para verificar se o player esta colidindo com uma plataforma
        for i in range(len(lista_plataforma)):

            #Caso o retangulo do player esteja colidindo com o retangulo da plataforma
            if (self.quadrado.colliderect(lista_plataforma[i])):

                #Retornamos True e a posicao da plataforma na lista_plataforma
                return True, i

        #Caso contrario, retornamos False e um valor escolhido aleatoriamente
        return False,0

    #Linha 38 ate 39 eh codigo basico
    def movimento(self, lista_plataformas):
        key = pg.key.get_pressed()

        #Variavel que diz se o jogador colidiu com uma plataforma
        colidiu:bool

        #Variavel, dentro da funcao, que ira receber o indice da plataforma que colidiu com o player
        indice:int

        #Linha 48 ate 49 eh codigo base
        if key[pg.K_a]:
            self.quadrado.x -= self.velocidade

            #Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            #Caso o jogador se mova para esquerda e colida com uma plataforma
            if (colidiu):
                #Modificamos a posicao do jogador para que fique a direita da plataforma
                self.quadrado.x = lista_plataformas[indice].x + lista_plataformas[indice].width

        if key[pg.K_d]:
            self.quadrado.x += self.velocidade

            #Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            #Caso o jogador se mova para direita e colida com uma plataforma
            if (colidiu):
                #Modificamos a posicao do jogador para que fique a esquerda da plataforma
                self.quadrado.x = lista_plataformas[indice].x - self.quadrado.width

        if key[pg.K_w]:
            self.quadrado.y -= self.velocidade

            # Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            # Caso o jogador se mova para frente e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique abaixo da plataforma
                self.quadrado.y = lista_plataformas[indice].y + lista_plataformas[indice].height

        if key[pg.K_s]:
            self.quadrado.y += self.velocidade

            #Chamando a funcao colisao da classe Player
            colidiu, indice = self.colisao(lista_plataformas)

            #Caso o jogador se mova para tras e colida com uma plataforma
            if (colidiu):
                # Modificamos a posicao do jogador para que fique em cima da plataforma
                self.quadrado.y = lista_plataformas[indice].y - self.quadrado.height

    #Linha 93 ate 94 codigo basico
    def draw(self):
        pg.draw.rect(self.win, self.cor, self.quadrado)

#Classe plataforma inventada para teste, nao eh muito importante para o codigo da colisao
#E eh bastante parecido com o codigo da classe Bala da branch Main no Github
class Plataform:
    quantidade_plataform = []
    def __init__(self,win,x,y,comprimento,altura):
        self.win = win
        self.plataforma = pg.Rect(x,y,comprimento,altura)
        self.cor = 'BLUE'
    def draw(self):
        pg.draw.rect(self.win,self.cor,self.plataforma)

#Linha 93 ate 96 eh codigo basico
def main():
    screen = pg.display.set_mode((640,480))
    clock = pg.time.Clock()
    player = Player(screen, 320, 240)

    #Criando 2 plataformas para testar colisao
    plataforma_superior_direita = Plataform(screen,50,50,150,20)
    plataforma_meio = Plataform(screen, 400, 300, 150, 20)

    #Linha 13 ate linha 108 eh codigo basico
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        #Chamando a funcao movimento do player, dentro dessa funcao movimento sera chamada a funcao colisao do player
        player.movimento([plataforma_superior_direita.plataforma, plataforma_meio.plataforma])

        #Linha 113 ate 115 eh codigo basico
        screen.fill((40,40,40))
        player.draw()

        #Desenhando as 2 plataformas de teste
        plataforma_superior_direita.draw()
        plataforma_meio.draw()

        #Linha 122 ate 129 eh codigo basico
        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()