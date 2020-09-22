from rest_framework import serializers
from .models import *


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Teacher
        fields      =       '__all__'
        read_only_fields        =  ['user']
