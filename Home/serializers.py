from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField(read_only=True)
    slug = serializers.SerializerMethodField(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = PostModel
        fields = '__all__'
        extra_kwargs = {'slug': {'read_only': True}, 'created_at': {'read_only': True}, 'updated_at': {'read_only': True}}

    def get_slug(self, obj):
        return obj.get_absolute_url()