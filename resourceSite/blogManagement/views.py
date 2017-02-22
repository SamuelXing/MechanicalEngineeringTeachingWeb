from django.shortcuts import get_object_or_404,render_to_response,get_list_or_404,redirect,render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.conf import settings

from .models import  Blog,Comments
from .blog_form import CommentForm


# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'latest_blog_list'

	def get_queryset(self):
		blog=Blog.objects.filter(status=0).order_by('-created_at')[:5]
		return blog


# class DetailView(generic.DetailView):
# 	model = Blog
# 	template_name = 'blog/detail.html'

def blog_detail(request, blog_id):
	if request.method == 'GET':
		blog=get_object_or_404(Blog,pk=blog_id)
		blog.view_times=blog.view_times+1
		blog.save()
		if Comments.objects.filter(blog__id=blog_id).count()==0:
			message=u"暂无评论"
		else:
			comments=get_list_or_404(Comments, blog=blog_id)
		return render_to_response('blog/detail.html', locals(), context_instance=RequestContext(request))
	elif request.method == 'POST':
		if not request.user.is_authenticated():
			return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
		blog=get_object_or_404(Blog,pk=blog_id)
		form=CommentForm(request.POST)
		if not form.is_valid():
			return render_to_response('blog/detail.html', locals(), context_instance=RequestContext(request))
		user=request.user
		comment=Comments(
			blog=blog,
			author=user,
			content=form.cleaned_data['content'],
		)
		comment.save()
		return HttpResponseRedirect(reverse('blog:detail', args=(blog.id,)))

def show(request):
	return render(request,'blog/homepage.html')

def subscription(request):
	return render(request,'blog/subscription.html')





