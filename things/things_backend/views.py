from django.shortcuts import render
from knox.auth import TokenAuthentication
from rest_framework import permissions, viewsets

from .models import Category, Post, Tag
from .serializers import CategorySerializer, PostSerializer, TagSerializer


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
