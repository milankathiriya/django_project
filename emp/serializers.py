from rest_framework import serializers
from .models import Employee

# model object => json data

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
