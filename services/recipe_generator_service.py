from typing import List
from pydantic import BaseModel
from openai import AsyncOpenAI, DefaultAioHttpClient
from settings import Settings

settings = Settings()

class RecipeResponse(BaseModel):
  title: str
  ingredients: str
  instructions: str
  cooking_time: int
  difficulty: str

class AsyncRecipeGeneratorService:
  async def generate_recipe_by_ingredients(self, ingredients: List[str]) -> dict:
    prompt_instructions = "Você é um chef de cozinha"
    prompt_text = "Gere uma receita com os seguintes ingredientes:\n"
    prompt_text += "\n".join([f"- {ingredient}" for ingredient in ingredients])

    async with AsyncOpenAI(api_key=settings.openai_api_key, http_client=DefaultAioHttpClient()) as client:
      response = await client.responses.parse(
        model="gpt-5-nano",
        reasoning={"effort": "minimal"},
        instructions=prompt_instructions,
        input=prompt_text,
        store=False,
        text_format=RecipeResponse
      )

    recipe = response.output_parsed
    return recipe
