#Django
from django.http import Http404
from django.utils.functional import empty

#Django rest framework
from rest_framework.response import Response
from rest_framework import views, status

#model
from authApp.models import User

#serializer
from authApp.serializers import UserSerializer
from authApp.serializers import UserTokenObtainPairSerializer

class UserView(views.APIView):
    
    serializer = UserSerializer
    model = User
    
    def setResult(self, type, content):
        answer = {
            "error": '',
            "result":'',
        }
        answer[type] = content
        return answer
    
    #Gets an instance of the user object specified by id, if not found, returns a 404 status.
    def get_instance(self, data):
        instance = self.model.objects.filter(**data)
        return instance
    
    #Returns the data of the user specified by id
    def get(self,request, *args, **kwargs):
        instance = self.get_instance(kwargs)
        if len(instance) == 0:
            result = self.setResult('error', 'user not found')
            return Response( result, status = status.HTTP_404_NOT_FOUND)
        
        mydata =self.serializer(instance[0]).data
        result = self.setResult('result', mydata)
        return Response(result, status = status.HTTP_200_OK)
    
    #Allows you to register a new user, if the username or email of the user is already registered, 
    # it will return a error with the field that must be changed.
    def post(self, request, *args, **kwargs):
        username = {"username": request.data['username']}
        email = {"email": request.data['email']}
    
        if len(self.get_instance(username))!= 0 and len(self.get_instance(email)) != 0:
            result = self.setResult('error','the username and email entered are registered')
            return Response(result, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        
        elif len(self.get_instance(username)) != 0:
            result = self.setResult('error','the username entered is already in use')
            return Response(result, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        
        elif len(self.get_instance(email)) != 0:
            result = self.setResult('error','the email entered is already in use')
            return Response(result, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        
        serializer = self.serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        
        tokenSerializer = UserTokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        result = self.setResult('result',tokenSerializer.validated_data)
        return Response(result, status= status.HTTP_201_CREATED)
    
    #Update user data
    def put(self, request, *args, **kwargs):
        id = {"id": request.data.pop('id')}
        instance = self.get_instance(id)
        if len(instance)== 0:
            result = self.setResult('error', 'user not found')
            return Response(result, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        
        serializer = self.serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = self.setResult('result',serializer.validated_data)
        return Response(result, status= status.HTTP_200_OK)
    
    #Delete user data
    def delete(self, request, *args, **kwargs):
        instance = self.get_instance(kwargs)
        if len(instance)== 0:
            result = self.setResult('error', 'user not found')
            return Response(result, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        instance.delete()
        result = self.setResult('result','successful deletion')
        return Response(result, status= status.HTTP_200_OK)