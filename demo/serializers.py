from rest_framework import serializers
from .models import Student

# model object => json data

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
