from django.conf.urls import patterns, include, url
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post-list'),
    url(r'^post/(?P<slug>[-_\w]+)/$', views.post_detail, name='post-detail'),
    url(r'^post_create/$', views.CreatePost.as_view(), name='post-create'),
	url(r'^publish_post/(?P<slug>[-_\w]+)/$', views.publish_post, name='publish-post'),
	url(r'^post/update/(?P<slug>[-_\w]+)/$', views.UpdatePost.as_view(), name='post-update'),
	url(r'^post/delete/(?P<slug>[-_\w]+)/$', views.DeletePost.as_view(), name='post-delete'),
)