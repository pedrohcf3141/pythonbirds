class Pesoa:
    def cumprimentar(self):
        return f'Ola Mundo{id(self)}'

if __name__ == '__main__':
    p = Pesoa()
    print(Pesoa.cumprimentar(p))
    print(id(p) )
    print(p.cumprimentar())


