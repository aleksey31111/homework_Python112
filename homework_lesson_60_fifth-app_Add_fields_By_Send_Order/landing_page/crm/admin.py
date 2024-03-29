from django.contrib import admin
from .models import StatusCrm, Order, CommentsCrm


class Comments(admin.StackedInline):
    model = CommentsCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    readonly_fields = ('id', 'order_dt')
    list_per_page = 9
    list_max_show_all = 100
    inlines = [Comments]


admin.site.register(StatusCrm)
admin.site.register(Order, OrderAdm)
admin.site.register(CommentsCrm)
