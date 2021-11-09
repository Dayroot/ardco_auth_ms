from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from authApp.models import User

        
class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = TokenVerifySerializer(data=request.data)
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        try:
            serializer.is_valid(raise_exception=True)
            token_data = tokenBackend.decode(request.data['token'],verify=False)
            user_id = token_data['user_id']
            user = User.objects.get(id = user_id)
            if(user.is_active == False):
                raise TokenError("user is suspended")
            serializer.validated_data['UserId'] = user_id
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
