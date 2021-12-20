import pygame as pg

class Tiro:
    """
    Classe de tiro do player
    """
    def __init__(self, win, x, y,direcao):
        self.win = win
        self.x = x
        self.y = y
        self.direcao = direcao
        self.largura = 5
        self.altura = 5
        self.cor = (41,41,41)
        self.rect = pg.Rect(x, y, 7, 7);
        self.loops=0

    def cooldown(self):
        """
        Método de deixar o Cool Down da bala
        """
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def draw(self):
        """
        Desenhar bala
        """
        self.rect.center = [self.x, self.y]
        pg.draw.rect(self.win, self.cor, self.rect)

    def colisao(self, obj, colidor):
        """
        verificar colisão com player
        """
        return obj.rect.colliderect(colidor)

    
    def colisao_plataforma(self, lista_plataforma: list, lista_quebravel: list, nivelQuebravel):
        """
        Método de colisão da bala com o barril
        """
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

    def movimento(self, vel):
        """
        Verificar qual direção o personagem está
        """

        if self.direcao == "baixo":
            self.y += vel
        elif self.direcao == "cima":
            self.y -= vel
        elif self.direcao == "direita":
            self.x += vel 
        elif self.direcao == "esquerda":
            self.x -= vel 

        
        #teleporta a tela para o outro lado da tela
        if self.y<0:
            self.loops+=1
            self.y = 640
        if self.y>640:
            self.loops+=1
            self.y = 0

    def fora_tela(self, altura):
        """
        Método de verificar se está fora de tela
        """
        return not (self.y <= altura and self.y >= 0)
