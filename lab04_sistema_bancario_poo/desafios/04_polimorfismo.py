class Animal:
    voa = False

    def fazer_som(self):
        raise NotImplementedError('Subclasse deve implementar este método')


class Cachorro(Animal):
    def fazer_som(self):
        return 'Au au'


class Gato(Animal):
    def fazer_som(self):
        return 'Miau'


class Passaro(Animal):
    voa = True

    def fazer_som(self):
        return 'Piu piu'


animais: list[Animal] = [Cachorro(), Gato(), Passaro()]
for animal in animais:
    print(f'''
        O animal é: {animal.__class__.__name__}
        O som do animal é: {animal.fazer_som()}
        O animal voa? {'Sim' if animal.voa else 'Não'}
    ''')
