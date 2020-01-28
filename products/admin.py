from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price', 'image')
    list_display = ('__str__', 'slug')


admin.site.register(Product, ProductAdmin)
