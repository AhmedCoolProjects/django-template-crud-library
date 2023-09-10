from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import CategorySerializer
from .models import Category

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Create': '/',
        'Get by ID': '/pk',
        'Get all': '/',
        'Update': '/update/pk',
        'Delete': '/delete/pk',
        'Create from list': '/list',
    }
 
    return Response(api_urls)

@api_view(['POST'])
def create_category(request):
    category = CategorySerializer(data=request.data)

    # check if name exists already 
    if Category.objects.filter(name=request.data['name']).exists():
        raise serializers.ValidationError('This data already exists')
 
    print("category", category)
    if category.is_valid():
        category.save()
        return Response(category.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def all_categories(request):
     
    items = Category.objects.all()
 
    if items:
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'No data found'})

@api_view(['PATCH'])
def update_category(request, pk):
    item = Category.objects.get(pk=pk)
    data = CategorySerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data=data.errors)
    

@api_view(['DELETE'])
def delete_category(request, pk):

    item = Category.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def create_category_from_list(request):

    categories = request.data['categories']
    for category in categories:
        category = CategorySerializer(data=category)
        if category.is_valid():
            category.save()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data=category.errors)
    return Response(status=status.HTTP_201_CREATED, data={'message': 'All categories created successfully'})

@api_view(['GET'])
def category_by_id(request, pk):
    
    item = Category.objects.get(pk=pk)
    serializer = CategorySerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)