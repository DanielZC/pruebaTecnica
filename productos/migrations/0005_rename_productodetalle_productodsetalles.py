# Generated by Django 4.1.4 on 2023-01-28 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_productodetalle_delete_producto_detalle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductoDetalle',
            new_name='ProductoDsetalles',
        ),
    ]