# Generated by Django 4.1.7 on 2023-04-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_description_product_genre_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
