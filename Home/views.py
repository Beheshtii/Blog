from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import *
from rest_framework.permissions import *

class HomeAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request):
        posts = PostModel.objects.all()
        ser_deta = PostSerializer(posts, many=True)
        return Response(ser_deta.data)

    def post(self, request):
        ser_data = PostSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save(author=request.user)  # 👈 اینجا نویسنده رو ست کن
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request, post_id, slug=None):
        try:
            post = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            return Response({"message": "post not found"}, status=status.HTTP_404_NOT_FOUND)

        ser_data = PostSerializer(post)
        return Response(ser_data.data, status=status.HTTP_200_OK)

class CategoryAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request):
        categories = CategoryModel.objects.all()