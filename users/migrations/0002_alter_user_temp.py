# Generated by Django 3.2.3 on 2021-06-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='temp',
            field=models.TextField(blank=True),
        ),
    ]
