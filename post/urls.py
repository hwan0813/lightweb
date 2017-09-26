from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^new$',views.post_new,name='post_new'),
    url(r'^photo$', views.photo, name='photo'),
    url(r'^about$', views.about, name='about'),
    url(r'^member$', views.member, name='member'),
    url(r'^introduce$', views.introduce, name='introduce'),
    url(r'^board$', views.board, name='board'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name = 'post_detail'),
    # url 막바꿔도 이제 url reverse때매 알아서 하이퍼링크바뀐주소가 잘 찾아서감.                 
]