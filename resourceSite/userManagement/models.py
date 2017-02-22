# -*- coding: utf-8 -*-
import datetime
import uuid

from django.db import models
from django.contrib.auth.models import User



class NormalUsers(models.Model):
	# id=models.UUIDField(primary_key=True,editable=True)
	# user = models.OneToOneField(User,related_name='user', null=True)
	user=models.OneToOneField(User,null=True)
	membership=models.BooleanField(default=False,verbose_name=u'会员?')
	userName=models.CharField(max_length=50,verbose_name=u'用户名')
	# userImage=models.URLField(max_length=50,blank=True,verbose_name=u'用户头像')
	signature=models.CharField(max_length=200,verbose_name='签名')
	created_at=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')

	def username(self):
		if self.userName:
			return self.userName
		else:
			return self.user.username

	def __str__(self):
		return self.userName

	class Meta:
		ordering=['-created_at']
		verbose_name_plural=verbose_name=u"用户信息"



class Payment(models.Model):
	user=models.ForeignKey(NormalUsers)
	payment=models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u'金额(元)')
	payed_at=models.DateTimeField(verbose_name=u'成为会员时间')

	def __str__(self):
		return self.user.userName

	class Meta:
		ordering=['-payed_at']
		verbose_name_plural=verbose_name=u"支付信息"





