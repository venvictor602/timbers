# woods/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class WoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'grain', 'density', 'durability')
    search_fields = ('name', 'color', 'grain', 'density', 'durability')
    list_filter = ('color', 'grain', 'density', 'durability')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'color', 'grain', 'density', 'durability', 'uses', 'care_instructions')
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3')
        }),
    )
    readonly_fields = ('image1_thumbnail', 'image2_thumbnail', 'image3_thumbnail')

    def image1_thumbnail(self, obj):
        if obj.image1:
            return mark_safe(f'<img src="{obj.image1.url}" width="150" height="150" />')
        return "No Image"
    image1_thumbnail.short_description = 'Image 1'

    def image2_thumbnail(self, obj):
        if obj.image2:
            return mark_safe(f'<img src="{obj.image2.url}" width="150" height="150" />')
        return "No Image"
    image2_thumbnail.short_description = 'Image 2'

    def image3_thumbnail(self, obj):
        if obj.image3:
            return mark_safe(f'<img src="{obj.image3.url}" width="150" height="150" />')
        return "No Image"
    image3_thumbnail.short_description = 'Image 3'

admin.site.register(Wood, WoodAdmin)
admin.site.register(Contact)
admin.site.register(Testimony)