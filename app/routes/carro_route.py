from fastapi import APIRouter
from app.models.carro import Carro
from app.database.database import db

router = APIRouter()

@router.post('/carro')
async def criar_carro(carro: Carro):
    resultado = await db.carro.insert_one(carro.dict())
    return { "id": str(resultado.inserted_id), "mensagem": "carro criado com sucesso" }

@router.get('/carros')
async def pegar_carro():
    carros = []
    async for carro in db.carro.find():
        carro['_id'] = str(carro['_id'])
        carros.append(carro)
    return carros