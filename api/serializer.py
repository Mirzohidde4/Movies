from rest_framework.serializers import ModelSerializer, SerializerMethodField
from posts.models import Posts
from django.contrib.auth import get_user_model


class PostsSer(ModelSerializer):
    category = SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Posts
        fields = '__all__'


class UserSer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "username", "email"]                