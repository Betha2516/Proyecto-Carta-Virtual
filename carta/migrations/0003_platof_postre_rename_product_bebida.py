# Generated by Django 5.1 on 2024-08-24 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0002_entrada'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatoF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('descripcion', models.CharField(default='', max_length=400)),
                ('img', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('descripcion', models.CharField(default='', max_length=400)),
                ('img', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Bebida',
        ),
    ]
