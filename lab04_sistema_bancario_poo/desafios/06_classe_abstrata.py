from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def nome(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    @property
    def nome(self):
        return self.__class__.__name__

    def area(self):
        return self.lado ** 2


class Retangulo(Forma):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    @property
    def nome(self):
        return self.__class__.__name__

    def area(self):
        return self.base * self.altura


for forma in [Quadrado(4), Retangulo(6, 3)]:
    print(f'Forma: {forma.nome} | Área: {forma.area()}')
