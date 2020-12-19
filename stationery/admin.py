from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Stationery

class UserAdmin(admin.ModelAdmin):
    #fields to display on panell
    list_display = ('stationery_name', 'stationery_location', 'Individual_Task', 'Group_Task', 'Report', 'Research', 'Paper' )

    #filter
    list_filter = ('Individual_Task', 'Group_Task', 'Report', 'Research', 'Paper')

    #customization of creation form
    fieldsets = (
        (None, {'fields' : ('stationery_name')}),
        ('Stationery info', {'fields':('stationery_profile', 'stationery_name', 'stationery_location', 'Stationery_slug')}),
        ('Stationery services', {'fields':('Individual_Task', 'Group_Task', 'Report', 'Research', 'Paper')}),
    )

    #search
    search_fealds = ('stationery_name', 'stationery_location', 'Individual_Task', 'Group_Task', 'Report', 'Research', 'Paper')
    list_ordering = ('stationery_name')
    filter_horizontally = ()

admin.site.register(Stationery, UserAdmin)