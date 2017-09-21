from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^new$',views.post_new,name='post_new'),
    url(r'^photo$', views.photo, name='photo'),
    url(r'^about$', views.about, name='about'),
    url(r'^member$', views.member, name='member'),
    url(r'^introduce$', views.introduce, name='introduce'),
          
    
]