from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
	PostCreateView,
	PostListView, 
	PostDetailView,
	PostUpdateView,
	PostDeleteView
	#, post_detail_view, 
	#post_list_view, 
	)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^search/$', PostListView.as_view(), name='list'), #/post/
    url(r'^create/$', PostCreateView.as_view(), name='create'), #/post/create
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'), #/tweet/1/
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'), #/tweet/1/update
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete') #/tweet/1/delete
]


