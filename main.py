from uuid import uuid4
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RecipeRequest(BaseModel):
    ingredients: List[str]
    style: str

@app.post('/recipes/generate')
def generate_recipe(recipe_request: RecipeRequest):
    random_id = str(uuid4())
    print(recipe_request)
    return {
        "id": random_id,
        "title": "Frango com Batata ao Forno",
        "ingredients": [
            {"name": "batata", "qty": "200g"},
            {"name": "frango", "qty": "300g"}
        ],
        "instructions": "1. Pré-aqueça o forno...\n2. ...",
        "cooking_time": 45,
        "difficulty": "fácil",
        "image_url": "https://picsum.photos/200"
    }
