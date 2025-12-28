# RoboNomeador 3000 - Núcleo em Python (POO)

class Robo:
    def __init__(self, modelo1: str, modelo2: str):
        self.modelo1 = modelo1
        self.modelo2 = modelo2

    def nome_completo(self) -> str:
        return f"{self.modelo1}-{self.modelo2}"


def modelo_valido(modelo: str) -> bool:
    return 1 <= len(modelo) <= 30 and modelo.isascii()


entrada = input().strip()
modelos = entrada.split()

if len(modelos) != 2:
    print("Entrada invalida: devem ser dois modelos separados por espaço.")
else:
    modelo1, modelo2 = modelos

    if not modelo_valido(modelo1) and not modelo_valido(modelo2):
        print("Entrada invalida: os modelos devem ter entre 1 e 30 caracteres "
              "e não podem possuir acentuações.")
    else:
        robo = Robo(modelo1, modelo2)
        print(robo.nome_completo())
