from django.urls import path

from api.views.all_recipe import AllRecipe
from api.views.category import CategoryGenericAPIView
from api.views.comment_recipe import CommentRecipeGenericAPIView, CommentsRecipeGenericAPIView, CountSavedRecipeAPIView
from api.views.dish import CreateDishGenericAPIView, MyRecipeGenericAPIView, MyRecipeDetailGenericAPIView
from api.views.new_recipe import NewRecipeGetView
from api.views.notification_created_recipe import NotificationCreateGet
from api.views.notification_saved_recipe import NotificationSaveGet
from api.views.rate_to_recipe import RateToRecipeGenericAPIView
from api.views.recipe_with_category import RecipeDataList
from api.views.saved_recipe import SavedRecipeGenericAPIView, SavedRecipeDetailGenericAPIView, UnSaveRecipeAPIView, \
    SaveRecipePostView
from api.views.search_recipe import SearchRecipeListAPIView

urlpatterns = [
    path('create-dish', CreateDishGenericAPIView.as_view(), name='create-dish'),
    path('saved-recipe', SavedRecipeGenericAPIView.as_view(), name='saved-recipe'),
    path('saved-recipe-detail/<int:dish_id>', SavedRecipeDetailGenericAPIView.as_view(), name='saved-recipe-detail'),
    path('saved-recipe-post', SaveRecipePostView.as_view(), name='saved-recipe-post'),
    path('count-comment-saved-recipe/<int:dish_id>', CountSavedRecipeAPIView.as_view(), name='count-comment-saved-recipe'),
    path('unsave-recipe/<int:dish_id>', UnSaveRecipeAPIView.as_view(), name='unsave-recipe'),
    path('rateto-recipe', RateToRecipeGenericAPIView.as_view(), name='rateto-recipe'),
    path('category', CategoryGenericAPIView.as_view(), name='category'),
    path('search-recipe', SearchRecipeListAPIView.as_view(), name='search-recipe'),
    path('my-recipe', MyRecipeGenericAPIView.as_view(), name='my-recipe'),
    path('my-recipe-detail/<int:dish_id>', MyRecipeDetailGenericAPIView.as_view(), name='my-recipe-detail'),
    path('comment', CommentRecipeGenericAPIView.as_view(), name='comment'),
    path('comments/<int:dish_id>', CommentsRecipeGenericAPIView.as_view(), name='comments'),
    path('notification-create-get', NotificationCreateGet.as_view(), name='notification-create-get'),
    path('notification-save-get', NotificationSaveGet.as_view(), name='notification-save-get'),
    path('new-recipes-get/', NewRecipeGetView.as_view(), name='new-recipes-get'),
    path('recipe-data/<int:pk>', RecipeDataList.as_view(), name='recipe-data'),
    path('all-recipes/', AllRecipe.as_view(), name='all-recipes'),
]
