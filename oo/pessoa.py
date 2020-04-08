class Pessoa:
    olhos = 2
    def __init__(self,*filhos,nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos = {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    pedro = Homem(nome ='pedro')
    henrique = Pessoa(pedro,nome ='Henrique')
    print(Pessoa.cumprimentar(henrique))
    print(id(henrique))
    print(henrique.cumprimentar())
    print(henrique.nome)
    print(henrique.idade)
    for filho in henrique.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Fernandes'
    del pedro.filhos
    pedro.olhos = 3
    print(pedro.__dict__)
    print(henrique.__dict__)
    print(pedro.olhos)
    print(Pesoa.olhos)
    print(Pesoa.__dict__)
    print((id(Pesoa.olhos),id(henrique.olhos),id(pedro.olhos)))
    print(Pesoa.metodo_estatico(), pedro.metodo_estatico())
    print(Pesoa.nome_e_atributos_de_classe(), pedro.nome_e_atributos_de_classe(), henrique.nome_e_atributos_de_classe())
