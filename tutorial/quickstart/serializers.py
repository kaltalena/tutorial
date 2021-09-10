from django.contrib.auth.models import User, Group
from tutorial.quickstart.models import Building
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['price', 'surface', 'room_count', 'address']
