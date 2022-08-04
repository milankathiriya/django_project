from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def index(request):
    students = Student.objects.all()
    res = StudentSerializer(students, many=True)
    return Response(res.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def studentDetail(request, pk):
    student = Student.objects.get(id=pk)
    res = StudentSerializer(student, many=False)
    return Response(res.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def studentCreate(request):
    res = StudentSerializer(data=request.data)
    
    if res.is_valid():
        res.save()
        
    return Response(res.data)


@api_view(['POST'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    res = StudentSerializer(instance=student, data=request.data)
    
    if res.is_valid():
        res.save()
        
    return Response(res.data)


@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    
    return Response("Record has been deleted successfully...")
