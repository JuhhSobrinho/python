quant = int(input())
lista = []
petRept = []

for item in range(quant):
    numb = int(input())
    lista.append(numb)

    if lista[item] not in petRept:
         petRept.append(lista[item])


if len(lista) != len(petRept):
    print('ERROR')
else:
    print('OK')