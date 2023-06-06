from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

from rest_framework.decorators import permission_classes

from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes([])  # Override the default permission that has been put in the settings to be empty "NO CHECK HERE"
def signup(request):
    data = {'data': '', 'status': ''}

    user_serialized = UserSerializer(data=request.data)

    if user_serialized.is_valid():
        user_serialized.save()

        print(Token.objects.get(user__username=user_serialized.data.get('username')))

        data['data'] = {
            'user': user_serialized.data,
            'token': Token.objects.get(user__username=user_serialized.data.get('username')).key,
            'message': 'Created'
        }
        data['status'] = status.HTTP_201_CREATED
    else:
        data['data'] = user_serialized.errors
        data['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**data)
