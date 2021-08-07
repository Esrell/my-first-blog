from django.contrib import admin
from .models import News, Category
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	last_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
	last_display_links = ('id', 'title')
	serch_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
	last_display = ('id', 'title')
	last_display_links = ('id', 'title')
	serch_fields = ('title')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

