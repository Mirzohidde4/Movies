from django.urls import path
from .views import HomePage, UserSetting, UpdatePassword, UpdateName, Admin


urlpatterns = [
    path('', HomePage, name='home'),
    path('user_setting/', UserSetting, name='user_setting'),
    path('update_pass/', UpdatePassword, name='update_pass'),
    path('update_name/', UpdateName, name='update_name'),
    path('admin', Admin, name='admin'),
]