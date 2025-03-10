from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "mundo"}


# http://127.0.0.1:8000/items/1000?q=5
@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# http://localhost:8000/calculadora?operando_1=4&&operando_2=6
@app.get('/calculadora')
def calcular(operando_1:float, operando_2:float):
    return {'suma': operando_1 + operando_2}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}