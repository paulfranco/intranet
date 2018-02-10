from django.conf.urls import url
from .views import post_detail_view, post_list_view

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', post_list_view, name='list'),
    url(r'^1/$', post_detail_view, name='detail'),
]


