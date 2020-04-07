class Motor:
    def __init__(self,velocidade = 0):
        self.velocidade = velocidade


    @property
    def acelerar (self):
        self.velocidade += 1
        return self.velocidade


    @property
    def freiar (self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
        return self.velocidade
