from django.contrib import admin

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount', 'created_time')
    inlines = [
        OrderItemInline,
    ]
    raw_id_fields = ('owner', 'address')


admin.site.register(Order, OrderAdmin)
