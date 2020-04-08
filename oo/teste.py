"""
Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar
    >>> motor.velocidade
    1
    >>> motor.acelerar
    >>> motor.velocidade
    2
    >>> motor.acelerar
    >>> motor.velocidade
    3
    >>> motor.frear
    >>> motor.velocidade
    1
    >>> motor.frear
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Norte'
    >>> carro = Carro()
    >>> carro.calcular_velocidade
    0
    >>> carro.acelerar
    >>> carro.calcular_velocidade
    1
    >>> carro.acelerar
    >>> carro.calcular_velocidade
    2
    >>> carro.frear
    >>> carro.calcular_velocidade
    0
    >>> carro.calcular_direcao
    'Norte'
    >>> carro.girar_a_direita
    >>> carro.calcular_direcao
    'Leste'
    >>> carro.girar_a_esquerda
    >>> carro.calcular_direcao
    'Norte'
    >>> carro.girar_a_esquerda
    >>> carro.calcular_direcao
    'Oeste'
"""
from oo.carro import Motor, Direcao, Carro