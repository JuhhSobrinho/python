valorPeca = float(input("Valor da peça vendida: "))
quantidadePeca = int(input("Quantidade de peças vendidas: "))
valorNota = input("Valor da peça (ex: dolar, real ou euro): ")

desconto = input("Se houver desconto, qual o valor:")
acrecimo = input("Se houver acrecimo, qual o valor:")


def calVendas (peca, quantidade, nota, des=None, acrecimo=None):
    valBruto = quantidade * peca
    if des:
        valLiquido = valBruto - (valBruto * (float(des) / 100))
    elif acrecimo:
        valLiquido = valBruto + (valBruto * (float(acrecimo) / 100))
    else:
        valLiquido = valBruto


    print(f"Valor de vendas {valLiquido} em {nota}")

    if nota == 'euro':
        nota = 'real'
        valLiquido = valLiquido * 5.7
        print(f"Valor de vendas {valLiquido} em {nota}")


    elif nota == 'dolar':
        nota = 'real'
        valLiquido = valLiquido * 5
        print(f"Valor de vendas {valLiquido} em {nota}")


print(calVendas(valorPeca, quantidadePeca, valorNota, desconto, acrecimo))

