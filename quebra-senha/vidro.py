import subprocess
import itertools

def quebrar_senha_rar(arquivo_rar, comprimento_maximo=10):
    # Obtendo a senha
    caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQSRTUVWXYZ!@#$%^&*()-_+=<>?/'
    
    for comprimento in range(1, comprimento_maximo + 1):
        for tentativa_senha in itertools.product(caracteres, repeat=comprimento):
            tentativa_senha = ''.join(tentativa_senha)
            
            try:
                # Chamando o comando rar diretamente com subprocess
                resultado = subprocess.run(['C:\\Program Files\\WinRAR\\rar.EXE', 'x', '-p' + tentativa_senha, '--', arquivo_rar])
                
                # Verificar o código de saída
                if resultado.returncode == 0:
                    print(f'Senha encontrada: {tentativa_senha}')
                    print(f'Arquivos extraídos com sucesso.')
                    return
                elif resultado.returncode == 11:
                    print(f'Senha incorreta: {tentativa_senha}')
                else:
                    print(f'Erro desconhecido: {resultado.stderr}')
            except subprocess.CalledProcessError as e:
                print(f'Erro desconhecido: {e}')

if __name__ == "__main__":
    arquivo_rar = './CRAC.rar'
    quebrar_senha_rar(arquivo_rar, comprimento_maximo=10)
