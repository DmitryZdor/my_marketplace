# Generated by Django 3.2.13 on 2023-05-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='+7-***-***-**-**', max_length=255),
        ),
    ]
