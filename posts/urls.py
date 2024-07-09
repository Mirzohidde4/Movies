from django.urls import path
from .views import *


urlpatterns = [
    path('search/', SearchPage, name='search'),
    path('', PostView, name='posts'),
    path('<int:id>/detail', PostDetail, name='post_detail'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('category/<slug:slug>/', CategoryPost, name='category_post'),
    path('new/', PostCreate.as_view(), name='post_new'),
]

