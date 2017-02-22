from django.shortcuts import render, get_object_or_404
from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.context_processors import csrf
from django.http import HttpResponse  # test

from .models import NormalUsers, Payment
from django.contrib.auth.models import User

# Create your views here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', 'Only alphanumeric characters and underscore are allowed.')
emailCheck=RegexValidator(r'^([0-9a-zA-Z\_\.]*?)@([0-9a-zA-Z]*?)\.([0-9a-zA-Z]*?){3}$','Only formal email address is valid.')

@login_required
def user_info(request, user_id):
	u=get_object_or_404(User, pk=user_id)
	if u.is_staff:
		return HttpResponse(u'对不起，您没有权限访问管理员信息！')
	if u.id == request.user.id:
		wrap_user=NormalUsers.objects.get(userName=u.username)
		wrap_user.user=u
		return render_to_response('userManage/user-info.html',{'request':request,'wrap_user':wrap_user,'user':u,})
	else:
		wrap_user = NormalUsers.objects.get(userName=u.username)
		wrap_user.user = u
		return render_to_response('userManage/user-public-info.html',{'request': request,'wrap_user': wrap_user,'user': u,})

def register(request):
	if request.method == 'GET':
		return render_to_response('userManage/register.html', {'title': _('register')},
		                          context_instance=RequestContext(request))
	elif request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		try:
			alphanumeric(username)
		except:
			messages.add_message(request, messages.WARNING,
			                     _(u'用户名只能包含字母，数字，下划线'))
			return HttpResponseRedirect(reverse('user:register'))

		try:
			emailCheck(email)
		except:
			messages.add_message(request,messages.WARNING,
			                     _(u'邮箱的地址不符合规则（xxx@example.com）'))
			return HttpResponseRedirect(reverse('user:register'))

		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.WARNING, _(u'用户名已经存在'))
			return HttpResponseRedirect(reverse('user:register'))

		if password != password2 or password == '' or password2 == '':
			messages.add_message(request, messages.WARNING, _(u'两次输入的密码不匹配，或者为空'))
			return HttpResponseRedirect(reverse('user:register'))

		user = User.objects.create_user(username, email, password)
		user = authenticate(username=username, password=password)
		login(request, user)
		p = NormalUsers()
		p.user = user
		p.userName = user.username
		p.save()
		return HttpResponseRedirect(reverse('course:index'))
		# return HttpResponse("Hello, world. You're at the polls index.")


def user_login(request):
	if request.method == 'GET':
		return render_to_response('userManage/login.html', context_instance=RequestContext(request))

	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if not User.objects.filter(username=username).exists():
			messages.add_message(request, messages.WARNING, _('username does not exist'))
			return HttpResponseRedirect(reverse('user:signin'))

		if user is None:
			messages.add_message(request, messages.WARNING, _('password is invalid'))
			return HttpResponseRedirect(reverse('user:signin'))

		login(request, user)
		return HttpResponseRedirect(reverse('course:index'))


def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('course:index'))


def setting(request):
	if request.method == 'GET':
		if request.user.is_staff:
			return HttpResponse(u'请前往后台设置')
		wrap_user = NormalUsers.objects.get(userName=request.user.username)
		return render_to_response('userManage/user-setting.html', {'request': request, 'wrap_user': wrap_user},
		                          context_instance=RequestContext(request))

	elif request.method == 'POST':
		wrap_user = NormalUsers.objects.get(userName=request.user.username)
		wrap_user.user = request.user
		wrap_user.signature = request.POST['signature']
		wrap_user.user.email = request.POST['email']
		wrap_user.save()
		request.user.save()
		return HttpResponseRedirect(reverse('user:userInfo', args=(request.user.id,)))


def change_password(request):
	u = request.user
	if request.user.is_staff:
		return HttpResponse(u'请前往后台修改')
	if request.method == 'GET':
		return render_to_response('userManage/change_password.html',
		                          {'request': request, },
		                          context_instance=RequestContext(request))
	elif request.method == 'POST':
		old = request.POST['old-password']
		new = request.POST['password']
		if request.POST['password'] != request.POST['password2'] or request.POST['password'] == '' or request.POST[
			'password2'] == '':
			messages.add_message(request, messages.WARNING, _('passwords don\'t match, or are blank'))
			return HttpResponseRedirect(reverse('user:change_password'))

		if authenticate(username=u.username, password=old):
			u.set_password(new)
			u.save()
			messages.add_message(request, messages.SUCCESS, _('password updated successfully'))
			update_session_auth_hash(request, u)
			return HttpResponseRedirect(reverse('user:change_password'))
		else:
			messages.add_message(request, messages.WARNING,
			                     _('unable to change your password, the current password may be invalid'))
			return HttpResponseRedirect(reverse('user:change_password'))


def reset(request):
	return password_reset(request, template_name='userManage/reset-password.html',
	                      email_template_name='userManage/reset_password_email.html',
	                      subject_template_name='userManage/reset_password_subject.txt',
	                      post_reset_redirect=reverse('user:signin'))


def reset_confirm(request, uidb64=None, token=None):
	return password_reset_confirm(request, template_name='user/reset_password_confirm.html',
	                              uidb64=uidb64, token=token, post_reset_redirect=reverse('user:signin'))





