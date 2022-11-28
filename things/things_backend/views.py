from django.shortcuts import render
from rest_framework import viewsets, permissions
from knox.auth import TokenAuthentication


from .models import Post, Category, Tag
from .serializers import PostSerializer, TagSerializer, CategorySerializer
# Create your views here.

class MixinViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PostViewSet(MixinViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class TagViewSet(MixinViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    

class CategoryViewSet(MixinViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer