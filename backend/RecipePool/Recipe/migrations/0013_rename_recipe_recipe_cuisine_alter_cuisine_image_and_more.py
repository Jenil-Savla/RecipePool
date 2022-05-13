# Generated by Django 4.0.3 on 2022-05-10 13:28

import Recipe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0012_remove_cuisine_recipe_recipe_recipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe',
            new_name='cuisine',
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Recipe.models.upload_path_handler),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(upload_to=Recipe.models.upload_path_handler),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=Recipe.models.upload_path_handler),
        ),
    ]
