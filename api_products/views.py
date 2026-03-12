from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view

@api_view(['GET'])
def show_items(request):
    items=Item.objects.all()
    serializer=ItemSerializer(items,many=True)
    return Response({'status':200,'data':serializer.data,'message':'Items Display successfully'})


@api_view(['GET'])
def show_one_item(request,pk):
    try:
        one_item=Item.objects.get(id=pk)
        serializer=ItemSerializer(one_item)
        return Response({'status':200,'data':serializer.data,'message':'OneItem Display successfully'})
    except:
        return Response({'status':404,'message':'Item Not Found'})
    
    
@api_view(['POST'])   
def add_item(request):
    serializer=ItemSerializer(data=request.data)
    if (not serializer.is_valid()):
        return Response({'status':400,'message':'Invalid data provided'})
    serializer.save()
    return Response({'status':200,'data':serializer.data,'message':'Data Inserted successfully'})


@api_view(['PUT'])
def update_item(request,pk):
    try:
        one_item=Item.objects.get(id=pk)
        serializer=ItemSerializer(one_item,data=request.data)
        
        if (not serializer.is_valid()):
            return Response({'status':500,'message':'Invalid data provided'})
        
        serializer.save()
        return Response({'status':200,'data':serializer.data,'message':'Data Updated successfully'})
    except:
        return Response({'status':403,'message':'Item Not Found'})
    
    
@api_view(['DELETE'])
def delete_item(request,pk):
    try:
        one_item=Item.objects.get(id=pk)
        one_item.delete()
        return Response({'status':200,'message':'Data Deleted successfully'})
    except:
        return Response({'status':403,'message':'Item Not Found'})