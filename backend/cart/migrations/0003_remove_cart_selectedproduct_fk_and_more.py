# Generated by Django 4.0.5 on 2022-07-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_selectedproduct_fk_selectedproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='selectedProduct_FK',
        ),
        migrations.AddField(
            model_name='cart',
            name='selectedProduct_FK',
            field=models.ManyToManyField(blank=True, null=True, related_name='CartList', to='cart.selectedproduct'),
        ),
    ]
