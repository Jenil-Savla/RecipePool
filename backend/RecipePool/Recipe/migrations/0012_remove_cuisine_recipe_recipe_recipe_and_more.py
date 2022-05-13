# Generated by Django 4.0.3 on 2022-05-10 13:26

import Recipe.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0011_alter_ingredient_image_alter_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuisine',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_cuisine', to='Recipe.cuisine'),
            preserve_default=False,
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
