from django.contrib import admin
from .models import ProductCategory, Product, BulkPrice

class BulkPriceInline(admin.TabularInline):
    model = BulkPrice
    extra = 1
    min_num = 1

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'base_price', 'min_order_quantity', 'current_stock')
    list_filter = ('category', 'active')
    search_fields = ('sku', 'name')
    inlines = [BulkPriceInline]
    fieldsets = (
        (None, {'fields': ('sku', 'name', 'category', 'description')}),
        ('Pricing & Inventory', {'fields': ('unit', 'base_price', 'min_order_quantity', 'current_stock')}),
        ('Media', {'fields': ('image',)}),
        ('Status', {'fields': ('active',)}),
    )
