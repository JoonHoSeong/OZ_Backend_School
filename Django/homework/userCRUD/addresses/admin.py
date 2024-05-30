from django.contrib import admin
from .models import Addresses

# Register your models here.
@admin.register(Addresses)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "street", "city", "state","postal_code", "country")
    list_filter = ("city", "state", "country")
    search_fields = ("user_name", "street", "city", "state", "postal_code", "country")
