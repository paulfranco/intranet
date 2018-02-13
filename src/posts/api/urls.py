from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
	PostListAPIView,

	)

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^$', PostListAPIView.as_view(), name='list'), #/api/post/
    # url(r'^create/$', PostCreateView.as_view(), name='create'), #/post/create
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'), #/tweet/1/
    # url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'), #/tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete') #/tweet/1/delete
]