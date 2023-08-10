conceito = ''

nota1 = float(input("Sua primeira nota:"))
nota2 = float(input("Sua segunda nota:"))

def media (nota1, nota2):
    media = (nota1 ++ nota2)/2

    if media <= 10.0 and media >= 6.0:
        if media >=9.0 and media <= 10.0:
            conceito = 'A'
            return conceito
        
        elif media >= 7.5 and media <= 8.9:
            conceito = 'B'

        elif media >=6.0 and media <= 7.4:
            conceito = 'C'

        print(f"Aprovado media: {media} e conceito: {conceito}")


    else:
        if media >= 4.0 and media <= 5.9:
            conceito = 'D'

        else:
            conceito = 'C'

        print(f"Reprovado media: {media} e conceito: {conceito}")


result = media(nota1, nota2)

print = (media)

