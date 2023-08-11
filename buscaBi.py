def busca(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        meio = (minimo + maximo) // 2

        print(meio)
        print(maximo)
        print(minimo)

        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True

    return False



valores = [11, 12, 13, 20, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 6, 7, 8, 9, 10]

print(valores)

listaOrdenada = sorted(valores)
listaOrdenadadois = valores.sort()

print(listaOrdenada)
print(listaOrdenadadois)


valor = int(input("Digite o número que deseja buscar na lista: "))

print(busca(valores, valor))

