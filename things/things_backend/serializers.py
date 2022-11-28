from rest_framework.serializers import ModelSerializer
from .models import Category, Post, Tag

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
