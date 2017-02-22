from django.contrib import admin

from .models import Plane, Node, Topic, Reply, Vote
# Register your models here.

class PlaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    list_filter = ('created',)


class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduction', 'created')
    search_fields = ('name',)
    list_filter = ('created',)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'node', 'created')
    search_fields = ('title', 'content')
    list_filter = ('created',)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('content', 'created')
    search_fields = ('content',)
    list_filter = ('created',)

admin.site.register(Plane, PlaneAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Vote)
