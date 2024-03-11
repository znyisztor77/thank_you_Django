from rest_framework.serializers import ModelSerializer
from .models import Refuel


class RefueSerializer(ModelSerializer):
    class Meta:
        model = Refuel
        fields = '__all__'