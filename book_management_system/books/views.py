from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import BooksSerializer, CheckoutSerializer
from .models import Books, Checkout
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def checkoutOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booksList(request):
    dabooks = Books.objects.all()
    serializer = BooksSerializer(dabooks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkoutList(request):
    userss = Checkout.objects.all()
    serializer = CheckoutSerializer(userss, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booksDetail(request, pk):
    dabooks = Books.objects.get(id=pk)
    serializer = BooksSerializer(dabooks, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkoutDetail(request, pk):
    userss = Checkout.objects.get(user=pk)
    serializer = CheckoutSerializer(userss, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def booksCreate(request, pk):
    serializer = BooksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkoutCreate(request, pk):
    serializer = CheckoutSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def booksUpdate(request, pk):
    dabook = Books.objects.get(id=pk)
    serializer = BooksSerializer(instance=dabook, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkoutUpdate(request, pk):
    userss = Checkout.objects.get(username=pk)
    serializer = CheckoutSerializer(instance=userss, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def booksDelete(request, pk):
    dabook = Books.objects.get(id=pk)
    dabook.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def checkoutDelete(request, pk):
    userss = Checkout.objects.get(user=pk)
    userss.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)