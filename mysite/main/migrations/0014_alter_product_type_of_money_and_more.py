# Generated by Django 4.1.7 on 2023-03-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_product_name_en_product_name_hy_product_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_of_money',
            field=models.CharField(choices=[('₽', 'Russian'), ('֏', 'Armenian'), ('$', 'American')], max_length=60, verbose_name='Type price name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_money_en',
            field=models.CharField(choices=[('₽', 'Russian'), ('֏', 'Armenian'), ('$', 'American')], max_length=60, null=True, verbose_name='Type price name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_money_hy',
            field=models.CharField(choices=[('₽', 'Russian'), ('֏', 'Armenian'), ('$', 'American')], max_length=60, null=True, verbose_name='Type price name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_money_ru',
            field=models.CharField(choices=[('₽', 'Russian'), ('֏', 'Armenian'), ('$', 'American')], max_length=60, null=True, verbose_name='Type price name'),
        ),
    ]
