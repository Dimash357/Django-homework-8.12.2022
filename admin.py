from django.contrib import admin
from django_app import models
from .models import profile


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'description',
    )
    list_filter = (
        'title',
        'description',
    )
    search_fields = (
        'title',
        'description',
    )
    fieldsets = (
        ("Основное", {"fields": ('title',)}),
        ("Дополнительное", {"fields": ('description',)}),
    )


class TodosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'description',
    )
    list_filter = (
        'title',
        'description',
    )
    search_fields = (
        'title',
        'description',
    )
    fieldsets = (
        ("Основное", {"fields": ('title',)}),
        ("Дополнительное", {"fields": ('description',)}),
    )


admin.site.register(models.Todo, TodosAdmin)


admin.site.register(profile)


class ProductAdmin(admin.ModelAdmin):
    """ """

    list_display = (
        "label",
        "amount",
        "not_bubble_price",
        "bubble_percentage",
        "final_price",
        "vat_price",
        "overall",
    )
    list_display_links = ("label",)
    list_editable = ("amount",)
    list_filter = (
        "label",
        "amount",
        "not_bubble_price",
        "bubble_percentage",
        "final_price",
        "vat_price",
        "overall",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "label",
                    "amount",
                    "not_bubble_price",
                    "bubble_percentage",
                    "final_price",
                    "vat_price",
                    "overall",
                )
            },
        ),
    )
    search_fields = [
        "label",
        "amount",
        "not_bubble_price",
        "bubble_percentage",
        "final_price",
        "vat_price",
        "overall",
    ]


# admin.site.register(models.Product)
admin.site.register(models.Product, ProductAdmin)