# Generated by Django 2.2.1 on 2022-05-23 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20220523_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='almacen',
            name='proveedor',
        ),
    ]
