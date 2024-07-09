from django.urls import path
from .views import PostsApi, UserApi, PostsListView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', viewset=UserApi, basename='users')

urlpatterns = [
    path('posts', PostsListView.as_view(), name='kitoblar'),
    path('listposts', PostsApi.as_view({'get': 'list'}), name='kitoblar-api'),
    path('listaddposts', PostsApi.as_view({'get':'list', 'post': 'create'}), name='kitoblar-list-create'),
    path('deleteupdateposts/<int:pk>/', PostsApi.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='kitoblar-delete-update'),
    path('users/', UserApi.as_view({'get': 'list', 'post': 'create'})),
]