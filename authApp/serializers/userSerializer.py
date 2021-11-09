from authApp.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    username= serializers.CharField()
    
    class Meta:
        model= User
        fields = '__all__'

    def create(self, validated_data):
        new_user = self.Meta.model(**validated_data)
        new_user.save()  
        return new_user
    
    def update(self, instance, data):
        if data.get("password") != None:
            some_salt= 'mMUj0DrIK6vgtdIYepkIxN'
            data['password'] = make_password(data['password'], some_salt)         
        return instance.update(**data)

    def to_representation(self, instance):
        return {
                    'id':instance.id,
                    'username': instance.username,
                    'fullname': instance.fullname,
                    'datebirth': instance.datebirth,
                    'email': instance.email,
                    'identification': instance.identification,
                    'phone_number':instance.phone_number,
                    'address': instance.address    
                }
            
           
           