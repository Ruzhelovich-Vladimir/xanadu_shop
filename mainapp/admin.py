from django.contrib import admin
from .models import Brand, Package, Classification, Country, Strong, Style, Product, PayForms, Warehouse, WarehouseStocks

admin.site.register(Brand)
admin.site.register(Package)
admin.site.register(Classification)
admin.site.register(Country)
admin.site.register(Strong)
admin.site.register(Style)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(WarehouseStocks)
