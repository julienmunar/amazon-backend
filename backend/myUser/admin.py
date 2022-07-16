from django.contrib import admin

from .models import MyUser
from django.contrib import admin
# Register your models here.

admin.site.register

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    ## ADMIN WEB HOME
    list_display = ('username','email',"firstname", 'lastname','is_active','is_admin')
    list_display_links = ("email",'username')
    list_filter=["is_admin","is_active"] 
    search_fields=["username","email"]
    save_on_top=True
    ## PAGE DETAILS
    fieldsets = (
        ("Informations", {
            'fields': ('email', 'password', "username","firstname","lastname","avatar","last_login")
        }),
        ('Advanced options', {
            'classes': ('collapse', 'open'),
            'fields': ("is_active","is_admin"),
        }),
    )
