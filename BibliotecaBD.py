import sqlite3
conect = sqlite3.connect('aulaDB.db')

#               criar tabela

def createTable(ddl_create):

    cursor = conect.cursor()
    cursor.execute(ddl_create)
    print(type(cursor))
    print("Tabela criada")
    print("Descrição: ", cursor.description)
    print("linhas afetadas: ", cursor.rowcount)
    cursor.close()
    conect.close()
 

#               Inserir itens a tabela

def insertInto(sql_insert, dados):

    cursor = conect.cursor()
    cursor.execute(sql_insert, dados)
    conect.commit()     #para confirmar a inserção/alteração 
    print(type(cursor))
    print("Dados Inseridos")
    print("Descrição: ", cursor.description)
    print("linhas afetadas: ", cursor.rowcount)
    cursor.close()
    conect.close()



#               Exibir a tabela

def exibir(sql_select):

    cursor = conect.cursor()
    cursor.execute(sql_select)
    resultados = cursor.fetchall()      # Recuperar todos os resultados
    for row in resultados:
        print("ID:", row[0])
        print("Nome:", row[1])
        print("Cidade:", row[2])
        print("Estado:", row[3])
        print("---")
    cursor.close()
    conect.close()






ddl_create = """
    CREATE TABLE FUNCIONARIO(
    id_func INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_funcionario TEXT NOT NULL,
    cidade TEXT,
    estado VARCHAR(2) NOT NULL
    );
"""


sql_insert = """
    INSERT INTO FUNCIONARIO 
    (nome_funcionario, cidade, estado)
    VALUES (?, ?, ?);
"""


sql_select = """
    SELECT * FROM FUNCIONARIO;
"""



escolha = input("Inserir (1) ou Exibir (0): ")

if escolha == "1":
    nome = input(" Digite seu nome: ")
    cidade = input(" Digite sua cidade: ")
    estado = input(" Digite seu estado (ex: SP ): ")

    dados = (nome, cidade, estado)

    insertInto(sql_insert, dados)
else:
    exibir(sql_select)