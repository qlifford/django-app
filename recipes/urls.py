from django.urls import path
from . import views

'app/model_view_type'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.home_index, name="index"),
    path('recipe/', views.RecipeListview.as_view(), name="recipes"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name="recipes-delete"),

    
    path('about/', views.about, name="about"),
]
