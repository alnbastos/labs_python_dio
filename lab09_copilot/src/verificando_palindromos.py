def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ").strip().lower()

    # remove espaços e caracteres especiais
    texto_limpo = "".join(c for c in texto if c.isalnum())

    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


resultado = verificar_palindromo()
print("É palíndromo?", resultado)
