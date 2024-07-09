from django.contrib import admin
from .models import Posts, Category, Comments

# Register your models here.
admin.site.register(Category)

@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    list_display = ['user', 'post', 'created']
    search_fields = ('user', 'post')

@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ['title', 'description', 'author']
    search_fields = ('title', 'author')

