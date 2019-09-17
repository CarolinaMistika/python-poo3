def vogal(z):
    if not isinstance(z, str) or len(z) != 1:
        return False

    vogais = ["a", "e", "i", "o", "u"]
    return z.lower() in vogais

def consoante(z):
    if not isinstance(z, str) or len(z) != 1:
        return False

    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"]
    return z.lower() in consoantes

def verifica_letra():
    letra_digitada = input("Digite uma letra: ")
    if vogal(letra_digitada) == True:
        print("A letra é uma vogal!")
    if consoante(letra_digitada) == True:
        print("A letra é uma consoante!")
    else:
        print("Não é uma letra!")

verifica_letra()