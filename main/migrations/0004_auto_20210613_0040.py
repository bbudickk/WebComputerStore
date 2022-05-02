# Generated by Django 3.2.3 on 2021-06-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_completeorder_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='id_product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='id_clients',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='status',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
