import pandas as pd 
from matplotlib import pyplot as plt

def usandoUrl():
    url = 'https://www.covildodev.com.br/artigo/criar-dataframes-pandas-python'

    # url que mostra uma tabela com, colunas, estado sigra pipulação e capital

    dados = pd.read_html(url)       # lendo, capturando e colocando na variavel dados a tabela
    print(type(dados))
    print("Quantas tabelas encontradas", len(dados))
    return dados



def usandoDicionario():
    capitais = [['Acre', 'AC', '803500', 'Rio Branco'],
            ['Amapá', 'AP', '776600', 'Macapá'],
            ['Amazonas', 'AM', '3900000', 'Manaus'],
            ['Pará', 'PA', '8100000', 'Belém'],
            ['Rondônia', 'RO', '1700000', 'Porto Velho'],
            ['Roraima', 'RR', '505600', 'Boa Vista'],
            ['Tocantins', 'TO', '1500000', 'Palmas']]
    
    df = pd.DataFrame(capitais, columns=['Estado', 'Sigla', 'População', 'Capital'])

    novo_dado = pd.DataFrame({'Estado': ['São Paulo'], 'Sigla': ['SP'], 'População': [24], 'Capital': ['São Paulo']}) #Criação de uma DataFrame temporaria para juntar/concatenar na DF principal
    df = pd.concat([df, novo_dado], ignore_index=True)  #Aparentemente o append está sendo descontinuado, então o jeito é concatenar (concat())

    tabela = df

    df['População'] = df['População'].astype(int)       #Convertendo (astype()) os valores da coluna População para tipo Inteiros(int)
    df.sort_values(by='População', ascending=True, inplace=True)    #Ordena (sort_values()) em ordem crescente de acordo com os dados da "População"

    poucosHabitante = df.loc[(df['População'] <= 1000000)]  #Fazendo uma filtragem (loc[]) para saber os estados com menos população
    return poucosHabitante, tabela


resultDic = usandoDicionario()
resultUrl =  usandoUrl()  

print("\n Estados com Poucos habitantes \n", resultDic)
print("\n Utilizando URL \n", resultUrl)


# Criando o gráfico de barras com Matplotlib
plt.figure(figsize=(7, 5))
plt.bar(resultDic[1]['Estado'], resultDic[1]['População'])
plt.xlabel('Estado')
plt.ylabel('População')
plt.title('População por Estado')
plt.tight_layout() 

plt.show()