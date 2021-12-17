import pygame
import pygame as pg

class Tiro:
    def __init__(self, win , x, y,direcao):
        self.win = win
        self.x = x
        self.y = y
        self.direcao = direcao
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

    def movimento(self, vel):
        if self.direcao == "baixo":
            self.y += vel
        elif self.direcao == "cima":
            self.y -= vel

    def fora_tela(self, altura):
        return not (self.y <= altura and self.y >= 0)