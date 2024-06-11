# Generated by Django 5.0.4 on 2024-06-10 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RRHH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ausencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('motivo', models.CharField(max_length=100)),
                ('decripcion', models.TextField(blank=True, null=True)),
                ('justificada', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RRHH.empleado')),
            ],
            options={
                'verbose_name': 'ausencia',
                'verbose_name_plural': 'ausencias',
                'db_table': 'Ausencia',
                'ordering': ['id'],
            },
        ),
    ]
