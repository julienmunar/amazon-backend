from django.contrib import admin

# Register your models here.

from .models import Inventory,ItemCategory

@admin.register(Inventory)
class AdminInventory(admin.ModelAdmin):
    list_display=("title","price","category")
    search_fields=["title"]
    save_on_top=True
    list_filter=["category"] 
admin.site.register(ItemCategory)
