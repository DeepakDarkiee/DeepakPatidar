from . import views
from django.urls import include
from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from django.contrib import admin


urlpatterns = [
    path("", views.home,name='home'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("blog/", views.PostList.as_view(), name="blog"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
   
]
