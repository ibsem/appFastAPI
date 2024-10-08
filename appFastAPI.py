from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

# Conectando ao MongoDB (local ou remoto)
client = MongoClient("mongodb://localhost:27017/")
db = client['databaseteste']
colecao = db['colecaoteste']

# Instância do FastAPI
app = FastAPI()

# Definir o formato dos dados que virão via request
class Dados(BaseModel):
    nome: str
    idade: int
    cidade: str

# Rota para adicionar um documento ao MongoDB
@app.post("/adicionar_dados/")
async def adicionar_dados(dados: Dados):
    try:
        # Criando o dicionário com os dados recebidos no formato JSON
        novo_documento = {
            "nome": dados.nome,
            "idade": dados.idade,
            "cidade": dados.cidade
        }

        # Inserindo o documento no MongoDB
        resultado = colecao.insert_one(novo_documento)

        # Retornando o ID do documento inserido
        return {"msg": "Dados inseridos com sucesso", "id": str(resultado.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rota para listar todos os documentos do MongoDB
@app.get("/listar_dados/")
async def listar_dados():
    try:
        # Buscando todos os documentos na coleção
        documentos = colecao.find()
        resultado = []
        
        # Formatando o resultado para uma lista de dicionários
        for documento in documentos:
            documento['_id'] = str(documento['_id'])  # Convertendo o ObjectId para string
            resultado.append(documento)
        
        return {"dados": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
