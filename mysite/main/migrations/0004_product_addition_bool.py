# Generated by Django 4.1.7 on 2023-02-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='addition_bool',
            field=models.BooleanField(default=1, verbose_name='Press and key for show'),
            preserve_default=False,
        ),
    ]
