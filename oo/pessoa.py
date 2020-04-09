class Pessoa:
    olhos = 2
    def __init__(self,*filhos,nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos = {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} aperto de mão'

class Mutante(Pessoa):
    olhos = 5

if __name__ == '__main__':
    pedro = Mutante(nome ='pedro')
    henrique = Homem(pedro,nome ='Henrique')
    print(Pessoa.cumprimentar(henrique))
    print(id(henrique))
    print(henrique.cumprimentar())
    print(pedro.cumprimentar())
    print(henrique.nome)
    print(henrique.idade)
    for filho in henrique.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Fernandes'
    del pedro.filhos
    print(pedro.__dict__)
    print(henrique.__dict__)
    print(pedro.olhos)
    print(Pessoa.olhos)
    print(Pessoa.__dict__)
    print((id(Pessoa.olhos),id(henrique.olhos),id(pedro.olhos)))
    print(Pessoa.metodo_estatico(), pedro.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), pedro.nome_e_atributos_de_classe(), henrique.nome_e_atributos_de_classe())
    print(pedro.olhos)