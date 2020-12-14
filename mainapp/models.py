from django.db import models


class Brand(models.Model):
    name = models.CharField(verbose_name='product brand name',
                            max_length=32, unique=True)
    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(verbose_name='package type',
                            max_length=32, unique=True)

    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Classification(models.Model):
    name = models.CharField(verbose_name='product classification',
                            max_length=32, unique=True)

    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(verbose_name='country',
                            max_length=32, unique=True)

    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Strong(models.Model):
    name = models.CharField(verbose_name='Strong',
                            max_length=32, unique=True)

    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(verbose_name='Style',
                            max_length=32, unique=True)

    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='product name',
                            max_length=64, blank=False)
    code = models.CharField(
        verbose_name='external code', max_length=8)
    short_desc = models.CharField(verbose_name='short desc',
                                  max_length=32)
    description = models.TextField(
        verbose_name='description', blank=True)
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, null=True, blank=True)
    volume = models.DecimalField(
        verbose_name='volum', blank=True, max_digits=10, decimal_places=2)
    package_qty = models.PositiveSmallIntegerField(
        verbose_name='package qty', blank=False)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True)
    strong = models.ForeignKey(
        Strong, on_delete=models.CASCADE, null=True, blank=True)
    style = models.ForeignKey(
        Style, on_delete=models.CASCADE, null=True, blank=True)
    expiration = models.PositiveSmallIntegerField(
        verbose_name='expiration or zero', blank=False)
    filename = models.ImageField(
        upload_to='products_images', blank=True)

    '''
    Temporary fields. Separate tables will be created
    '''
    price = models.DecimalField(
        verbose_name='product price', max_digits=8, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(verbose_name='stock', default=0)

    def __str__(self):
        return f'{self.short_desc} {self.package} {self.volume}x{self.package_qty}'


class PayForms(models.Model):
    name = models.CharField(verbose_name='product name',
                            max_length=64, blank=False)
    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(verbose_name='product name',
                            max_length=64, blank=False)
    code = models.CharField(
        verbose_name='external code', max_length=8)

    def __str__(self):
        return self.name


class WarehouseStocks(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='stock', default=0)
