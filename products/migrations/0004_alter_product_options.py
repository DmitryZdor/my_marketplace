# Generated by Django 3.2.13 on 2023-05-15 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230503_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
