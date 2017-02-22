from django.shortcuts import render, get_list_or_404, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .video_form import VideoForm

from django.contrib.auth.models import User
from userManagement.models import NormalUsers
from .models import Courses, Chapters, Section, Video, Photos, Reply,PhotoList

# Create your views here.
def index(request):
	courses=get_list_or_404(Courses, status=0)
	chapters=get_list_or_404(Chapters, course=1)
	paginator=Paginator(chapters,6)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render_to_response('course/index.html', locals(),
		context_instance=RequestContext(request))

def get_chapters(request, course_id):
	courses=get_list_or_404(Courses, status=0)
	course=get_object_or_404(Courses,pk=course_id)
	# chapters=get_list_or_404(Chapters, course=course_id)
	chapters=Chapters.objects.all().filter(course=course_id)
	paginator=Paginator(chapters,6)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render_to_response('course/course.html', locals(),
		context_instance=RequestContext(request))

@login_required
def get_section(request, chap_id):
	chap=get_object_or_404(Chapters,pk=chap_id)
	sections=Section.objects.all().filter(chap=chap_id)
	return render_to_response('course/sections.html', locals(),
		context_instance=RequestContext(request))


@login_required
def get_video_or_image(request,sec_id):
	sec=get_object_or_404(Section,pk=sec_id)
	# chap=sec.sec_chap.get()
	chap=get_object_or_404(Chapters,pk=sec.chap.id)
	course=get_object_or_404(Courses,pk=chap.course.id)
	if course.is_display:
		photos=Photos.objects.all().filter(chap=sec_id)
		return render_to_response('course/photos.html', locals(),
								  context_instance=RequestContext(request))
	else:
		videos=Video.objects.all().filter(chap=sec_id)
		paginator=Paginator(videos,6)
		page = request.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)
		return render_to_response('course/videos.html', locals(),
								  context_instance=RequestContext(request))

def watch(request,video_id):
	if request.method=='GET':
		user_id=request.user.id
		u=get_object_or_404(User, pk=user_id)
		wrap_user=NormalUsers.objects.get(userName=u.username)
		video=get_object_or_404(Video,pk=video_id)
		print(video.permission)
		print(wrap_user.membership)
		if not wrap_user.membership and video.permission:
			print("not member and not available video")
			return render_to_response('course/membership_check.html',)
		else:
			if Reply.objects.filter(video__id=video_id).count()==0:
				message=u"暂无评论"
			else:
				replies=get_list_or_404(Reply, video=video_id)
		return render_to_response('course/watch.html', locals(),
								  context_instance=RequestContext(request))
	elif request.method=='POST':
		video=get_object_or_404(Video,pk=video_id)
		form=VideoForm(request.POST)
		if not form.is_valid():
			return render_to_response('course/watch.html', locals(),
								  context_instance=RequestContext(request))
		user=request.user
		reply=Reply(
			video=video,
			author=user,
			content=form.cleaned_data['content'],
		)
		reply.save()
		return HttpResponseRedirect(reverse('course:watch', args=(video.id,)))

