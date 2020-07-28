from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer, UserSerializer
from .permissions import IsAutherOrReadOnly
from .models import Post

# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAutherOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewset(ModelViewSet):
    permission_classes = (IsAutherOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer