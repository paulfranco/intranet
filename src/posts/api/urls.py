from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    LikeToggleAPIView,
	RepostAPIView,
	PostListAPIView,
	PostCreateAPIView,
    PostDetailAPIView,
   
	)

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^$', PostListAPIView.as_view(), name='list'), #/api/post/
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'), #/post/
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'), # /api/post/id/post/
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'), # /api/post/id/post/
    url(r'^(?P<pk>\d+)/repost/$', RepostAPIView.as_view(), name='repost'),
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'), #/tweet/1/
    # url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'), #/tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete') #/tweet/1/delete
]
