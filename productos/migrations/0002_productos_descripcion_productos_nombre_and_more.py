# Generated by Django 4.1.4 on 2023-01-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='productos',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
