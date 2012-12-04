from django.contrib import admin

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
#    raw_id_fields = ('product',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount', 'created_time')
    inlines = [
        OrderItemInline,
    ]
    raw_id_fields = ('owner',)


admin.site.register(Order, OrderAdmin)
