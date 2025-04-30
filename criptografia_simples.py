
def cripto(frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + "@"
        elif letra in "Bb":
            tradutor = tradutor + "#"
        elif letra in "Cc":
            tradutor = tradutor + "3"
        elif letra in "Dd":
            tradutor = tradutor + "4"
        elif letra in "Ee":
            tradutor = tradutor + "5"
        elif letra in "Ff":
            tradutor = tradutor + "6"            
        else:
            tradutor = tradutor + letra
    return tradutor

print(cripto(input("Digite sua frase:")))