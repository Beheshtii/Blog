from rest_framework import serializers
from Home.models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'