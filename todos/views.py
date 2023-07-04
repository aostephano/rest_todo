class TodoCreateView:
    pass

# class OldTodoCreateView(APIView):
#     permission_classes = [TodoUserWritePermission]
#
#     def post(self, request, format=None):
#         current_user_pk = self.request.user.pk
#         request.data['user'] = current_user_pk
#
#         serializer_todo = TodoSerializer(data=request.data)
#         if serializer_todo.is_valid():
#             serializer_todo.save()
#             return Response(serializer_todo.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET'])
# @permission_classes([DjangoModelPermissions])
# def todo_list(request, format=None):
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer_todo = TodoSerializer(todos, many=True)
#         return Response(serializer_todo.data)
#
#
# @api_view(['POST'])
# def todo_create(request, format=None):
#     if request.method == 'POST':
#         serializer_todo = TodoSerializer(data=request.data)
#         if serializer_todo.is_valid():
#             serializer_todo.save()
#             return Response(serializer_todo.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['POST'])
# def todo_create_multiple(request, format=None):
#     if request.method == 'POST':
#         serializer_todo = TodoSerializer(data=request.data, many=True)
#         if serializer_todo.is_valid():
#             serializer_todo.save()
#             return Response(serializer_todo.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([TodoUserWritePermission])
# def todo_detail(request, todo_id, format=None):
#     try:
#         todo = Todo.objects.get(pk=todo_id)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer_todo = TodoSerializer(todo, many=False)
#         return Response(serializer_todo.data)
#
#     # PUT = alters a existing todo
#     elif request.method == 'PUT':
#         # In PUT method, i should save() or update()? Get current value > Modify the value passing the new Todo
#         #  inside request > Validate request > Save content > Return Response + 200 Code
#         serializer_todo = TodoSerializer(todo, data=request.data)
#         if serializer_todo.is_valid():
#             serializer_todo.save()
#             return Response(serializer_todo.data)
#         else:
#             return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     # Get current value > Delete the todo > Return Response + 200 Code
#
#
# @api_view(['GET'])
# def user_todos(request, user_id, format=None):
#     if request.method == 'GET':
#         try:
#             user = User.objects.get(id=user_id)
#             try:
#                 todos = Todo.objects.filter(user=user_id)
#                 serializer_todo = TodoSerializer(todos, many=True)
#                 return Response(serializer_todo.data)
#             except Todo.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         except User.DoesNotExist:
#             return Response(status=404, data={'error': 'User not found'})
