from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import MyAccount

# MyAccount = get_user_model()
# Modify Site Header
admin.site.site_header = 'E-Printing Service'                    # default: "Django Administration"
# Modify Site Title
admin.site.index_title = 'E-Printing Site Management'            # default: "Site administration"
# Modify Site Index Title
admin.site.site_title = 'Welcome to E-Printing service admin site'                  # default: "Django site admin"
# Modify Site URL
admin.site.site_urls = 'E-Printing admin site'

class UserAdmin(admin.ModelAdmin):
    #.............Form to add and change user instance......
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    #.....fields used in displaying user models......
    list_display    = ('username', 'email', 'admin')
    list_filter     = ('admin','staff', 'active')
    fieldsets       = (
        (None, {'fields': ('username', 'email','password')}),
        ('personal info', {'fields': ('first_name','last_name','sex', 'phone')}),
        ('permission',{'fields': ('admin', 'staff', 'active')}),

    )
    #.............add fields set is not standard model.admin attribute..........
    #............ overrides get_fieldsets to use when creating a user...........
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide'),
    #         'fiels': ('email', 'password1','password2')
    #     }),
    # )
    search_fields = ('email','username', 'first_name','last_name',)
    ordering      = ('email','username',)
    filter_horizontall = ()
admin.site.register(MyAccount, UserAdmin)
#.........removing group model from admin we`re not using it....... 
# admin.site.unregister(Group)