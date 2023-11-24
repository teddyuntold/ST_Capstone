from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BooksSerializer
from .models import Books

# Create your views here.
@api_view(['GET'])
def booksOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def booksList(request):
    dabooks = Books.objects.all()
    serializer = BooksSerializer(dabooks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def booksDetail(request, pk):
    dabooks = Books.objects.get(id=pk)
    serializer = BooksSerializer(dabooks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def booksCreate(request, pk):
    serializer = BooksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def booksUpdate(request, pk):
    dabook = Books.objects.get(id=pk)
    serializer = BooksSerializer(instance=dabook, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def booksDelete(request, pk):
    dabook = Books.objects.get(id=pk)
    dabook.delete()
    return Response(serializer.data)