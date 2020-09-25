from rest_framework import serializers
from .models import *


class classesSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Classes
        fields      =       '__all__'
       