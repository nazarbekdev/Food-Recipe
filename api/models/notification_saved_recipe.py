from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class NotificationSaveRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_saved_recipe_notification(cls, user):
        notification = cls(
            user=user,
            notification_type='recipe_saved'
        )
        notification.save()
        return notification
