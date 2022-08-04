from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.DjangoModelPermissions]


# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         pass
    
#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(Employee, id=pk)
#         serializer = EmployeeSerializer(queryset, many=False)
#         return Response(serializer.data)
    
#     def destroy(self, request):
#         pass
    
#     def update(self, request):
#         pass

# class EmployeeList(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    

# class EmployeeList(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         res = EmployeeSerializer(employees, many=True)
#         return Response(res.data)
    
#     def post(self, request):
#         res = EmployeeSerializer(data=request.data)
        
#         if res.is_valid():
#             res.save()
#             return Response(res.data)
#         return Response(res.errors)



# class EmployeeDetail(APIView):
#     def get(self, request, pk):
#         emp = get_object_or_404(Employee, id=pk)
#         res = EmployeeSerializer(emp, many=False)
#         return Response(res.data)
    
#     def put(self, request, pk):
#         emp = get_object_or_404(Employee, id=pk)
        
#         res = EmployeeSerializer(emp, data=request.data)
        
#         if res.is_valid():
#             res.save()
#             return Response(res.data)
#         return Response(res.errors)
    
#     def delete(self, request, pk):
#         emp = get_object_or_404(Employee, id=pk)
#         emp.delete()
#         return Response('Deleted successfully...')
