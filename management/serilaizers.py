from rest_framework import serializers
from .models import Items, CustomUser, Purchase


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
    name = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ("name", "quantity", "amount")
    
    def get_name(self, instance):
        return instance.name.item_name




class PurchasedItemSerializers(serializers.ModelSerializer):
    items = ItemsSerializers( many=True)
    class Meta:
        model = Purchase
        fields = ("purchase_date", "items", "amount_spent")