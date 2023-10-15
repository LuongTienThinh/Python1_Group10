from django.contrib import admin
from .models import Post,Category,Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'body', 'date_added',)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)