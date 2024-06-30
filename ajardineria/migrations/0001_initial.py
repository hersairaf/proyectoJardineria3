# Generated by Django 5.0.6 on 2024-06-29 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apaterno', models.CharField(max_length=20)),
                ('amaterno', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('fono', models.CharField(max_length=45)),
            ],
        ),
    ]