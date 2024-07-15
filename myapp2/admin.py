from django.contrib import admin
from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']

    readonly_fields = ['date_added', 'rating']
    fieldsets = [
            (
                None,
                {
                    'classes': ['wide'],
                    'fields': ['name'],
                },
            ),

            (
                'Подробности',
                {
                    'classes': ['collapse'],
                    'description': 'Категория товара и его подробноеописание', 'fields':['category', 'description'],
                },
            ),

            (
                'Бухгалтерия',
                {
                    'fields': ['price', 'quantity'],
                }
            ),
            (
                'Рейтинг и прочее',
                {
                    'description': 'Рейтинг сформирован автоматически на основе оценок покупателей', 'fields': ['rating', 'date_added'],
                }
            ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)