class Bicicleta:
    def __init__(self, cor: str, modelo: str, ano: int, valor: float):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Parando a bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vruuuum!')

    def __str__(self):  # representação da classe
        return f'{self.__class__.__name__}: {', '.join([
            f'{chave}={valor}' for chave, valor in self.__dict__.items()
        ])}'


b1 = Bicicleta('vermelha', 'caloi', 2002, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1)
