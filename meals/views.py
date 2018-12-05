from rest_framework import viewsets
from .models import Meal, Ingredient, Menu
from .serializers import MealSerializer, IngredientSerializer, MenuSerializer

class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer