from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static 

from accounts.views import UserRegisterView

from hashtags.api.views import TagPostAPIView
from hashtags.views import HashTagView
from posts.api.views import SearchPostAPIView
from posts.views import PostListView
from .views import home, SearchView

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^post/', include('posts.urls', namespace='post')),
    url(r'^api/tags/(?P<hashtag>.*)/$', TagPostAPIView.as_view(), name='tag-post-api'),
    url(r'^api/search/$', SearchPostAPIView.as_view(), name='search-api'),
    url(r'^api/post/', include('posts.api.urls', namespace='post-api')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('accounts.urls', namespace='profiles')),
     
]


if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))