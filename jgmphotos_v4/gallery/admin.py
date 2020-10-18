from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    #search_fields = ['title']
    list_display = ('title',)
    #filter_horizontal = ['album_name']
    #inlines = [AlbumNameInline]


admin.site.register(Image, ImageAdmin)
