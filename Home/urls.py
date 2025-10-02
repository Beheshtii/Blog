from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryAPIView.as_view(), name='category'),
    path('', views.HomeAPIView.as_view(), name='home'),
    path('<int:post_id>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('<int:post_id>/<str:slug>/', views.PostDetailAPIView.as_view(), name='post-detail'),

]
