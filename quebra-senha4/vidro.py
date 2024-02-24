import subprocess
import itertools

def testar_senha(arquivo_rar, senha):
    try:
        resultado = subprocess.run(['C:\\Program Files\\WinRAR\\rar.EXE', 'x', '-p' + senha, '--', arquivo_rar], check=True)
        
        # Verificar o código de saída
        if resultado.returncode == 0:
            return True  # Senha correta
        elif resultado.returncode == 11:
            return False  # Senha incorreta
        else:
            print(f'Erro desconhecido: {resultado.stderr}')
            return False  # Outro erro
    except subprocess.CalledProcessError as e:
        print(f'Erro desconhecido: {e}')
        return False  # Erro ao chamar subprocess

def quebrar_senha_rar(arquivo_rar, comprimento_maximo=12, prefixo='skid', arquivo_historico='historico_senhas.txt'):
    # Obtendo a senha
    caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ!@#$%^&*()-_+=<>?/'

    try:
        # Carregar a última senha testada do histórico se existir
        with open(arquivo_historico, 'r') as historico_file:
            ultima_senha_testada = historico_file.read().strip()
    except FileNotFoundError:
        ultima_senha_testada = ""

    for tentativa_senha in itertools.product(caracteres, repeat=comprimento_maximo - len(prefixo)):
        senha_completa = prefixo + ''.join(tentativa_senha)
        
        print(f'Tentando senha: {senha_completa}')

        if ultima_senha_testada and senha_completa <= ultima_senha_testada:
            continue  # Pular senhas já testadas

        if testar_senha(arquivo_rar, senha_completa):
            print(f'Senha encontrada: {senha_completa}')
            print(f'Arquivos extraídos com sucesso.')
            
            # Atualizar o arquivo de histórico com a última senha testada
        with open(arquivo_historico, 'w') as historico_file:
            historico_file.write(senha_completa)


if __name__ == "__main__":
    arquivo_rar = './CRAC.rar'
    quebrar_senha_rar(arquivo_rar, comprimento_maximo=12, prefixo='skid')
