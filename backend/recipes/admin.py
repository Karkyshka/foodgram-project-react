from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Ingredient, Recipe, Tag, IngredientRecipe


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display= (
        'id', 'author', 'name', 'text',
        'cooking_time', 'pub_date',
    )


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    pass


@admin.register(IngredientRecipe)
class IngredientAdmin(ImportExportModelAdmin):
    list_display= (
        'recipe', 'ingredient')