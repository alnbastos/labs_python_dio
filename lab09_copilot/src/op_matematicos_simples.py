def calcular():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input(
            "Escolha a operação (soma, subtracao, multiplicacao, divisao): "
        ).strip().lower()

        match operacao:
            case "soma":
                return num1 + num2
            case "subtracao":
                return num1 - num2
            case "multiplicacao":
                return num1 * num2
            case "divisao":
                if num2 == 0:
                    raise ZeroDivisionError(
                        "Divisão por zero não é permitida."
                    )
                return num1 / num2
            case _:
                raise ValueError("Operação inválida.")

    except ValueError as ve:
        raise ValueError(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        raise ZeroDivisionError(f"Erro: {zde}")
    except Exception as e:
        raise Exception(f"Ocorreu um erro inesperado: {e}")


resultado = calcular()
print("Resultado:", resultado)
