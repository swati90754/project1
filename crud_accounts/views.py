from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import ProjectModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

import logging
logby =logging.getLogger('user')


class ProjectAPI(APIView):

    def get(self,request):
        projects=Project.objects.all()
        serializer = ProjectModelSerializer(projects,many=True)
        return Response(data=serializer.data)
    
    def post(self,request):
         serializer = ProjectModelSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data)
         return Response(data=serializer.errors)
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    

class ProjectDetailsAPI(APIView):
    def get(self,request,pk=None):
        try:
            obj = Project.objects.get(pk=pk)
        except:
             return Response(data={'message':'Details not found'})
        serializer = ProjectModelSerializer(instance=obj)
        return Response(data=serializer.data)
    
    def put(self,request,pk=None):
        obj = get_object_or_404(Project,pk=pk)
        serializer = ProjectModelSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self,request,pk=None):
        obj = get_object_or_404(Project,pk=pk)
        serializer = ProjectModelSerializer(data=request.data,instance=obj,partial=True)
        if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def delete(self,request,pk=None):
        obj = get_object_or_404(Project,pk=pk)
        obj.delete()
        return Response(data=None)
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
