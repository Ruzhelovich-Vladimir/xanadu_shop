from django.core.management.base import BaseCommand
from mainapp.models import Brand, Package, Classification, Country, Strong, Style, Product
from django.contrib.auth.models import User

import json
import os
from authapp.models import User

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    print(f'loading: {file_name}')
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


def fillTable(table, object_list):
    table.objects.all().delete()
    for object in object_list:
        elem = table(**object)
        elem.save()


class Command(BaseCommand):

    def handle(self, *args, **options):

        object_list = load_from_json('Brand')
        fillTable(Brand, object_list)

        object_list = load_from_json('Package')
        fillTable(Package, object_list)

        object_list = load_from_json('Сlassification')
        fillTable(Classification, object_list)

        object_list = load_from_json('Сountry')
        fillTable(Country, object_list)

        object_list = load_from_json('Strong')
        fillTable(Strong, object_list)

        object_list = load_from_json('Style')
        fillTable(Style, object_list)

        products = load_from_json('Product')
        Product.objects.all().delete()
        foreignkey_tbl_lst = ('Brand', 'Package',
                              'Classification', 'Country', 'Strong', 'Style')
        for product in products:
            for foreignkey_tbl in foreignkey_tbl_lst:
                foreignkey_tbl_name = product[foreignkey_tbl.lower()]
                foreignkey = globals()[foreignkey_tbl].objects.get(
                    name=foreignkey_tbl_name)
                product[foreignkey_tbl.lower()] = foreignkey
            new_product = Product(**product)
            try:
                new_product.save()
            except Exception as err:
                print(
                    f'Таблица - {foreignkey_tbl};\nЗначение - {foreignkey_tbl_name};\nКлюч - {foreignkey};\n {err}')

        # Создаем суперпользователя при помощи менеджера модели
        super_user = User.objects.create_superuser(
            'admin', 'admin@localhost', 'admin', age=45)
