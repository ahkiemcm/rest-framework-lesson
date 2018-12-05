from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('meals', views.MealView)
router.register('ingredients', views.IngredientView)
router.register('menu', views.MenuView)

urlpatterns =[
    path('', include(router.urls))
]

