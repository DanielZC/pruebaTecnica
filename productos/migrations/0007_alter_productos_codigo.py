# Generated by Django 4.1.4 on 2023-01-29 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_productos_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='codigo',
            field=models.CharField(editable=False, max_length=40),
        ),
    ]
