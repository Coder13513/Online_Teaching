from rest_framework import serializers
from .models import *


class assignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model       =      Assignment
        fields      =       '__all__'
       


class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Question
        fields      =       '__all__'
      


class choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model       =    Choice
        fields      =       '__all__'
      


class quizSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Quiz
        fields      =       '__all__'
      

