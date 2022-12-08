from django.contrib import admin
from .models import Post
from .models import Group


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = 'empty'
    list_editable = ('group',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group)

