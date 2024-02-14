from django.db.models import Avg
from api.models.recipe_rate import RecipeRate


def recipe_rate(dish_id):
    rate_list = RecipeRate.objects.filter(dish_id=dish_id).aggregate(average_rate=Avg('rate'))
    return rate_list['average_rate']



