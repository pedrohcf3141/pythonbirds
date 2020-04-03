class Pesoa:
    def __init__(self,nome = None, idade = 33):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola Mundo{id(self)}'

if __name__ == '__main__':
    p = Pesoa('Henrique')
    print(Pesoa.cumprimentar(p))
    print(id(p) )
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Pedro'
    print(p.nome)
    print(p.idade)
