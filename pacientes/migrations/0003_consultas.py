# Generated by Django 5.1.6 on 2025-02-15 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_tarefas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humor', models.PositiveIntegerField()),
                ('registro_geral', models.TextField()),
                ('video', models.FileField(upload_to='video')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('tarefas', models.ManyToManyField(to='pacientes.tarefas')),
            ],
        ),
    ]
