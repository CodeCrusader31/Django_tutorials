from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content')
    list_filter = ('date', 'tags','author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)