from rest_framework import serializers
from core.models import Foods

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name', 'price', 'image', 'count']
