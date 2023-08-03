from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views  import APIView

class RegisterUser(APIView):
    def get(self,request):
        uobj = User.objects.all()
        serializer=registerUser(uobj,many=True)
        return Response(data=serializer.data)
    
    def post(self,request):
        serializer=registerUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)