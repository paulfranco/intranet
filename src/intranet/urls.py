from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static 

from hashtags.views import HashTagView
from posts.views import PostListView
from .views import home

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^post/', include('posts.urls', namespace='post')),
    url(r'^api/post/', include('posts.api.urls', namespace='post-api')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^', include('accounts.urls', namespace='profiles')),
     
]


if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))