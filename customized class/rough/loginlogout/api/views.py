from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from loginout.models import LoginModel
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from api.serializers import Loginserializer

class apiView(APIView):
    def get(self,request):
        log=LoginModel.objects.all()
        serializer=Loginserializer(log,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Loginserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
