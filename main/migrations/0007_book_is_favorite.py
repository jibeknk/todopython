# Generated by Django 3.1.7 on 2021-04-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210413_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]