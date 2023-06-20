from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from todos import views

urlpatterns = [
    path('', views.todo_list),
    path('create/', views.todo_create),
    path('create_multiple/', views.todo_create_multiple),
    path('<int:todo_id>', views.todo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
