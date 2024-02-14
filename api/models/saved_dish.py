from django.db import models
from api.models.dish import Dish
from django.contrib.auth import get_user_model

User = get_user_model()


class SavedDish(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Saved Dish"
        verbose_name_plural = "Saved Dishes"
        unique_together = ("user_id", "dish_id")

    def __str__(self):
        return f"{self.user_id} - {self.dish_id}"
