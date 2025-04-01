from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        ('', {
            'fields': ('category',),
        }),
    )

admin.site.register(Category, CategoryAdmin)
