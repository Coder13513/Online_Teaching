from rest_framework import serializers
from .models import *


class chapterSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Chapter
        fields      =       '__all__'
       