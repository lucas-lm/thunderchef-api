from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from .services.recipe_generator_service import AsyncRecipeGeneratorService
from .settings import Settings

settings = Settings()
app = FastAPI()

class RecipeRequest(BaseModel):
    ingredients: List[str]
    style: str

class RecipeGenerated(BaseModel):
  title: str
  ingredients: str
  instructions: str
  cooking_time: int
  difficulty: str
  image_url: str = "https://picsum.photos/600/300"

@app.post('/recipes/generate', response_model=RecipeGenerated)
async def generate_recipe(recipe_request: RecipeRequest):
    recipe_generator_service = AsyncRecipeGeneratorService()
    recipe_response = await recipe_generator_service.generate_recipe_by_ingredients(recipe_request.ingredients)
    return recipe_response
