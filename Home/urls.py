from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostAPIView.as_view(), name='post'),
    path('<int:post_id>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('<int:post_id>/<str:slug>/', views.PostDetailAPIView.as_view(), name='post-detail'),

]
