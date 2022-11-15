from rest_framework import serializers
from .models import Descuentos


class DescuentosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Descuentos
        fields = '__all__'