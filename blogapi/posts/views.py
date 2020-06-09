from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializers import PostSerializer
from .serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer