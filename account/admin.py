from django.contrib import admin

from account.models import ContactAddress


class ContactAddressAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'phone', 'address', 'post_code', 'is_default')
    raw_id_fields = ('user',)
    
admin.site.register(ContactAddress, ContactAddressAdmin)
