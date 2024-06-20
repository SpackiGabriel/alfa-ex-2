from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get('/recipes/{food}')
async def get_recipe(food: str):
    """
    Retrieve recipes based on the specified food.

    Args:
        food (str): The name of the food to search for recipes.

    Returns:
        dict: A dictionary containing the count of recipes found and a list of recipes.
    """
    try:
        url = f"https://forkify-api.herokuapp.com/api/search?q={food}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        recipes = data.get('recipes')

        if not recipes:
            raise HTTPException(status_code=404, detail="Nenhuma receita encontrada.")

        return {'count': len(recipes), 'recipes': recipes}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f'Erro ao fazer requisição para a API do Forkify: {e}')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro interno no servidor: {e}')
