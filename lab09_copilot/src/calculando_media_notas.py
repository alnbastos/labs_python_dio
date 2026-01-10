def calcular_media():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        media = (nota1 + nota2 + nota3) / 3
        return media
    except ValueError:
        raise ValueError(
            "Entrada inválida. Digite números válidos para as notas."
        )


media = calcular_media()
print(f"A média das notas é: {media:.2f}")
