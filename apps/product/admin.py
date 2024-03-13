from django.contrib import admin

from .models import Category, Product


class CategoryModelAdmin(admin.ModelAdmin):
    fields = ['name_uz', 'name_ru', 'name_en', 'parent']
    # exclude = ['slug']


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Product)
