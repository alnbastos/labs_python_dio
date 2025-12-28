# RoboNomeador 3000 - Núcleo em Python (POO)

class Robo:
    def __init__(self, modelo1: str, modelo2: str):
        self.modelo1 = modelo1
        self.modelo2 = modelo2

    def nome_completo(self) -> str:
        return f"{self.modelo1}-{self.modelo2}"


entrada = input().strip()
modelos = entrada.split()

if len(modelos) != 2:
    print("Entrada invalida: devem ser dois modelos separados por espaço.")
else:
    modelo1, modelo2 = modelos

    if len(modelo1) > 30 or len(modelo2) > 30:
        print("Entrada invalida: os modelos devem ter no máximo "
              "30 caracteres.")
    else:
        robo = Robo(modelo1, modelo2)
        print(robo.nome_completo())
