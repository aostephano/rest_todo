from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from todos import views

urlpatterns = [
    # Class Based Views
    path('todo_user_list', views.TodoUserListView.as_view(), name='todo_user_list'),
    path('todo_create', views.TodoCreateView.as_view(), name='todo_create'),

    # Func Based Views
    # path('todo_create', views.todo_create, name='todo_create'),
    path('todo_create_multiple', views.todo_create_multiple, name='todo_create_multiple'),
    path('<int:todo_id>', views.todo_detail, name='todo_detail'),
    path('user_todos/<int:user_id>', views.user_todos, name='user_todos'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
