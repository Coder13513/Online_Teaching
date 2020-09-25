from rest_framework import serializers
from .models import *


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Subject
        fields      =       '__all__'
        read_only_fields        =  ['class_id']
