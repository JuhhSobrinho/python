# python

Coleção de scripts Python independentes, em sua maioria exercícios e estudos. Cada arquivo resolve um problema isolado, como cálculos simples, listas, ordenação, classes, banco de dados SQLite, análise de dados com pandas e um conjunto de experimentos de quebra de senha de arquivos RAR. Não há um programa único: cada script é executado separadamente.

## Funcionalidades

- `app.py`: calcula um reajuste salarial conforme a faixa do salário (20%, 15%, 10% ou 5%).
- `BibliotecaBD.py`: cadastra funcionários em um banco SQLite (`aulaDB.db`) e exibe os registros, via terminal.
- `OlaMundo.py`: substitui, letra a letra, os caracteres de uma lista pelos caracteres de uma palavra, exibindo cada etapa.
- `automotivas.py`: calcula o valor de vendas de peças com desconto ou acréscimo e converte valores em dólar e euro para real.
- `buscaBi.py`: busca binária de um número em uma lista ordenada.
- `classeMetodo.py`: exemplos de classes, métodos, construtor `__init__` e herança (`Pessoa` e `Funcionario`).
- `imc.py`: calcula o IMC e exibe a classificação.
- `media.py`: calcula a média de duas notas, com conceito (A a D) e situação de aprovado ou reprovado.
- `ordenar`: implementações de ordenação por seleção e bubble sort.
- `pandinha.py`: cria um DataFrame pandas com estados e capitais, filtra os estados menos populosos, lê uma tabela de uma página da web com `pd.read_html` e plota um gráfico de barras com matplotlib.
- `percorrer.py`: percorre uma palavra caractere a caractere e monta o resultado a partir de uma lista de letras.
- `temp.py`: lê uma sequência de inteiros e informa se há valores repetidos (`OK` ou `ERROR`).
- `vetoresParImpar.py`: separa os números pares e ímpares de uma lista e soma seus valores.
- `quebra-senha/`, `quebra-senha3/`, `quebra-senha4/`: experimentos que tentam descobrir a senha de um arquivo `.rar` por força bruta, chamando o WinRAR/rar pela linha de comando. Ver Observações.

## Tecnologias

- Python 3
- Bibliotecas da biblioteca padrão: `sqlite3`, `itertools`, `subprocess`
- Bibliotecas externas: `pandas`, `matplotlib` (e `lxml` ou `bs4`, exigidos por `pd.read_html`; a confirmar)
- WinRAR / `rar` (apenas para a pasta `quebra-senha*`)

## Estrutura

```
python/
├── app.py                  reajuste salarial
├── BibliotecaBD.py         cadastro e consulta em SQLite
├── OlaMundo.py
├── automotivas.py          vendas de peças com conversão de moeda
├── buscaBi.py              busca binária
├── classeMetodo.py         classes e herança
├── imc.py
├── media.py
├── ordenar                 ordenação (seleção e bubble sort)
├── pandinha.py             pandas e matplotlib
├── percorrer.py
├── temp.py
├── vetoresParImpar.py
├── quebra-senha/           experimento com força bruta em .rar
├── quebra-senha3/          versão com histórico de tentativas
└── quebra-senha4/          versão com registro da última tentativa
```

## Como executar

Cada script é executado separadamente, a partir da pasta do projeto:

```bash
python app.py
python BibliotecaBD.py        # digite 1 para inserir ou 0 para exibir
python imc.py
python pandinha.py            # requer pandas, matplotlib e lxml
```

Não há arquivo `requirements.txt`. Para o `pandinha.py`, instale as dependências com `pip install pandas matplotlib lxml` (a confirmar).

## Observações

- Não há `requirements.txt` nem README por script. A finalidade de cada exercício foi inferida do código.
- Alguns scripts têm erros de lógica:
  - `app.py`, `media.py` e `automotivas.py` chamam `print(função(...))` em funções que não retornam valor, então imprimem `None` depois da mensagem.
  - `media.py` sobrescreve a função `print` na última linha (`print = (media)`), o que quebra os `print` seguintes. A variável `conceito` também não é definida em todos os casos.
  - `imc.py` usa `or` nas faixas de classificação, então qualquer IMC acima de 18.5 cai na primeira faixa seguinte (ex.: "peso ideal").
  - `BibliotecaBD.py` fecha a conexão em cada função, então a segunda operação na mesma execução falha. A função `createTable` existe, mas não é chamada pelo menu, e o nome do banco no código (`aulaDB.db`) difere do arquivo versionado (`aulaDb.db`).
- As pastas `quebra-senha*` contêm scripts que tentam abrir arquivos `.rar` testando combinações de caracteres. Também há arquivos `.rar` de teste e, em `quebra-senha3/` e `quebra-senha4/`, arquivos de histórico de tentativas, sendo o de `quebra-senha3/` muito grande (centenas de milhares de linhas). A finalidade desses experimentos é a confirmar. Eles devem ser usados apenas em arquivos de sua propriedade. Considere se esses arquivos devem continuar em um repositório público.
- O caminho do WinRAR nesses scripts é fixo (`C:\Program Files\WinRAR\rar.EXE`), e o `quebra-senha4` usa apenas `rar`, presente no PATH.
- O repositório também contém arquivos de metadados do Windows (`desktop.ini`) e binários (`.rar`, `.db`) que não são código-fonte.

## Autor

Desenvolvido por [Juliano Sobrinho](https://github.com/JuhhSobrinho).
