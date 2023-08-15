from django.contrib import admin

from resturant_menu.models import Item


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status', )
    search_fields = ('meal', 'description')
