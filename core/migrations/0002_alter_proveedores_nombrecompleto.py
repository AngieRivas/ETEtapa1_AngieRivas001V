# Generated by Django 3.2.3 on 2021-07-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='nombrecompleto',
            field=models.CharField(max_length=100, verbose_name='Nombre completo'),
        ),
    ]
