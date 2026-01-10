def par_ou_impar():
    try:
        num = int(input("Digite um número inteiro: "))
        return "par" if num % 2 == 0 else "impar", num
    except ValueError:
        raise ValueError("Entrada inválida. Digite um número inteiro.")


resultado, numero = par_ou_impar()
print(f"O número {numero} é {resultado}")
