print(" >>>> Utilizando classe \n >>> Cadastrando dog \n")
class dog:                   #class uma classe, tá facil poh

    def imprimir(self, nome, cor ): #declarando um metodo   
        print(f"nome do dog: {nome} \n cor da pelugem: {cor}")


objeto = dog()              #instanciando o objeto do tipo pessoa
objeto.imprimir('volkswagen', 'loiro')      #chamando o metodo e adicionando um atributo para o objeto





print(" \n \n \n >>>> Utilizando Classe com o Metodo tipo init() \n >>> Cadastrnado Pessoa \n")
class Pessoa:

    def __init__(self, cpf, nome, idade):    #chamado no mommento da instancia
        self._cpf = cpf
        self.nome = nome
        self.idade = idade

    def imprimir(self):                 #por conta dos objetos estarem sendo guardados em (self.), não é necessario chamar nome e idade, apenas (self)
        print(f" \n Pessoa Cadastrado\n Seja bem vindo {self.nome} \n")


pessoaCpf = input("  Digite o seu Cpf: ")
pessoaNome = input("  Digite o seu nome: ")
pessoaIdade = input("  Digite sua idade: ")

pessoa1 = Pessoa(pessoaCpf, pessoaNome, pessoaIdade)  #com o init os atributos são colocado na hr da instanciação
pessoa1.imprimir()                  #diferente do init, é necessario chamar o imprimir





print(" \n \n \n >>>> Utilizando Herança \n >>> Cadastrando Funcionario \n")
class Funcionario(Pessoa):          #pega os objetos da classe pai (Pessoa)

    def __init__(self, matricula, salario):
       self.matricula = matricula
       self.salario = salario

    def imprimirDados(self):        #por todos os itens estarem armazenados no self (self.cpf e o resto), só o self já chama tudo
        print(f" \n nome: {self.nome} \n cpf: {self.cpf} \n idade {self.idade} \n matricula {self.matricula} \n salario: {self.salario}")


funMatrticula= input("  Digite a id da sua matricula: ")
funSalario = input("  Digite seu salario: ")
funCpf = input("  Digite seu CPF: ")
funNome = input("  Digite seu nome: ")
funIdade = input("  Digite sua idade: ")


f1 = Funcionario(funMatrticula, funSalario)         #coisa original da classe funcionario
f1.cpf = funCpf             #f1 utilizando o cpf objeto de pessoa para armazenar o seu cpf
f1.nome = funNome
f1.idade = funIdade

f1.imprimirDados()

