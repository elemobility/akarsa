# Generated by Django 3.1.13 on 2022-02-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20220223_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo_product',
            name='crosssell_product',
            field=models.ManyToManyField(blank=True, null=True, related_name='crosssell', to='customer.Product'),
        ),
    ]
