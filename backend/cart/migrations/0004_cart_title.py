# Generated by Django 4.0.5 on 2022-07-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_selectedproduct_fk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
