from rest_framework import serializers
from .models import Meal, Ingredient, Menu

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'vegetarian', 'meal')

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'meals', 'id')

class MealSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    menus = MenuSerializer(many=True, read_only=True)
    class Meta:
        model = Meal
        fields = ('id', 'name', 'ingredients', 'menus')
