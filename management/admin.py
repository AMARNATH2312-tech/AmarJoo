from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ("username", "email", "last_login","is_active")
    search_fields = ("username", "email")

@admin.register(models.Amount)
class AmountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ItemInfo)
class ItemImagesAdmin(admin.ModelAdmin):
    list_display = ("item_name", "image",)

@admin.register(models.Items)
class ItemsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Month)
class MonthAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Year)
class YearAdmin(admin.ModelAdmin):
    pass
