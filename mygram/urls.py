from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    url('^$',views.home,name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^post/(\d+)',views.post,name ='post') ,
    url(r'^like_home/(\d+)',views.like_home,name ='like1') ,
    url(r'^like_post/(\d+)',views.like_post,name ='like2') ,
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)