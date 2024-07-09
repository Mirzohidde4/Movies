from django.shortcuts import render
from posts.models import Posts
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import PostsSer, UserSer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permission import MyPermission
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserApi(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSer
    pagination_class = StandardResultsSetPagination


class PostsApi(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSer
    pagination_class = StandardResultsSetPagination


class PostsListView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSer


# class PostsListCreateView(ListCreateAPIView):
#     permission_classes = (IsAdminUser, )
#     queryset = Posts.objects.all()
#     serializer_class = PostsSer


# class PostsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (MyPermission, )
#     queryset = Posts.objects.all()
#     serializer_class = PostsSer
