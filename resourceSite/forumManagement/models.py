from django.db import models
from django.contrib.auth.models import User

# 数据库字段类型定义
class NormalTextField(models.TextField):
    '''
    models.TextField 默认在MySQL上的数据类型是longtext，用不到那
    么大，所以派生NormalTextField，只修改生成SQL时的数据类型text
    '''
    def db_type(self, connection):
        return 'text'

class Pages(object):
    '''
    分页查询类
    '''
    def __init__(self, count, current_page=1, list_rows=40):
        self.total = count
        self._current = current_page
        self.size = list_rows
        self.pages = self.total // self.size + (1 if self.total % self.size else 0)

        if (self.pages == 0) or (self._current < 1) or (self._current > self.pages):
            self.start = 0
            self.end = 0
            self.index = 1
        else:
            self.start = (self._current - 1) * self.size
            self.end = self.size + self.start
            self.index = self._current
        self.prev = self.index - 1 if self.index > 1 else self.index
        self.next = self.index + 1 if self.index < self.pages else self.index

class NodeManager(models.Manager):
	def get_all_hot_nodes(self):
		query=self.get_queryset().filter(topic__reply_count__gt=0).order_by('-topic__reply_count')
		query.query.group_by=['id']
		return query

class TopicManager(models.Manager):
    '''
    Topic objects
    '''
    def get_all_topic(self, num=36, current_page=1): # 可以考虑在这里过滤掉没有头像的用户发帖，不显示在主页
        count = self.get_queryset().count()
        page = Pages(count, current_page, num)
        query = self.get_queryset().select_related('node', 'author').\
            all().order_by('-last_touched', '-created', '-last_replied_time', '-id')[page.start:page.end]
        return query, page

    def get_user_all_topics(self, uid, num = 36, current_page = 1):
        count = self.get_queryset().filter(author__id=uid).count()
        page = Pages(count, current_page, num)
        query = self.get_queryset().select_related('node', 'author').\
            filter(author__id=uid).order_by('-id')[page.start:page.end]
        return query, page

    def get_user_all_replied_topics(self, uid, num = 36, current_page = 1):
        pass # 留着以后再说

    def get_topic_by_topic_id(self, topic_id):
        query = self.get_queryset().select_related('node', 'author').get(pk=topic_id)
        return query

    def get_user_last_created_topic(self, uid):
        query = self.get_queryset().filter(author__id=uid).order_by('-created')[0]
        return query

class ReplyManager(models.Manager):
    '''
    Reply objects
    '''
    def get_all_replies_by_topic_id(self, topic_id):
        count = self.get_queryset().filter(topic__id=topic_id).count()
        query = self.get_queryset().select_related('author').\
            filter(topic__id=topic_id).order_by('id')
        return query

    def get_user_all_replies(self, uid, num = 16, current_page = 1):
        count = self.get_queryset().filter(author__id=uid).count()
        page = Pages(count, current_page, num)
        query = self.get_queryset().select_related('topic', 'topic__author').\
            filter(author__id=uid).order_by('-id')[page.start:page.end]
        return query, page


# Create your models here
class Plane(models.Model):
	name=models.CharField(max_length=200,null=True,blank=True,verbose_name=u'名称')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['-created']
		verbose_name_plural=verbose_name=u"版块"

class Node(models.Model):
	name=models.CharField(max_length=200,null=True,blank=True,verbose_name='节点名称')
	introduction=models.CharField(max_length=500,null=True,blank=True,verbose_name='介绍')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
	plane=models.ForeignKey(Plane,null=True,blank=True,verbose_name=u'所属版块')
	topic_count=models.IntegerField(null=True,blank=True)

	objects=NodeManager()
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created']
		verbose_name_plural=verbose_name=u"节点"


class Topic(models.Model):
	author=models.ForeignKey(User,related_name='topic_author',verbose_name=u'发帖人')
	title=models.CharField(max_length=160,verbose_name=u'标题')
	content=models.TextField(blank=True,null=True,verbose_name=u'帖子内容')
	hits=models.IntegerField(default=1,verbose_name=u'点击数')
	created=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
	updated = models.DateTimeField(null=True, blank=True,verbose_name=u'更新时间')
	node=models.ForeignKey(Node,null=True,blank=True,verbose_name=u'所属节点')
	reply_count=models.IntegerField(null=True,blank=True,verbose_name=u'回复数量')
	up_vote = models.IntegerField(null=True, blank=True,verbose_name=u'赞同')
	down_vote = models.IntegerField(null=True, blank=True,verbose_name=u'反对')
	last_replied_time = models.DateTimeField(null=True, blank=True,verbose_name=u'最后回复时间')
	last_touched = models.DateTimeField(null=True, blank=True,verbose_name=u'最后点击时间')

	objects=TopicManager()
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']
		verbose_name_plural=verbose_name=u"帖子"


class Reply(models.Model):
	topic=models.ForeignKey(Topic,null=True,blank=True,verbose_name=u'回复话题')
	author=models.ForeignKey(User,related_name='reply_author',verbose_name=u'作者')
	content=NormalTextField(null=True,blank=True,verbose_name=u'内容')
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True,verbose_name=u'创建时间')
	updated = models.DateTimeField(null=True, blank=True,verbose_name=u'更新时间')
	up_vote = models.IntegerField(null=True, blank=True,verbose_name=u'赞同数')
	down_vote = models.IntegerField(null=True, blank=True,verbose_name=u'反对数')
	last_touched = models.DateTimeField(null=True, blank=True,verbose_name=u'最后浏览时间')

	objects=ReplyManager()
	def __str__(self):
		return self.content
	class Meta:
		ordering = ['-created']
		verbose_name_plural=verbose_name=u"回复"

class Vote(models.Model):
	status = models.IntegerField(null=True, blank=True,verbose_name=u'状态')
	involved_type = models.IntegerField(null=True, blank=True)
	involved_user = models.ForeignKey(User, related_name='vote_user', null=True, blank=True)
	involved_topic = models.ForeignKey(Topic, related_name='vote_topic', null=True, blank=True)
	involved_reply = models.ForeignKey(Reply, related_name='vote_reply', null=True, blank=True)
	trigger_user = models.ForeignKey(User, related_name='vote_trigger', null=True, blank=True)
	occurrence_time = models.DateTimeField(null=True, blank=True)

	class Meta:
		ordering = ['-occurrence_time']
		verbose_name_plural=verbose_name=u"投票"