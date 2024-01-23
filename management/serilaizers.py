from rest_framework import serializers
from .models import Items, CustomUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=225)

    class Meta:
        fields = ("username", "password")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password")


class UserCreationSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ("name", "quantity", "amount")