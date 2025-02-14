from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('<slug:slug>/', views.blog_page, name='blog_page'),
]
