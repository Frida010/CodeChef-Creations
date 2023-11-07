from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<str:category_name>/', views.CategoryListView.as_view(),
         name='category_posts'),  # Link to category posts
    path('category/detail/<str:category_name>/', views.CategoryDetailView.as_view(),
         name='category_detail'),  # Link to category details
    path('post/<slug:slug>/', views.PostDetail.as_view(),
         name='post_detail'),  # Link to blogpost details
]
