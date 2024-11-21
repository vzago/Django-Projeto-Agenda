from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone', 'email', 'created_date',
    ordering = 'id', #-id para decrescente
    #list_filter = 'created_date', # ou ('created_date',)
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'first_name' , 'last_name', #edit without opening the contact
    list_display_links = 'id', 'phone', #clickable link