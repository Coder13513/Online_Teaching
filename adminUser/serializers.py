from rest_framework import serializers
from .models import *


class adminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Admin
        fields      =       '__all__'
        read_only_fields        =  ['user']
