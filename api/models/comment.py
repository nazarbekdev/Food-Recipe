from django.db import models
from django.contrib.auth import get_user_model
from api.models.dish import Dish

User = get_user_model()


class Comment(models.Model):
    text = models.TextField('Comment')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.user_id} - {self.dish_id}"
