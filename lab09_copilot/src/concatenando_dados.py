def concatenar_dados():
    try:
        # Recebe os dados do usuário
        dado1 = str(input("Digite o primeiro dado: "))
        dado2 = str(input("Digite o segundo dado: "))

        # Retorna os dados concatenados com espaço
        return f"{dado1} {dado2}"
    except Exception as e:
        # Caso ocorra algum erro, lança TypeError
        raise TypeError(f"Não foi possível concatenar os dados: {e}")


# Exemplo de uso
resultado = concatenar_dados()
print("Resultado:", resultado)
