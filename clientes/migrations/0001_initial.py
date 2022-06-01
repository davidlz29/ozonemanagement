# Generated by Django 2.2.1 on 2022-05-22 13:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('tipo_cliente', models.IntegerField(blank=True, choices=[(1, 'Profesional'), (2, 'Particular')], db_index=True, default=1, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellidos', models.CharField(max_length=255)),
                ('tipo_documento', models.IntegerField(blank=True, choices=[(1, 'Nif'), (2, 'Nie'), (3, 'Cif')], db_index=True, default=3, null=True)),
                ('num_documento', models.CharField(blank=True, max_length=9, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('dir_calle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calle')),
                ('dir_numero', models.CharField(blank=True, max_length=255, null=True, verbose_name='Número')),
                ('dir_piso', models.CharField(blank=True, max_length=255, null=True, verbose_name='Piso/Planta')),
                ('codigo_postal', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Télefono')),
                ('movil', models.CharField(blank=True, max_length=20, null=True)),
                ('web', models.CharField(blank=True, max_length=255, null=True)),
                ('profesion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_alta', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('sexo', models.IntegerField(blank=True, choices=[(1, 'Indefinido'), (2, 'Hombre'), (3, 'Mujer')], db_index=True, default=1, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
                ('cod_provincia', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'provincia',
                'verbose_name_plural': 'provincias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='TipoDocumentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('code', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'tipo documento',
                'verbose_name_plural': 'tipo documentos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nombre', models.CharField(max_length=255)),
                ('cod_poblacion', models.CharField(max_length=255)),
                ('cod_provincia', models.CharField(max_length=255)),
                ('provincias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Provincias')),
            ],
            options={
                'verbose_name': 'poblacion',
                'verbose_name_plural': 'poblacion',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('etiqueta', models.CharField(max_length=255)),
                ('fecha_foto', models.DateField(default=django.utils.timezone.now)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'fotos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('etiqueta', models.CharField(max_length=255)),
                ('fecha_documento', models.DateField(default=django.utils.timezone.now)),
                ('documento', models.FileField(blank=True, null=True, upload_to='documentos_cliente')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
                ('tipodocumento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.TipoDocumentos')),
            ],
            options={
                'verbose_name': 'documento',
                'verbose_name_plural': 'documentos',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='poblacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Poblacion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='provincias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Provincias'),
        ),
    ]
