from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
	url(r'^search/$', views.search, name='search'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
]