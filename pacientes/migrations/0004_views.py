# Generated by Django 5.1.6 on 2025-02-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visualizacao', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
