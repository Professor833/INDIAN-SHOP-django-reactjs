# Generated by Django 3.1.7 on 2021-03-27 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210326_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='raing',
            new_name='rating',
        ),
    ]
