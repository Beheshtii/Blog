from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import CategorySerializer
from Home.serializers import PostSerializer
from Home.models import *
from rest_framework.permissions import *
from django.shortcuts import get_object_or_404

class CategoryAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request):
        categories = CategoryModel.objects.all()
        ser_data = CategorySerializer(categories, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        ser_data = CategorySerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request, category_id):
        category: CategoryModel = get_object_or_404(CategoryModel, id=category_id)
        ser_data = CategorySerializer(category)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def put(self, request: Request, category_id):
        category: CategoryModel = get_object_or_404(CategoryModel, id=category_id)
        ser_data = CategorySerializer(instance=category, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, category_id):
        category: CategoryModel = get_object_or_404(CategoryModel, id=category_id)
        category.delete()
        return Response({"message": "category deleted"}, status=status.HTTP_204_NO_CONTENT)

class PostAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request):
        posts = PostModel.objects.all()
        ser_data = PostSerializer(posts, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        ser_data = PostSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save(author=request.user)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request, post_id):
        post: PostModel = get_object_or_404(PostModel, id=post_id)
        ser_data = PostSerializer(post)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def put(self, request: Request, post_id):
        post: PostModel = get_object_or_404(PostModel, id=post_id)
        ser_data = PostSerializer(instance=post, data=request.data)
        if ser_data.is_valid():
            ser_data.save(author=request.user)
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, post_id):
        post: PostModel = get_object_or_404(PostModel, id=post_id)
        post.delete()
        return Response({"message": "post deleted"}, status=status.HTTP_204_NO_CONTENT)