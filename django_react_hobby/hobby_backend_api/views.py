from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import User, Hobby
from .serializers import UserSerializer, HobbySerializer

class UserView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Added Successfully", safe=False)
        return JsonResponse("Failed to add user", safe=False)
    
    def get_users(self, pk):
        try:
            user = User.objects.get(userId=pk)
            return user
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_u(pk)
            serializer = UserSerializer(data)
        else:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
    

    def put(self, request, pk=None):
        user_to_update = User.objects.get(userId = pk)
        serializer = UserSerializer(instance = user_to_update, data = request.data, many = True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Updated Successfully", safe=False)
        return JsonResponse("Failed to update User", safe=False)
    

    def delete(self, request, pk):
        user_to_delete = User.objects.get(userId = pk)
        user_to_delete.delete()
        return JsonResponse("User Deleted Successfully", safe=False)

    

    
    
class HobbyView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = HobbySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Hobby Added Successfully", safe=False)
        return JsonResponse("Failed to add hobby", safe=False)
    
    def get_hobbies(self, pk, userid):
        try:
            hobby = Hobby.objects.get(hobbyId=pk, userId = userid)
            return hobby
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, userid = None):
        if pk:
            data = self.get_u(pk)
            serializer = HobbySerializer(data)
        else:
            data = Hobby.objects.all()
            serializer = HobbySerializer(data, many=True)
        return Response(serializer.data)
    

    def put(self, request, pk=None, userId=None):
        hobby_to_update = Hobby.objects.get(hobbyId = pk)
        serializer = HobbySerializer(instance = hobby_to_update, data = request.data, many = True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Hobby Updated Successfully", safe=False)
        return JsonResponse("Failed to update Hobby", safe=False)
    

    def delete(self, request, pk):
        hobby_to_delete = Hobby.objects.get(hobbyId = pk)
        hobby_to_delete.delete()
        return JsonResponse("Hobby Deleted Successfully", safe=False)

    

