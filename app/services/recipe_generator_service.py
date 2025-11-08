import httpx
from datetime import datetime
from typing import List
from pydantic import BaseModel
from openai import AsyncOpenAI, DefaultAioHttpClient
from ..settings import Settings


settings = Settings()

class RecipeResponse(BaseModel):
  title: str
  ingredients: str
  instructions: str
  cooking_time: int
  difficulty: str

class AsyncRecipeGeneratorService:
  
  async def _get_month_to_date_costs(self):
    openai_admin_key = settings.openai_admin_key
    start_time = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0).timestamp()
    start_time = int(start_time)
    async with httpx.AsyncClient(headers={"Authorization": f"Bearer {openai_admin_key}"}, timeout=None) as client:
      response = await client.get("https://api.openai.com/v1/organization/costs", params={"start_time": start_time, "limit": 30})
      json_response: dict = response.json()
      buckets = json_response.get("data")
      month_to_date_costs = 0
      if buckets:
        for bucket in buckets:
          results = bucket.get("results")
          if results and len(results) > 0:
            result = results[0]
            amount = result.get("amount")
            bucket_costs = amount.get("value", 0) if amount else 0
            month_to_date_costs += bucket_costs

      print(f"MTD Costs: {month_to_date_costs} USD")
    return month_to_date_costs
  
  async def _is_credit_healthy(self, threshold: int = 3):
    mtd_costs = await self._get_month_to_date_costs()
    is_fine = mtd_costs < threshold
    return is_fine

  async def generate_recipe_by_ingredients(self, ingredients: List[str]) -> dict:

    if settings.enable_cost_short_circuit:
      is_credits_healthy = await self._is_credit_healthy()
      if not is_credits_healthy:
        raise Exception("Credits reached to the limit :(")

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
