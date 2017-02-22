# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models #从django.db中导入models
from django.contrib.auth.models import User #导入Django内置的认证系统中的用户模型
from userManagement.models import NormalUsers
# import markdown2

from django.utils import timezone

# 数据库字段类型定义
class NormalTextField(models.TextField):
    '''
    models.TextField 默认在MySQL上的数据类型是longtext，用不到那
    么大，所以派生NormalTextField，只修改生成SQL时的数据类型text
    '''
    def db_type(self, connection):
        return 'text'

STATUS = {
    0: u'发布',
    1: u'草稿',
    2: u'删除',
}

class BlogManager(models.Manager):
	pass


class Blog(models.Model):
	userName=models.ForeignKey(User,null=False,verbose_name=u'作者')
	title=models.CharField(max_length=50,null=False,verbose_name=u'标题')
	summary=models.CharField(max_length=200,null=False,verbose_name=u'摘要')
	content=models.TextField(null=False,verbose_name=u'正文')
	view_times = models.IntegerField(default=1)
	is_top = models.BooleanField(default=False, verbose_name=u'置顶')
	status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
	pub_at = models.DateTimeField(default=datetime.now, verbose_name=u'发布时间')

	created_at=models.DateTimeField(u'创建于',auto_now_add=True,editable=True)
	update_at = models.DateTimeField(u'更新时间', auto_now=True,null=True)
	objects = BlogManager()

	def __str__(self):
		return self.title

	# @classmethod
	# def available_list(cls):
	# 	return cls.objects.filter(status=0)

	class Meta:
		ordering = ['-is_top', '-pub_at', '-created_at']
		verbose_name_plural=verbose_name=u"文章"


class Comments(models.Model):
	blog=models.ForeignKey(Blog,null=True,blank=True)
	author=models.ForeignKey(User,related_name='comment_author',null=True,blank=True)
	content = NormalTextField(null=True, blank=True,verbose_name=u'内容')
	created_at=models.DateTimeField(auto_now_add=True,verbose_name=u'发表于')

	class Meta:
		ordering=['-created_at']
		verbose_name_plural=verbose_name=u"评论"




