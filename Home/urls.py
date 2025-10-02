from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryAPIView.as_view(), name='category'),
    path('category/<int:category_id>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),
    path('', views.PostAPIView.as_view(), name='post'),
    path('<int:post_id>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('<int:post_id>/<str:slug>/', views.PostDetailAPIView.as_view(), name='post-detail'),

]
