from rest_framework import serializers
from .models import ProductPublisherModels


class ProductPublisherSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductPublisherModels
		fields = '__all__'
