from pydantic import BaseModel

class Carro(BaseModel):
    modelo: str
    marca: str
    ano: int