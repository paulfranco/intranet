from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostListView
from .views import home

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('posts.urls', namespace='post'))
]


if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))