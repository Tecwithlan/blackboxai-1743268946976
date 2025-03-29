from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'unit_price', 'bulk_price', 'line_total')
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'status', 'total')
    list_filter = ('status', 'order_date', 'tax_exempt')
    search_fields = ('customer__business_name', 'id')
    readonly_fields = ('subtotal', 'tax_amount', 'total')
    inlines = [OrderItemInline]
    fieldsets = (
        (None, {'fields': ('customer', 'status', 'notes')}),
        ('Financials', {'fields': ('tax_exempt', 'tax_rate', 'subtotal', 'tax_amount', 'total')}),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'line_total')
    list_filter = ('order__status',)
    search_fields = ('product__name', 'order__id')
