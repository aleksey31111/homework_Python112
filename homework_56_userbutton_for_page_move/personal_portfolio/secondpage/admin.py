from django.contrib import admin
from .models import Secondpage


class SecondpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'date')


admin.site.register(Secondpage, SecondpageAdmin)
