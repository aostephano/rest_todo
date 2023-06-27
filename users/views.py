from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


# 1. Create a User

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # save() method is provided by ModelSerializer and call my UserSerializer.create() method
        # internally
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# 2. Get a User
@api_view(['GET'])
def get_user(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


# 3. Update a User
@api_view(['PUT'])
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# 4. Delete a User
@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return Response(status=204)

