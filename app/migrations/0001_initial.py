# Generated by Django 4.2.16 on 2024-09-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_link', models.CharField(max_length=255, unique=True)),
                ('long_link', models.CharField(max_length=255)),
            ],
        ),
    ]
