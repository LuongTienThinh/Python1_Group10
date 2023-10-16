from django.contrib import admin
from django.urls import path, re_path, include
from .views import HomeView ,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,AddReplyView,CategoryView,CategoryListView,LikeView,AddCommentView,DraftView,AdminView,AdminUpdatePostView,DeleteCommentView,search_posts,ProfileDetailView, ProfileUpdateView
urlpatterns = [
    # re_path(r'^$', views.index,name = 'index')
    path('',HomeView.as_view(), name = 'index'),
    path('draft',DraftView.as_view(), name = 'draft'),
    path('adminview',AdminView.as_view(), name = 'admin'),
    path('article<int:pk>',ArticleDetailView.as_view(), name='article_details'),
    path('add_post/',AddPostView.as_view(),name = 'add_post'),
    path('add_category/',AddCategoryView.as_view(),name = 'add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name ='update_post'),
    path('article/admin-edit/<int:pk>',AdminUpdatePostView.as_view(),name ='admin_update_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name ='delete_post'),
    path('category/<str:cats>/',CategoryView,name = 'category'),
    path('category-list/',CategoryListView,name = 'category-list'),
    path('like/<int:pk>',LikeView, name='like_post'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(), name ='add_comment'),
    path('article/<int:pk>/comment/<int:parent_id>', AddReplyView.as_view(), name='add_reply'),
    path('article/<int:post_pk>/comment/<int:pk>/delete',DeleteCommentView.as_view(), name ='delete_comment'),
    path('search/', search_posts, name='search_posts'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
]   
