from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer


class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # # Generate tokens for the created user
            # refresh = TokenObtainPairSerializer.get_token(user)
            # tokens = {
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # }
            message = {
                'success': 'User created successfully',
                'username': user.username,
                # 'tokens': tokens
            }

            return Response(message, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:  # user is authenticated, so isnt None
            login(request, user)

            refresh = TokenObtainPairSerializer.get_token(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(tokens, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
            # add to token to blacklist
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class MyProtectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'message': 'You are authenticated'
        }
        return Response(content)

# class UserLogin(APIView):
#     def post(self, request, format='json'):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#
# class UserLogout(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, format='json'):
#         request.user.auth_token.delete()
#         logout(request)
#         return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

# # 1. Create a User
#
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()  # save() method is provided by ModelSerializer and call my UserSerializer.create() method
#         # internally
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
#
#
# # 2. Get a User
# @api_view(['GET'])
# def get_user(request, pk):
#     user = User.objects.get(pk=pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)
#
#
# # 3. Update a User
# @api_view(['PUT'])
# def update_user(request, pk):
#     user = User.objects.get(pk=pk)
#     serializer = UserSerializer(user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
#
#
# # 4. Delete a User
# @api_view(['DELETE'])
# def delete_user(request, pk):
#     user = User.objects.get(pk=pk)
#     user.delete()
#     return Response(status=204)
