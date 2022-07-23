from django.contrib import admin
from .models import Firstpage
from .models import Blog
from .models import Category


class FirstpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'url')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'url')


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'cat', 'time_completed', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_completed')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Firstpage, FirstpageAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
