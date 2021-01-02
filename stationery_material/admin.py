from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from stationery_material.models import Material

class UserAdmin(admin.ModelAdmin):
    list_display =  ('title', 'material_type')
    list_filter  =  ('title', 'material_type')

    fieldsets    =  (
        ('content title', {'fields' : ('title',)}),
        ('content_type', {'fields' : ('material_type',)}),
        ('short summary', {'fields' : ('description',)}),
    )

    search_fields =  ('material_type', 'title')
    ordering      =  ('title', 'material_type')
    filter_horizontall = ()

admin.site.register(Material,UserAdmin)