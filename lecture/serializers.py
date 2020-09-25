from rest_framework import serializers
from .models import *


class lectureSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Lecture
        fields      =       '__all__'
        read_only_fields        =  ['user']
