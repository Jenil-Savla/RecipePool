# Generated by Django 4.0.3 on 2022-04-04 13:25

import Recipe.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=Recipe.models.upload_path_handler)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1.0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_ingredient', to='Recipe.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_shopping_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('instructions', models.TextField(max_length=255)),
                ('totalTime', models.TimeField()),
                ('url', models.URLField(null=True)),
                ('image', models.ImageField(upload_to=Recipe.models.upload_path_handler)),
                ('healthLabels', models.JSONField()),
                ('totalNutrients', models.JSONField()),
                ('calories', models.IntegerField()),
                ('cuisineType', models.CharField(max_length=50)),
                ('mealType', models.CharField(max_length=50)),
                ('dishType', models.CharField(max_length=50)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('missingIngredients', models.JSONField(null=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_likes', to='Recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1.0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_ingredient', to='Recipe.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_inventory', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Inventories',
            },
        ),
        migrations.CreateModel(
            name='IngredientList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1.0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredient', to='Recipe.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_list', to='Recipe.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_fav', to='Recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DietLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('calories', models.FloatField(default=0)),
                ('cholestrol', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('sugar', models.FloatField(default=0)),
                ('proteins', models.FloatField(default=0)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_log', to='Recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]