from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # # fields =['name','age']
        # exclude=['id']
        fields = '__all__'