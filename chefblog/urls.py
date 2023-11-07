from django.urls import path
from . import views
from .views import CategoryListView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<str:category_name>/',
         CategoryListView.as_view(), name='posts_by_category'),
    path('category/<str:category_name>/',
         views.CategoryDetailView.as_view(), name='category_detail'),
]
