from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('name', )}
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

