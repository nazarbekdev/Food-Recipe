from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class NotificationCreateRecipe(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_received')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_sent')
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_saved_recipe_notification(cls, to_user, from_user):
        notification = cls(
            to_user=to_user,
            from_user=from_user,
            notification_type='create_recipe'
        )
        notification.save()
        return notification
