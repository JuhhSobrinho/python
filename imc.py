class pessoa:
    def __init__(self, dados):
        self.nome = dados[0]
        self.altura = float(dados[1])
        self.peso = float(dados[2])

    def imcCalcula(self):
        imc = self.peso / (self.altura ** 2)

        print(f" {self.nome} seu IMC é: {imc:.3f}")

        if imc <= 18.5:
            print("Você está abaixo do peso")
        elif imc > 18.5 or imc <= 24.9:
            print("Você está no peso ideal")
        elif imc > 24.9 or imc <= 29.9:
            print("Você está levemente acima do peso")
        elif imc > 29.9 or imc >= 34.9:
            print("Você está com obsidade grau I")
        elif imc > 34.9 or 39.9:
            print("Você está com obsidade grau II")
        else:
            print("Você está com obsidade grau III")


print("\n >>>> Calculo de IMC >>>> \n")
nome = input(" Digite seu nome: ")
altura = input(" Digite sua altura (ex: 1.50): ")
peso = input(" Digite seu peso (ex: 56): ")

dados = (nome, altura, peso)
ficha = pessoa(dados)

ficha.imcCalcula()