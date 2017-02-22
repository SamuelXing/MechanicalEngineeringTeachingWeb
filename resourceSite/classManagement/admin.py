from django.contrib import admin
from .models import Courses, Chapters, Section, Video, Reply, Photos,PhotoList

# Register your models here.
class ChaptersInline(admin.StackedInline):
	model = Chapters
	extra = 3

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created','updated','intro','status','is_display')
    search_fields = ('name',)
    list_filter = ('created',)
    inlines = [ChaptersInline]

class SectionInline(admin.StackedInline):
	model = Section
	extra = 3

class ChaptersAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created','intro','course')
    search_fields = ('name',)
    list_filter = ('created',)
    inlines = [SectionInline]


class SectionAdmin(admin.ModelAdmin):
	list_display = ('name','chap','created','intro')
	search_fields = ('name',)
	list_filter = ('created',)

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title','chap','created','intro','permission','is_demo','hits')
	search_fields = ('name',)
	list_filter = ('created',)

class PhotosAdmin(admin.ModelAdmin):
	list_display = ('title','chap','created')
	search_fields = ('title',)
	list_filter = ('created',)

class PhotoListAdmin(admin.ModelAdmin):
	list_display = ('title','photo','created')
	search_fields = ('title',)
	list_filter = ('created',)

class ReplyAdmin(admin.ModelAdmin):
	list_display = ('content','video','created')
	search_fields = ('content',)
	list_filter = ('created',)


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Chapters, ChaptersAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Reply,ReplyAdmin)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(PhotoList,PhotoListAdmin)


