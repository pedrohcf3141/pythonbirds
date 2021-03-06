from unittest import TestCase
from oo.carro import Motor,Direcao,Carro

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar
        self.assertEqual(1,motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.velocidade = 5
        motor.frear
        self.assertEqual(3,motor.velocidade)