from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from api.models.dish import Dish

User = get_user_model()


class RecipeRate(models.Model):
    rate = models.PositiveIntegerField('Rate', validators=[MinValueValidator(1), MaxValueValidator(5)])
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recipe Rate'
        verbose_name_plural = 'Recipes Rate'
        unique_together = ('user_id', 'dish_id')

    def __str__(self):
        return f'{self.rate}'
