from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.log_in, name='login page'),
    url(r'^logout/', views.log_out, name='logout'),
    url(r'^profile/', views.profile, name='profile page'),
    url(r'^delete/book/(?P<id>[0-9]+)/$', views.delete_book, name='delete book'),
    url(r'^add/', views.add_book, name='add book'),
    url(r'^friends/', views.friend_list, name='user friend list'),
]