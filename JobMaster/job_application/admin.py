from django.contrib import admin
from .models import Form

@admin.site.register
class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    filter = ('date', 'occupation')
    ordering = ('first_name', )
    readonly_fields = ('occupation', )
