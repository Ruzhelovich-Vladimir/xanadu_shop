# Generated by Django 2.2.17 on 2020-12-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, verbose_name='volum'),
        ),
    ]