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
        # Carregar o histórico de senhas se existir
        with open(arquivo_historico, 'r') as historico_file:
            historico_senhas = set(historico_file.read().splitlines())
    except FileNotFoundError:
        historico_senhas = set()

    for tentativa_senha in itertools.product(caracteres, repeat=comprimento_maximo - len(prefixo)):
        senha_completa = prefixo + ''.join(tentativa_senha)
        
        print(f'Tentando senha: {senha_completa}')

        if senha_completa in historico_senhas:
            continue

        historico_senhas.add(senha_completa)

        if testar_senha(arquivo_rar, senha_completa):
            print(f'Senha encontrada: {senha_completa}')
            print(f'Arquivos extraídos com sucesso.')
            return
        
        with open(arquivo_historico, 'a') as historico_file:
            historico_file.write(f'{senha_completa}\n')

if __name__ == "__main__":
    arquivo_rar = './CRAC.rar'
    quebrar_senha_rar(arquivo_rar, comprimento_maximo=12, prefixo='skid')
