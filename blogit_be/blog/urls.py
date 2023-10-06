from django.contrib import admin
from django.urls import path, re_path, include
from .views import HomeView ,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView
urlpatterns = [
    # re_path(r'^$', views.index,name = 'index')
    path('',HomeView.as_view(), name = 'index'),
    path('article<int:pk>',ArticleDetailView.as_view(), name='article_details'),
    path('add_post/',AddPostView.as_view(),name = 'add_post'),
    path('add_category/',AddCategoryView.as_view(),name = 'add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name ='update_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name ='delete_post'),
    path('category/<str:cats>/',CategoryView,name = 'category'),
]   
