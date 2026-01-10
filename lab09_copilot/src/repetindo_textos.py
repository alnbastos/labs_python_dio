def repetir_string():
    try:
        texto = input("Digite uma string: ")
        vezes = int(input("Digite um número inteiro: "))

        if vezes < 0:
            raise ValueError("O número de repetições não pode ser negativo.")

        return " ".join([texto] * vezes)
    except ValueError as ve:
        raise ValueError(f"Erro: {ve}")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado: {e}")


resultado = repetir_string()
print("Resultado:", resultado)
