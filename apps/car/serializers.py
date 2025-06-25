from rest_framework import serializers
from apps.car.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'updated_at', 'created_at')

    # id = serializers.IntegerField(read_only=True)
    # brand = serializers.CharField(max_length=20)
    # year = serializers.IntegerField()
    # price = serializers.FloatField()
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data:dict):
    #     return CarModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data:dict):
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     return instance
