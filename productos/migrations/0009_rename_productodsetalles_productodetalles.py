# Generated by Django 4.1.4 on 2023-01-29 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_alter_productos_codigo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductoDsetalles',
            new_name='ProductoDetalles',
        ),
    ]
