# Generated by Django 4.1.7 on 2023-02-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_category_name_en_category_name_hy_category_name_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForZhenya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='ForZhenya')),
            ],
        ),
    ]
