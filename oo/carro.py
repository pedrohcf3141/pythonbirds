class Direcao:
    def __init__(self,valor = 'Norte'):
        self.valor = valor

    @property
    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'
        return self.valor

    @property
    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        return self.valor


    def __str__(self):
        return self.valor


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


    def __str__(self):
        return str(self.velocidade)


class Carro:
    def __init__(self):
        self.direcao = Direcao()
        self.motor = Motor()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    @property
    def acelerar(self):
        return self.motor.acelerar
    @property
    def freiar(self):
        return self.motor.freiar

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
motor.freiar
print(motor)
motor.freiar
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
print(carro.calcular_direcao())
print(carro.calcular_velocidade())
carro.acelerar
carro.acelerar
print(carro.calcular_velocidade())
carro.girar_a_direita
print(carro.calcular_direcao())
carro.girar_a_direita
print(carro.calcular_direcao())
carro.girar_a_direita
print(carro.calcular_direcao())
carro.girar_a_esquerda
print(carro.calcular_direcao())