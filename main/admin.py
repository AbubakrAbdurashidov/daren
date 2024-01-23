from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    search_fields = ('name', 'email')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date', )
