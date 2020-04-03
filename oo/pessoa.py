class Pesoa:
    def __init__(self,*filhos,nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo{id(self)}'


if __name__ == '__main__':
    pedro = Pesoa(nome ='pedro')
    henrique = Pesoa(pedro,nome ='Henrique')
    print(Pesoa.cumprimentar(henrique))
    print(id(henrique))
    print(henrique.cumprimentar())
    print(henrique.nome)
    print(henrique.idade)
    for filho in henrique.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Fernandes'
    del pedro.filhos
    print(pedro.__dict__)
    print(henrique.__dict__)
