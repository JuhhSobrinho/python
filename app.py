desconto=''

salario = float(input("seu salario:"))
desSalario = ''
result =''

def results (salario, desconto):
    desSalario = desconto * salario
    result = salario ++ desSalario
    print(f"Seu salario antes do reajuste {salario} \n O porcentual de almento aplicado {desconto} \n O valor aumentado {desSalario}\n O novo salario {result}")

if salario <= 280:
    desconto = 0.20

    print (results(salario, desconto))


elif salario > 280 and salario <= 700:
    desconto = 0.15

    print (results(salario, desconto))

    
elif salario > 700 and salario <= 1500:
    desconto = 0.10

    print (results(salario, desconto))


elif salario > 1500:
    desconto = 0.05

    print (results(salario, desconto))