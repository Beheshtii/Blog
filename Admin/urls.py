from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryAPIView.as_view(), name='admin-category'),
    path('category/<int:category_id>/', views.CategoryDetailAPIView.as_view(), name='admin-category-detail'),
    path('post/', views.PostAPIView.as_view(), name='admin-post'),
    path('post/<int:post_id>/', views.PostDetailAPIView.as_view(), name='admin-post-detail'),

]
