# Generated by Django 4.1.4 on 2023-01-29 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_rename_productodsetalles_productodetalles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='codigo',
            field=models.IntegerField(editable=False, unique=True),
        ),
    ]
