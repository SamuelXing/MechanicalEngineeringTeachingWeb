from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NormalTextField(models.TextField):
    def db_type(self, connection):
        return 'text'

STATUS = {
    0: u'发布',
    1: u'草稿',
    2: u'删除',
}


class Courses(models.Model):
	name=models.CharField(max_length=50,verbose_name=u'课程名')
	intro=models.CharField(max_length=200,verbose_name=u'课程介绍',blank=True,null=True)
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
	updated=models.DateTimeField(auto_now_add=True,verbose_name=u'更新时间', blank=True,null=True)
	is_display=models.BooleanField(default=False,verbose_name=u'是否为图片展示')
	status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')

	def __str__(self):
		return self.name

	class Meta:
		ordering=['created',]
		verbose_name_plural=verbose_name=u"课程信息"

class Chapters(models.Model):
	course=models.ForeignKey(Courses, related_name='chap_course' ,verbose_name=u'所属课程')
	name=models.CharField(max_length=100,verbose_name=u'大章名称')
	intro=models.CharField(max_length=200,verbose_name=u'大章介绍', blank=True,null=True)
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
	image=models.ImageField(upload_to='chap_img/%Y/%m/%d', verbose_name=u'大章图片')

	def __str__(self):
		return self.name

	class Meta:
		ordering=['created']
		verbose_name_plural=verbose_name=u"大章信息"

class Section(models.Model):
	chap=models.ForeignKey(Chapters,related_name='sec_chap',verbose_name=u'所属大章')
	name=models.CharField(max_length=100,verbose_name=u'小节名称')
	intro=models.CharField(max_length=200,verbose_name=u'介绍',blank=True,null=True)
	created=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

	def __str__(self):
		return self.name

	class Meta:
		ordering=['created',]
		verbose_name_plural=verbose_name=u"小节信息"

class Video(models.Model):
	user=models.ForeignKey(User,related_name='upload_author',verbose_name=u'上传者')
	chap=models.ForeignKey(Section,related_name='video_sec',verbose_name=u'所属小节')
	title=models.CharField(max_length=100,verbose_name=u'视频名称')
	intro=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'介绍')
	image=models.ImageField(upload_to='video_img/%Y/%m/%d',verbose_name=u'视频图片')
	video=models.FileField(upload_to='video/%Y/%m/%d',verbose_name=u'视频')
	assignment=models.TextField(blank=True,null=True,verbose_name=u'作业')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
	hits=models.IntegerField(default=1,verbose_name=u'点击数')
	permission=models.BooleanField(default=True,verbose_name=u'会员观看?')
	is_demo=models.BooleanField(default=True,verbose_name=u'是否为演示视频')

	def __str__(self):
		return self.title

	class Meta:
		ordering=['created']
		verbose_name_plural=verbose_name=u"视频信息"

class Photos(models.Model):
	chap=models.ForeignKey(Section,related_name='photo_sec',verbose_name=u'所属小节')
	title=models.CharField(max_length=50,verbose_name=u'图片名称')
	intro=models.CharField(max_length=200,verbose_name=u'图片描述')
	file=models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name=u'图片文件')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

	def __str__(self):
		return self.title

	class Meta:
		ordering=['created']
		verbose_name_plural=verbose_name=u"图片信息"

class PhotoList(models.Model):
	photo=models.ForeignKey(Photos,related_name='photo_list',verbose_name=u'所属图片类')
	title=models.CharField(max_length=50,verbose_name=u'名称')
	file=models.ImageField(upload_to='detail/%Y/%m/%d',verbose_name=u'图片文件')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

	def __str__(self):
		return self.title

	class Meta:
		ordering=['created']
		verbose_name_plural=verbose_name=u"详细图片"


class Reply(models.Model):
	video=models.ForeignKey(Video,verbose_name=u'所属视频')
	author=models.ForeignKey(User,related_name='video_reply',verbose_name=u'回复人')
	content=NormalTextField(null=True,blank=True,verbose_name=u'内容')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'回复时间')

	class Meta:
		ordering=['-created',]
		verbose_name_plural=verbose_name=u"回复信息"








