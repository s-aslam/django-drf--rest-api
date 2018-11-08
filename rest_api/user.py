from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes


from base.api_functions import successResponse, errorResponse
from base.api_messages import response_text, api_message, getSerializer_errors

from users.models import User
from users import serializers
from users.helper import get_login_user_dict

user_model = get_user_model()

class Loginview(generics.GenericAPIView):    
    serializer_class = serializers.LoginSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request):
        print("=====> request.data:",request.data)
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            # check for existence            
            get_user = user_model.objects.filter(username=request.data.get('email')).first()
            if not get_user:
                success = False
                error=list()
                error.append(api_message['email_not_exist'])
                response_data = errorResponse(success,error) 
            if get_user:   
                if not get_user.is_active:
                    success = False
                    error=list()
                    error.append(api_message['account_deactivated'])
                    response_data = errorResponse(success,error) 

                else:
                    get_user = authenticate(username=request.data.get('email'), password=request.data.get('password'))
                    if get_user:
                        if  False:#get_user.is_deleted:
                       
                            success = False
                            error=list()
                            error.append(api_message['email_not_exist'])
                            response_data = errorResponse(success,error)
                        else:
                            token = Token.objects.get_or_create(user=get_user)[0]
                            # get_user.is_online = True
                            get_user.save()
                            success = True
                            data = get_login_user_dict(request, get_user,token)
                            message = api_message['login_success']
                            response_data = successResponse(success,data,message)

                    else:
                        # Here email is exist bit password is wrong so success is True but code is 400
                        success = False
                        error=list()
                        error.append(api_message['wrong_credentials'])
                        response_data = errorResponse(success,error)
            else:
                success = False
                error=list()
                error.append(api_message['wrong_credentials'])
                response_data = errorResponse(success,error)  
        else:
            # print("serializer_data:",serializer_data.errors)
            success = False
            error=list()
            # error=serializer_data.errors
            # error.append(response_text[400])
            error = getSerializer_errors(serializer_data.errors)
            response_data = errorResponse(success,error)
           
        return Response(response_data , status=response_data.get("code"))


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        request.user.save()
        success = True
        # data = list()
        # message = api_message['success_logout']
        response_data = successResponse(success)      
        return Response(response_data,status=response_data["code"])