from sqladmin import ModelView

from models import Product, Category

class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.slug]



class CategoryAdmin(ModelView, model=Category):
    column_list = ['id', 'name', 'product_count']
    column_details_list = ['id', 'name', 'product_count']
    form_rules = [
        "name"
    ]
    can_export = False