from django.db import models
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import generics
from rest_framework.response import Response
from base.api_functions import successResponse,errorResponse
from base.api_messages import response_text,api_message,getSerializer_errors, page_size
from datetime import datetime
from product.models import Product
from product.helper import getProductList,getProductData
from product.serializers import ProductSerializer

class ProductListApi(generics.GenericAPIView):
    """
    List all objects, or create a new objects.
    """   
    # function for searching in list

    permission_classes = [IsAuthenticated]
    model = Product
    serializer_class = ProductSerializer
    get_object_list = getProductList
    get_object_data = getProductData

    def get(self, request, format=None):
        objects = self.model.objects.filter(is_deleted=False).order_by('-created_date')
        if objects:

            success = True
            data =  self.get_object_list(objects)
            response_data = successResponse(success,data)
        else:
            success = True
            error=list()
            error.append(response_text[603])
            code=200
            response_data = errorResponse(success,error,code)  
        
        return Response(response_data,status=response_data["code"])
     
    def post(self, request, format=None):        

        serializer = self.serializer_class(data=request.data)   
        
        if serializer.is_valid():
            instance = serializer.save()
            instance.created_by = request.user.id
            instance.updated_by = request.user.id
            instance.save()
           
            success = True
            data =  self.get_object_data(instance)
            response_data = successResponse(success,data)
            # return Response(response_data,status=response_data["code"])

        else:
            print(serializer.errors)
            success = False
            error=list()
            error.append(response_text[400])
            error = list(serializer.errors)
            error = getSerializer_errors(serializer.errors)
            response_data = errorResponse(success,error)
            # return Response(response_data,status=response_data["code"])
      
        return Response(response_data,status=response_data["code"])  

class ProductDetailApi(generics.GenericAPIView):
    """
    Retrieve, update, delete and change active status of a model instance.
    """
    permission_classes = [IsAuthenticated]
    model = Product
    serializer_class = ProductSerializer
    get_object_list = getProductList
    get_object_data = getProductData

    def get(self, request, pk,  format=None):
        get_instance = None
        try:
            get_instance = self.model.objects.filter(is_deleted=False).get(pk=int(pk))
        except self.model.DoesNotExist:
            success = True
            error=list()
            error.append(response_text[603])
            code=200
            response_data = errorResponse(success,error,code)
                                                
        if get_instance:
            success = True
            data =  self.get_object_data(get_instance)
            response_data = successResponse(success,data)
        else:
            success = True
            error=list()
            error.append(response_text[603])
            code=200
            response_data = errorResponse(success,error,code) 
                  
        return Response(response_data,status=response_data["code"])

    def put(self, request, pk, format=None):
        get_instance = None
        try:
            get_instance = self.model.objects.filter(is_deleted=False).get(pk=int(pk))
        except self.model.DoesNotExist:
            success = True
            error=list()
            error.append(response_text[603])
            response_data = successResponse(success,error)
            return Response(response_data,status=response_data["code"])
        
        serializer = self.serializer_class(get_instance, data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.updated_by = request.user.id
            instance.save()
            success = True
            data =  self.get_object_data(instance)
            response_data = successResponse(success,data)
            # return Response(response_data,status=response_data["code"])
        else:
            print(serializer.errors)
            success = False
            error = list()
            error = getSerializer_errors(serializer.errors)
            response_data = errorResponse(success,error)
            # return Response(response_data,status=response_data["code"])
      
        return Response(response_data,status=response_data["code"]) 

    
    def patch(self, request, pk, format=None):
        instance = None
        try:
            instance = self.model.objects.filter(is_deleted=False, pk=int(pk)).first()
        except self.model.DoesNotExist:
            success = False
            error = list()
            error.append(response_text[603])
            response_data = errorResponse(success,error)
        if instance:
            instance.is_active = False if instance.is_active else True
            instance.save()
            success = True
            data = { 'is_active': instance.is_active }
            response_data = successResponse(success, data)        
        return Response(response_data,status=response_data["code"])
    
    def delete(self, request, pk, format=None):
        instance = None        
        try:
            instance = self.model.objects.filter(is_deleted=False, pk=int(pk)).first()
        except self.model.DoesNotExist:
            success = False
            error = list()
            error.append(response_text[603])
            response_data = errorResponse(success,error)
            return Response(response_data,status=response_data["code"])

        if instance:
            instance.is_active=False
            instance.is_deleted=True
            instance.save()
            success = True
            response_data = successResponse(success)
        else:
            success = False
            error=list()
            error.append(response_text[603])
            response_data = errorResponse(success,error)             
        return Response(response_data,status=response_data["code"])