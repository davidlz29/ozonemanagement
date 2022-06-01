# Generated by Django 2.2.1 on 2022-05-23 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='cod_prov',
            field=models.CharField(max_length=255, null=True, verbose_name='Código proveedor'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='cod_sust',
            field=models.CharField(max_length=255, null=True, verbose_name='Código sustitución'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='iva',
            field=models.IntegerField(choices=[(1, 'Iva General (21%)'), (2, 'Iva Reducido (10%)'), (3, 'Iva Superreducido (4%)')], db_index=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='precio',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gastos.Proveedor'),
        ),
    ]
