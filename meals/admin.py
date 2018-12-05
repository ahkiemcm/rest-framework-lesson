from django.contrib import admin
from .models import Meal, Menu, Ingredient

admin.site.register([Meal, Menu, Ingredient])
