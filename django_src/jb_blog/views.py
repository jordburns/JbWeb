from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404
from django.shortcuts import redirect
from .models import Post
from braces.views import PermissionRequiredMixin
from django.utils.text import slugify
from django.core.urlresolvers import reverse_lazy
from fm.views import AjaxCreateView
from jb_blog.forms import PostForm


def post_list(request):

	if request.user.has_perm('jb_blog.add_post'):
		all_posts = Post.objects.all().order_by('published', '-published_date', '-created')
	else:
		all_posts = Post.objects.filter(published=True).order_by('-published_date')

	return render(request, 'jb_blog/post_list.html', {'all_posts': all_posts})


class CreatePost(PermissionRequiredMixin, AjaxCreateView):

	form_class = PostForm
	model = Post
	permission_required = "jb_blog.add_post"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super(CreatePost, self).form_valid(form)


class UpdatePost(PermissionRequiredMixin, UpdateView):

	model = Post
	fields = ['title', 'abstract', 'content', 'published']
	permission_required = "jb_blog.change_post"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super(UpdatePost, self).form_valid(form)


class DeletePost(PermissionRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('post-list')
	permission_required = 'jb_blog.delete_post'
	
def post_detail(request, slug):

	post = Post.objects.get(slug=slug)

	if post.published or request.user.has_perm('jb_blog.change_post'):
		return render(request, 'jb_blog/post_detail.html', {'post':post})
	else:
		raise Http404("Not Staff")


def publish_post(request, slug):

	if request.user.has_perm('jb_blog.change_post'):
		post = Post.objects.get(slug=slug)
		post.publish()
		return redirect('post-list')
	else:
		raise Http404("Not Staff")

	 
