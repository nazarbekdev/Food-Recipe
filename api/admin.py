from django.contrib import admin
from api.models.category import Category
from api.models.comment import Comment
from api.models.dish import Dish
from api.models.recipe_rate import RecipeRate
from api.models.saved_dish import SavedDish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(SavedDish)
class SavedDishAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'dish_id')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'dish_id', 'created_at')


@admin.register(RecipeRate)
class RecipeRate(admin.ModelAdmin):
    list_display = ('id', 'rate', 'user_id', 'dish_id')