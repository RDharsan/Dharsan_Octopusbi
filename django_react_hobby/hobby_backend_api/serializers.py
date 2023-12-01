from rest_framework import serializers
from hobby_backend_api.models import User,Hobby

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId',
                'name',
                  'email',
                  'personal_no',
                  'home_no',
                  'username',
                  'password')
        
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('hobbyId',
                'hobbyTitle',
                  'hobbyBody',
                  'userId')