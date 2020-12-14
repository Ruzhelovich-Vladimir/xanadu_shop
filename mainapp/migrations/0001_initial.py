# Generated by Django 2.2.17 on 2020-12-10 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='product brand name')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='product classification')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='country')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='package type')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='PayForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product name')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product name')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
                ('short_desc', models.CharField(max_length=32, unique=True, verbose_name='product name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('volume', models.DecimalField(blank=True, decimal_places=5, max_digits=5, verbose_name='volum')),
                ('package_qty', models.PositiveSmallIntegerField(verbose_name='package qty')),
                ('expiration', models.PositiveSmallIntegerField(verbose_name='expiration or zero')),
                ('filename', models.ImageField(blank=True, upload_to='products_images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='product price')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='stock')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Brand')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Classification')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Country')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Strong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Strong')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Style')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product name')),
                ('code', models.CharField(max_length=8, verbose_name='external code')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='stock')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='strong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Strong'),
        ),
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Style'),
        ),
    ]
