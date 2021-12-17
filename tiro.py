import pygame as pg

class Tiro:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

        self.largura = 5
        self.altura = 5
        self.cor = 'BLUE'
        self.rect = pg.Rect(x, y, 5, 5);

    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def draw(self):
        self.rect.center = [self.x, self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def colisao(self, obj, colidor):
        return obj.rect.colliderect(colidor)

    #Funcao da colisao bala-barril
    def colisao_plataforma(self, lista_plataforma: list, lista_quebravel: list, nivelQuebravel):

        #Loop para verificar se precisa diminuir a vida de um barril
        for objeto in lista_quebravel:

            #Caso a bala colida com o barril
            if (self.rect.colliderect(objeto[0].rect)):

                #Criamos uma lista com os caminhos das imagens do barril quebrando
                lista_path = ['imagens/barril_quebrado2.png','imagens/barril_quebrado1.png']

                #Diminuindo a vida do barril
                objeto[1] -= 1

                #Como as configuraoes do barril estao na variavel objeto[0], entao removemos o barril do Group,
                #Mudamos a variavel imagem dentro da variavel objeto[0] e colocamos o barril de volta no Group, dessa
                #vez com a imagem diferente
                nivelQuebravel.remove(objeto[0])
                objeto[0].image = pg.image.load(lista_path[objeto[1]-1]).convert_alpha()
                nivelQuebravel.add(objeto[0])

                #Caso o barril esteja com vida verada
                if (objeto[1] <= 0):

                    #Removemos o barril da lista com os barrils, da lista com os barrils quebraveis e do Group
                    lista_quebravel.pop(lista_quebravel.index(objeto))
                    lista_plataforma.pop(lista_plataforma.index(objeto[0].rect))
                    nivelQuebravel.remove(objeto[0])

                #Retornamos True para terminar a funcao
                return True

        #Loop para ver se colidiu com algum barril nao quebravel
        for plataforma in lista_plataforma:
            if (self.rect.colliderect(plataforma)):
                return True

        #Caso a bala nao tenha colidido com nada, retornamos False
        return False

    def movimento(self, vel, direcao):
        if direcao == pg.K_RCTRL:
            self.y += vel
        elif direcao == pg.K_f:
            self.y -= vel

    def fora_tela(self, altura):
        return not (self.y <= altura and self.y >= 0)
