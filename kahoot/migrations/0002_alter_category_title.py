# Generated by Django 5.0.7 on 2024-08-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kahoot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]