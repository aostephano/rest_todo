from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer_todo = TodoSerializer(todos, many=True)
        return Response(serializer_todo.data)


@api_view(['POST'])
def todo_create(request):
    if request.method == 'POST':
        serializer_todo = TodoSerializer(data=request.data)
        if serializer_todo.is_valid():
            serializer_todo.save()
            return Response(serializer_todo.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def todo_create_multiple(request):
    if request.method == 'POST':
        serializer_todo = TodoSerializer(data=request.data, many=True)
        if serializer_todo.is_valid():
            serializer_todo.save()
            return Response(serializer_todo.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_todo = TodoSerializer(todo, many=False)
        return Response(serializer_todo.data)

    # PUT = alters a existing todo
    elif request.method == 'PUT':
        # In PUT method, i should save() or update()? Get current value > Modify the value passing the new Todo
        #  inside request > Validate request > Save content > Return Response + 200 Code
        serializer_todo = TodoSerializer(todo, data=request.data)
        if serializer_todo.is_valid():
            serializer_todo.save()
            return Response(serializer_todo.data)
        else:
            return Response(serializer_todo.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # Get current value > Delete the todo > Return Response + 200 Code
