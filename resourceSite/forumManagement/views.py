from django.shortcuts import render
import json, math, hashlib
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import timezone
from django.conf import settings
from forumManagement.models import Topic, Vote, Reply, Node,  Plane, Pages
from django.contrib.auth.models import User
from userManagement.models import NormalUsers
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from .forum_form import CreateForm,ReplyForm
from django import forms
from django.views import generic

# Create your views here.
def get_index(request):
    user = request.user
    if user.is_authenticated():
        counter = {
            'topics': user.topic_author.all().count(),
            'replies': user.reply_author.all().count(),
        }
    # 计数功能
        status_counter = {
        'users': User.objects.all().count(),
        'nodes': Node.objects.all().count(),
        'topics': Topic.objects.all().count(),
        'replies': Reply.objects.all().count(),
    }

    try:
        current_page = int(request.GET.get('p', '1'))
    except ValueError:
        current_page = 1

    topics, topic_page = Topic.objects.get_all_topic(current_page=current_page,num=10)
    planes = Plane.objects.all().prefetch_related('node_set')
    nodes = Node.objects.all()
    active_page = 'topic'
    return render_to_response('forum/index.html', locals(),
        context_instance=RequestContext(request))

def get_node_topics(request,node_id):
	node=get_object_or_404(Node,pk=node_id)
	topics_list=Topic.objects.all().filter(node=node_id)
	paginator=Paginator(topics_list,8)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render_to_response('forum/node_topics.html', locals())


@login_required
def get_create(request,errors=None):
	user=request.user
	counter = {
        'topics': user.topic_author.all().count(),
        'replies': user.reply_author.all().count(),
    }
	return render_to_response('forum/create.html', locals(),
        context_instance=RequestContext(request))

@login_required
def post_create(request):
	form=CreateForm(request.POST)
	if form.is_valid():
		t=Topic()

		user=request.user
		try:
			last_created=user.topic_author.all().order_by('-created')[0]
		except IndexError:
			last_created=None
		now=timezone.now()
		t.title=form.cleaned_data.get('title')
		t.content=form.cleaned_data.get('content')
		t.node=form.cleaned_data['nodes']
		t.created=now
		t.author=user
		t.reply_count=0
		t.last_touched=now
		t.save()
	else:
		return get_create(request,errors=form.errors)

	#如果用户最后一篇的标题内容与提交的相同
	#
	#
	return HttpResponseRedirect(reverse('forum:index'))

def post_view(request, topic_id):
	if request.method == 'GET':
		try:
			topic=Topic.objects.get_topic_by_topic_id(topic_id)
		except Topic.DoesNotExist:
			raise Http404

		replies=Reply.objects.get_all_replies_by_topic_id(topic.id)

		topic.hits=(topic.hits or 0)+1
		topic.save()
		return render_to_response('forum/topic.html', locals(), context_instance=RequestContext(request))

	elif request.method == 'POST':
		if not request.user.is_authenticated():
			return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
		try:
			topic=Topic.objects.get_topic_by_topic_id(topic_id)
		except Topic.DoesNotExist:
			raise Http404

		form=ReplyForm(request.POST)
		if not form.is_valid():
			return render_to_response('forum/topic.html', locals(), context_instance=RequestContext(request))

		user=request.user
		try:
			last_reply=topic.reply_set.all().order_by('-created')[0]
		except IndexError:
			last_reply=None

		now=timezone.now()
		reply=Reply(
			topic=topic,
			author=user,
			content=form.cleaned_data['content'],
			created=now,
		)
		topic.reply_count=topic.reply_count+1
		topic.save()
		reply.save()
		Topic.objects.filter(pk=topic.id).update(last_replied_time=now, last_touched=now)

		return HttpResponseRedirect(reverse('forum:view_topic', args=(topic.id,)))







