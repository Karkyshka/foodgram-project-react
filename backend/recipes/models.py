from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    """Список ингредиентов с возможностью поиска по имени."""
    name = models.CharField(verbose_name='Ингредиент', max_length=10)
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения', max_length=3
      )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Cписок тегов."""
    name = models.CharField(verbose_name='Тег', max_length=200)
    color = models.CharField(
        max_length=7, null=True
      )
    slug = models.CharField(unique=True, null=True, max_length=200)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Рецепты. Страница доступна всем пользователям.
    Доступна фильтрация по избранному, автору, списку покупок и тегам."""
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    author = models.ForeignKey(
        User, verbose_name='Автор рецета',
        on_delete=models.CASCADE, related_name='recipes', null=True
      )
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='Ингредиенты', null=True
      )
    name = models.TextField(
        verbose_name='Название блюда', max_length=200, null=True
      )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время готовки', null=True
      )
    text = models.TextField(verbose_name='Описание рецепта', null=True)
    image = models.ImageField(null=True)
    is_favorited = models.BooleanField(null=True)
    is_in_shopping_cart = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name
