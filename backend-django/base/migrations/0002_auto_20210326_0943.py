# Generated by Django 3.1.7 on 2021-03-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True),
        ),
    ]
