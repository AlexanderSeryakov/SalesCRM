from rest_framework import serializers
from ..models import Supply


class SupplySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Supply.objects.create(**validated_data)

    class Meta:
        model = Supply
        fields = '__all__'
