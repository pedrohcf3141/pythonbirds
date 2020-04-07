class Direcao:
    def __init__(self,valor = 'Norte'):
        self.__valor = valor

    @property
    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        if self.valor == 'Oeste':
            self.valor = 'Sul'
        if self.valor == 'Sul':
            self.valor = 'Leste'
        if self.valor == 'Leste':
            self.valor = 'Norte'
        return self.valor

    @property
    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        if self.valor == 'Oeste':
            self.valor = 'Norte'
        if self.valor == 'Sul':
            self.valor = 'Oeste'
        if self.valor == 'Leste':
            self.valor = 'Sul'
        return self.valor