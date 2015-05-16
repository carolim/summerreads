from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.log_in, name='Login Page'),
    url(r'^logout/', views.log_out, name='Logout'),
    url(r'^profile/', views.profile, name='Profile Page'),
    url(r'^add/', views.add_book, name='Add Book'),
]