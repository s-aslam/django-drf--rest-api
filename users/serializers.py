from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#-----------------------------------------------------------------#

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})
#-----------------------------------------------------------------#

class UserTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True)
    class Meta:
        model = Token
        fields = ('token',) 
#-----------------------------------------------------------------#
