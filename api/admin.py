from django.contrib import admin
from . import models


class PhotoItemInline(admin.TabularInline):
    model = models.PhotoItem
    extra = 1

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoItemInline]


admin.site.register(models.PDFFile)
