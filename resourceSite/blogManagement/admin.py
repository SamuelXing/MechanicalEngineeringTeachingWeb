# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Blog,Comments
# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status=0)
make_published.short_description = u"标记选择好的文章来发布"

class BlogAdmin(admin.ModelAdmin):
	search_fields = ['title']
	fields = ('title', 'userName','summary', 'content',  'status', 'is_top',  'pub_at')
	list_display = ('title','is_top','status','pub_at')
	list_display_links = ('title', )
	actions = [make_published]

class CommentsAdmin(admin.ModelAdmin):
	list_display=('author','content','created_at')
	search_fields = ['content']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comments,CommentsAdmin)
