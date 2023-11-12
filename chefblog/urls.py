from django.urls import path
from .views import PostList, PostLike, CategoryListView, CategoryDetailView, PostDetail, toggle_saved, saved_posts

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
    path('category/<str:category_name>/',
         CategoryListView.as_view(), name='category_posts'),
    path('category/detail/<str:category_name>/',
         CategoryDetailView.as_view(), name='category_detail'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('toggle_saved/<int:post_id>/', toggle_saved, name='toggle_saved'),
    path('saved_posts/', saved_posts, name='saved_posts'),
]
