import pygame
import pygame as pg

class Balas:
    #lista de todas as balas do jogo
    lista_balas=[]

    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 10
        self.altura = 10
        self.cor = 'RED'
        self.rect=pygame.Rect(x,y,10,10);

        #coloca a bala na lista
        Balas.lista_balas.append(self)

    def draw(self):
        self.rect.center=[self.x,self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def remover(self):
        Balas.lista_balas.remove(self)
class Tiro:
    def __init__(self, win , x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 5
        self.altura = 5
        self.cor = 'BLUE'
        self.rect=pygame.Rect(x,y,5,5);
    
    def draw(self):
        self.rect.center=[self.x,self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def movimento(self, vel, direcao):
        if direcao == pg.K_RCTRL:
            self.y += vel
        elif direcao == pg.K_f:
            self.y -= vel

    def fora_tela(self, altura):
        return not (self.y <= altura and self.y >= 0)

class Player:
    COOLDOWN = 30 # Metade de um segundo pois o jogo é 60 fps

    def __init__(self, win, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita, tecla_tiro):
        self.win = win
        self.x = x
        self.y = y

        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita
        self.tecla_tiro = tecla_tiro
        
        self.quantidade_balas=0
        self.square = pygame.Rect(300, 230, 20, 20)
        self.largura = 20
        self.altura = 20
        self.vel = 10
        self.cor = 'WHITE'
        self.rect=pygame.Rect(x,y,20,20);

        self.tiros = []
        self.cool_down = 0

        self.balas = 0

    
    def control(self):
        keys = pg.key.get_pressed()

        if keys[self.tecla_esquerda]:
            self.x -= self.vel
        if keys[self.tecla_direita]:
            self.x += self.vel
        if keys[self.tecla_cima]:
            self.y -= self.vel
        if keys[self.tecla_baixo]:
            self.y += self.vel
        if keys[self.tecla_tiro]:
            self.tiro()
        self.movimento_tiro(self.vel)

    
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
        self.rect.center=[self.x,self.y]
        pg.draw.rect(self.win, self.cor, self.rect)
        for bala in self.tiros:
            bala.draw()
    

def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    player1 = Player(screen, 320, 240, pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_f)
    player2 = Player(screen, 220, 140, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_RCTRL)
    
    Balas(screen, 100, 80)
    Balas(screen, 200, 80)
    Balas(screen, 200, 180)
    Balas(screen, 100, 180)

    #posição do jogador no plano (x, y)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        
        player1.control()
        player2.control()

        screen.fill((40, 40, 40))

        player1.draw()
        player2.draw()

        #desenha todas as balas da lista
        for bala in Balas.lista_balas:
            bala.draw()

        pg.display.flip()
        clock.tick(30)

        #para cada bala na lista checa a colisão
        for bala in Balas.lista_balas:
            if bala.rect.colliderect(player1):
                player1.quantidade_balas+=1
                bala.remover()
                print(f"player1 tem {player1.quantidade_balas} balas")

            if bala.rect.colliderect(player2):
                player2.quantidade_balas+=1
                bala.remover()
                print(f"player2 tem {player2.quantidade_balas} balas")


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()