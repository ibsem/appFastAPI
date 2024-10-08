from pymongo import MongoClient

# Configuração: URL de conexão com o MongoDB
# Se você estiver usando um MongoDB local, a URL padrão seria:
# mongodb://localhost:27017/

# No caso de usar um MongoDB remoto, você colocaria a URL do servidor.
client = MongoClient("mongodb://localhost:27017/")

# Conectando ao banco de dados
# Caso o banco de dados não exista, o MongoDB o criará automaticamente na primeira inserção de dados
db = client['databaseteste']

# Acessando uma coleção (similar a uma tabela em um banco relacional)
colecao = db['colecaoteste']

# Inserindo um documento (similar a uma linha em uma tabela relacional)
novo_documento = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
result = colecao.insert_one(novo_documento)

# Confirmando a inserção
print(f"Documento inserido com ID: {result.inserted_id}")

# Fazendo uma consulta no banco de dados
# Aqui estamos buscando todos os documentos que têm "nome" igual a "João"
consulta = colecao.find({"nome": "João"})

# Exibindo os resultados da consulta
for doc in consulta:
    print(doc)

# Encerrando a conexão
client.close()
