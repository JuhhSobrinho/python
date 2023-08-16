lista = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]

numbpar = list(filter(lambda i : i%2 == 0, lista))
numbImpar = list(filter(lambda i : i%2 != 0, lista))


valor = 0 
for i in lista:
    valor = valor + i


print(f"soma de ttodos valores da lista: {valor}") 
print (f" lista: {lista} \n lista de numeros pares: {numbpar} \n lista de numeros impares: {numbImpar}")