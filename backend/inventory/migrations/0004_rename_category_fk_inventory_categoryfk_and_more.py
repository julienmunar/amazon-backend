# Generated by Django 4.0.5 on 2022-07-04 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='category_FK',
            new_name='categoryFk',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='rating_FK',
            new_name='ratingFk',
        ),
    ]
