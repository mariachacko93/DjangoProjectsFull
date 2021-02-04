from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from api.serializers import bookSerializers
from Books.models import Books
# api/books-->for creating and listing all books
from rest_framework import status

class booklist(APIView):
    def get(self,request):
        books=Books.objects.all()
        serializer=bookSerializers(books,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=bookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Bookdetails(APIView):
    def get_object(self,id):
        return Books.objects.get(id=id)
    def get(self,request,id):
        book=self.get_object(id)
        serializer=bookSerializers(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
