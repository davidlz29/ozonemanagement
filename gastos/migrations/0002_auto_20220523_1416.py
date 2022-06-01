# Generated by Django 2.2.1 on 2022-05-23 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='cod_postal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dir_calle',
            field=models.CharField(max_length=255, null=True, verbose_name='calle'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='num_documento',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='razon_social',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='tipo_documento',
            field=models.IntegerField(choices=[(1, 'Nif'), (2, 'Nie'), (3, 'Cif')], db_index=True, default=3, null=True),
        ),
    ]
