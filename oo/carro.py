NORTE ='Norte'
OESTE = 'Oeste'
SUL= 'Sul'
LESTE='Leste'


class Direcao:
    rotacao_a_direita_dct = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotacao_a_esquerda_dct = {NORTE:OESTE,OESTE:SUL,SUL:LESTE,LESTE:NORTE}

    def __init__(self):
        self.valor = NORTE



    @property
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def __str__(self):
        return self.valor


    @property
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0


    @property
    def acelerar (self):
        self.velocidade += 1


    @property
    def frear (self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)

    def __str__(self):
        return str(self.velocidade)


class Carro:
    def __init__(self):
        self.direcao = Direcao()
        self.motor = Motor()

    @property
    def calcular_velocidade(self):
        return self.motor.velocidade

    @property
    def calcular_direcao(self):
        return self.direcao.valor

    @property
    def acelerar(self):
        return self.motor.acelerar
    @property
    def frear(self):
        return self.motor.frear

    @property
    def girar_a_direita(self):
        return self.direcao.girar_a_direita

    @property
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda


print('Teste Motor')
motor = Motor()
print(motor)
motor.acelerar
print(motor)
motor.acelerar
motor.acelerar
print(motor)
motor.frear
print(motor)
motor.frear
print(motor)
print('Teste direcao')
direcao = Direcao()
print(direcao)
direcao.girar_a_direita
print(direcao)
direcao.girar_a_direita
print(direcao)
direcao.girar_a_direita
print(direcao)
direcao.girar_a_esquerda
print(direcao)
direcao.girar_a_esquerda
print(direcao)
direcao.girar_a_esquerda
print(direcao)

print('Teste Carro')
carro = Carro()
print(carro.calcular_direcao)
print(carro.calcular_velocidade)
carro.acelerar
carro.acelerar
print(carro.calcular_velocidade)
carro.girar_a_direita
print(carro.calcular_direcao)
carro.girar_a_direita
print(carro.calcular_direcao)
carro.girar_a_direita
print(carro.calcular_direcao)
carro.girar_a_esquerda
print(carro.calcular_direcao)
