from django.contrib import admin
from .models import Post,Category,Comment,Profile
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'body', 'date_added',)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Profile)