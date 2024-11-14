from rest_framework import serializers
from .models import Member, FoodPost, FoodRequest

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class FoodPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPost
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False},
            'quantity': {'required': False},
            'posted_by': {'required': False},
            'posted_by': {'required': False},
            'expiration_date': {'required': False},
            'photo': {'required': False},
            'whatsapp_link': {'required': False},
            'collection_point': {'required': False},
        }

class FoodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = ['food_post']  # Only the food_post field will be passed in the request

    def create(self, validated_data):
        validated_data['requested_by'] = None
        return super().create(validated_data)

    






