from fastapi import FastAPI
from app.routes.carro_route import router as carro_router



app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": "API FUNCIONANDO"}

app.include_router(carro_router)