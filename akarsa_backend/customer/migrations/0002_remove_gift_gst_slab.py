# Generated by Django 3.1.13 on 2022-02-23 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='gst_slab',
        ),
    ]